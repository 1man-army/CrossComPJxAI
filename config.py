from config import C2_URL, OPERATOR_ID
from datetime import datetime

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")