"""
AI Task Suggestion Module - CrossComPJxAI
Suggests next operator actions based on collected intel.
"""

from config import C2_URL, OPERATOR_ID
from datetime import datetime

def suggest_tasks(context):
    if "NTLM" in str(context):
        return ["Try pass-the-hash lateral movement.", "Dump Kerberos tickets.", "Escalate privileges."]
    if "linux" in str(context).lower():
        return ["Check for sudo/root access.", "Enumerate SSH keys.", "Scan for cron jobs."]
    return ["Run full recon.", "Check persistence.", "Monitor for anomalies."]

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

if __name__ == "__main__":
    print(suggest_tasks({"platform": "Windows", "NTLM": "hash"}))