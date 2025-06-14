"""
Intel Linker - CrossComPJxAI
Links and correlates collected recon intel for operator review.
"""

from datetime import datetime
from config import C2_URL, OPERATOR_ID

def link_intel(*intel_sources):
    linked = {}
    for src in intel_sources:
        if isinstance(src, dict):
            for k, v in src.items():
                if k not in linked:
                    linked[k] = []
                linked[k].append(v)
    return linked

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

if __name__ == "__main__":
    # Example usage
    a = {"host": "target1", "ip": "10.0.0.1"}
    b = {"host": "target2", "ip": "10.0.0.2"}
    print(link_intel(a, b))