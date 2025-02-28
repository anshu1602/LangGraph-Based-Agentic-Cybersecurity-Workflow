from langgraph.graph import StateGraph, END
from src.models import PipelineState, Task
from src.tools import SecurityTools
import re

def task_generator(state: PipelineState) -> PipelineState:
    state.tasks.append(Task(id="1", description="Scan ports", command="nmap google.com"))
    return state

def task_executor(state: PipelineState) -> PipelineState:
    for task in state.tasks:
        if task.status == "pending":
            try:
                output = SecurityTools.run_nmap(task.command.split()[-1], state.scope)
                task.output = output
                task.status = "completed"
                
                # Dynamic task update based on scan results
                if "nmap" in task.command.lower():
                    if re.search(r"80/tcp\s+open", output):
                        state.tasks.append(Task(
                            id=f"{task.id}.1",
                            description="Directory enumeration on port 80",
                            command="gobuster dir -u http://google.com -w common.txt"
                        ))
                        state.logs.append(f"Added gobuster task based on open port 80")
                    elif re.search(r"22/tcp\s+open", output):
                        state.tasks.append(Task(
                            id=f"{task.id}.2",
                            description="SSH scan",
                            command="nmap -p 22 --script ssh-auth-methods google.com"
                        ))
                        state.logs.append(f"Added SSH scan task based on open port 22")
                
            except Exception as e:
                task.status = "failed"
                state.logs.append(f"Task {task.id} failed: {str(e)}")
            break
    return state

def build_workflow():
    workflow = StateGraph(PipelineState)
    workflow.add_node("generator", task_generator)
    workflow.add_node("executor", task_executor)
    
    workflow.set_entry_point("generator")
    workflow.add_edge("generator", "executor")
    
    # Conditional edges with proper mapping
    workflow.add_conditional_edges(
        "executor",
        lambda state: "__end__" if all(t.status in ["completed", "failed"] for t in state.tasks) else "executor",
        {
            "executor": "executor",  # Loop back to executor if tasks remain
            "__end__": END           # End workflow if all tasks are done
        }
    )
    
    return workflow.compile()