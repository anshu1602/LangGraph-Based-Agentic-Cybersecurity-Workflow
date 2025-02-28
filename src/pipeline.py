
from langgraph.graph import StateGraph, END
from src.models import PipelineState, Task
from src.tools import SecurityTools

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
            except Exception as e:
                task.status = "failed"
                state.logs.append(f"Task {task.id} failed: {str(e)}")
            break
    return state

def build_workflow():
    workflow = StateGraph(PipelineState)
    workflow.add_node("generator", task_generator)
    workflow.add_node("executor", task_executor)
    
    # Entry point set karo
    workflow.set_entry_point("generator")  # Yeh line add karo
    
    workflow.add_edge("generator", "executor")
    workflow.add_edge("executor", END)
    return workflow.compile()