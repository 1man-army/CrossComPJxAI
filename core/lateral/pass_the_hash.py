from config import C2_URL, OPERATOR_ID
from datetime import datetime
import socket
import random
import uuid

"""
CrossComPJxAI - Pass-the-Hash Lateral Movement Automation
Enhanced simulation with agent fingerprinting, network awareness, and expanded logging.
"""

def get_agent_id():
    return str(uuid.uuid4())[:8].upper()

def get_hostname():
    return socket.gethostname()

def automate_lateral_movement(creds):
    agent_id = get_agent_id()
    hostname = get_hostname()

    for user, data in creds.items():
        hash_value = data.get("NTLM")
        if hash_value:
            try:
                print(f"[MOVE:{agent_id}] Using NTLM hash for {user} → attempting SMB/RDP lateral move from {hostname}...")
                log_event(f"[{agent_id}] Pass-the-hash → {user} via NTLM from {hostname}")
                send_status(f"{user}'s hash used for lateral move. Agent {agent_id} reporting to {C2_URL}")
            except Exception as e:
                log_event(f"[{agent_id}] ERROR while moving laterally as {user}: {str(e)}")

def log_event(msg):
    with open("agent.log", "a") as log_file:
        log_file.write(f"[{datetime.now().isoformat()}] {msg}\n")

def send_status(msg):
    # Simulated operator uplink - insert API beaconing here in production
    print(f"[STATUS] {msg} | OPERATOR: {OPERATOR_ID}")

if __name__ == "__main__":
    # Sample simulated credentials
    sample_creds = {
        "admin": {"NTLM": "aad3b435b51404eeaad3b435b51404ee:cc39e91ba7fc8bdb5bb63b86945f1315"},
        "svc_account": {"NTLM": "aad3b435b51404eeaad3b435b51404ee:7ff658ec6ab0dc02c123456789abcdef"},
    }
    automate_lateral_movement(sample_creds)