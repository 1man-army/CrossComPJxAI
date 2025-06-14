"""
Voice Router - CrossComPJxAI
Routes operator voice commands to agent actions (stub/demo).
"""

from config import C2_URL, OPERATOR_ID
from datetime import datetime

def route_voice_command(cmd):
    # In real use, integrate with speech-to-text and agent comms
    print(f"[VOICE] Routing command: {cmd}")

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        route_voice_command(" ".join(sys.argv[1:]))
    else:
        print("Usage: python voice_router.py <command>")