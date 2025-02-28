
import json
from src.models import PipelineState

def generate_report(state):
    # Agar state ek AddableValuesDict hai, toh usse PipelineState ke form mein access karo
    tasks = state.get("tasks", [])  # Dictionary se tasks nikalo
    logs = state.get("logs", [])    # Dictionary se logs nikalo
    
    report = {
        "tasks": [task.dict() for task in tasks],  # Tasks ko list mein convert karo
        "logs": logs
    }
    with open("outputs/security_report.json", "w") as f:
        json.dump(report, f)