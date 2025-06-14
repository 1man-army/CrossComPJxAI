"""
recon_ai.py – CrossComPJxAI
AI-assisted Reconnaissance Module: Passive network, host, and service discovery.
"""

import socket
import platform
import json
from datetime import datetime

def passive_recon():
    info = {
        "timestamp": datetime.now().isoformat(),
        "platform": platform.system(),
        "hostname": socket.gethostname(),
        "local_ip": get_local_ip(),
        "open_ports": scan_ports(["22", "80", "443", "445", "3389"])
    }
    return info

def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return "unknown"

def scan_ports(port_list):
    results = {}
    for port in port_list:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((get_local_ip(), int(port)))
            results[port] = "open" if result == 0 else "closed"
            s.close()
        except Exception:
            results[port] = "error"
    return results

if __name__ == "__main__":
    recon_data = passive_recon()
    print(json.dumps(recon_data, indent=2))