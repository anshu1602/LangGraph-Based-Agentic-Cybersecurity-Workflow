import logging
from src.models import ScopeConfig  # Yeh line add karo

logging.basicConfig(filename='logs/security_pipeline.log', level=logging.INFO)

class ScopeManager:
    @staticmethod
    def is_in_scope(target: str, scope: ScopeConfig) -> bool:
        is_allowed = any(domain in target for domain in scope.domains)
        if not is_allowed:
            logging.warning(f"Target {target} is outside defined scope")
        return is_allowed