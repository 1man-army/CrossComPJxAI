"""
reconbot_skynet.py – Cross-platform passive reconnaissance + AI-assisted intel linker
Author: Red Team AI Assistant | Year: 2025 PJxAI 2.0
"""
import os, socket, platform, subprocess, json, threading, time, base64, random
from datetime import datetime

def get_os_info():
    return {
        "platform": platform.system(),
        "version": platform.version(),
        "release": platform.release(),
        "arch": platform.machine()
    }

def get_hostname_ip():
    return {
        "hostname": socket.gethostname(),
        "local_ip": socket.gethostbyname(socket.gethostname())
    }

def get_net_connections():
    try:
        output = subprocess.check_output("netstat -ano", shell=True, text=True)
        return output.splitlines()[:10]
    except:
        return ["[!] Failed to fetch netstat."]

def obfuscate(data):
    return base64.b64encode(json.dumps(data).encode()).decode()

def recon_report():
    print("\n[ Skynet ReconBot Report 🚨 | AI+Stealth Mode ]\n")
    report = {"timestamp": datetime.utcnow().isoformat()}
    threads = []

    def t_os(): report["os_info"] = get_os_info()
    def t_host(): report["host_info"] = get_hostname_ip()
    def t_net(): report["netstat_sample"] = get_net_connections()

    for func in [t_os, t_host, t_net]:
        t = threading.Thread(target=lambda: [time.sleep(random.uniform(0.5, 2.5)), func()])
        t.start()
        threads.append(t)
    for t in threads: t.join()

    obf = obfuscate(report)
    print(f"[OBFUSCATED REPORT]\n{obf}\n")
    print("[DECODED REPORT]\n", json.dumps(report, indent=4))

if __name__ == "__main__":
    recon_report()