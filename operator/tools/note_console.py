"""
Note Console - CrossComPJxAI
Operator-agent live chat and mission notes.
"""
import datetime
from config import C2_URL, OPERATOR_ID

def add_note(note, author="operator"):
    ts = datetime.datetime.now().isoformat()
    with open("mission_notes.txt", "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {author}: {note}\n")

def show_notes():
    try:
        with open("mission_notes.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("No notes yet.")

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {msg}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        add_note(" ".join(sys.argv[1:]))
    else:
        show_notes()