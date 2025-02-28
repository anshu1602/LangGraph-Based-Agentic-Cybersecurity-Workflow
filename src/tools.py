import subprocess
from src.scope import ScopeManager
from src.models import ScopeConfig  # Yeh line add karo

class SecurityTools:
    @staticmethod
    def run_nmap(target: str, scope: ScopeConfig) -> str:
        if not ScopeManager.is_in_scope(target, scope):
            raise ValueError(f"Target {target} outside scope")
        cmd = f"nmap -Pn {target}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout