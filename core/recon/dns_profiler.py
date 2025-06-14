"""
DNS Profiler - CrossComPJxAI
Performs DNS lookups and profiling for a given domain.
"""
import socket

def dns_profile(domain):
    try:
        ip = socket.gethostbyname(domain)
        return {
            "A": ip,
            "PTR": socket.gethostbyaddr(ip)[0] if ip else None
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print(dns_profile("example.com"))