import subprocess
from src.scope import ScopeManager
from src.models import ScopeConfig

class SecurityTools:
    @staticmethod
    def run_nmap(target: str, scope: ScopeConfig) -> str:
        if not ScopeManager.is_in_scope(target, scope):
            raise ValueError(f"Target {target} outside scope")
        cmd = f"nmap -Pn {target}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout

    @staticmethod
    def run_gobuster(target: str, scope: ScopeConfig) -> str:
        if not ScopeManager.is_in_scope(target, scope):
            raise ValueError(f"Target {target} outside scope")
        cmd = f"gobuster dir -u {target} -w common.txt"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout