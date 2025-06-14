"""
Mode Switch - CrossComPJxAI
Switches agent/operator between Red Team (offensive) and Blue Team (defensive) modes.
"""

import sys
from config import C2_URL, OPERATOR_ID
from datetime import datetime

MODES = {
    "red": "Offensive mode: full recon, lateral movement, persistence enabled.",
    "blue": "Defensive mode: monitoring, anomaly detection, OPSEC only.",
    "stealth": "Stealth mode: minimal footprint, logs disabled, beacon only."
}

def switch_mode(mode):
    mode = mode.lower()
    if mode in MODES:
        log_event(f"Switched to {mode.upper()} - {MODES[mode]}")
        print(f"[MODE] Switched to {mode.upper()} - {MODES[mode]}")
        # Here you can trigger actual mode changes in agents (stub/demo)
        return mode
    else:
        print(f"[ERROR] Unknown mode: {mode}")
        print("Available modes:", ", ".join(MODES.keys()))
        return None

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        switch_mode(sys.argv[1])
    else:
        print("Usage: python mode_switch.py <red|blue|stealth>")