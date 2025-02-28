from src.pipeline import build_workflow
from src.models import PipelineState, ScopeConfig
from src.reporting import generate_report

def main():
    scope = ScopeConfig(domains=["google.com"], ip_ranges=["142.250.0.0/16"])
    state = PipelineState(tasks=[], scope=scope, logs=[])
    
    app = build_workflow()
    final_state = app.invoke(state)
    
    generate_report(final_state)
    print("Pipeline completed. Check outputs/security_report.json")

if __name__ == "__main__":
    main()