# 🧠 CrossComPJxAI

> *“A PhantomNet Initiative — Command the unseen. Orchestrate the unknown.”*  
> Modular, AI-augmented Red Team suite engineered by **Professor Johnny (PJxAI)**

![Red Team Ops](https://img.shields.io/badge/Red%20Ops-Active-red)
![AI-Driven](https://img.shields.io/badge/AI%20Modules-Enabled-blue)
![Cross-Platform](https://img.shields.io/badge/Cross--Platform-Windows%20%7C%20Linux%20%7C%20Android-green)
![Built By](https://img.shields.io/badge/Built%20By-1man--army%20x%20PJxAI-black)

---

## 🧩 Overview

**CrossComPJxAI** is a cross-platform, modular red team and operator automation suite with AI-powered decisions and covert communication protocols.

🔒 Focus: **Stealth ops, field agents, recon coordination, and AI logic modules**

📡 Stack: Python · SocketIO · Modular C2 · VoiceOps · HUD overlay

---

## ⚙️ Features

| Category        | Description |
|----------------|-------------|
| 👥 **Agents** | Stealth agents for Windows, Linux, Android, iOS |
| 🧠 **AI Core** | Task suggestion, intel linking, OPSEC heuristics |
| 🎛️ **Dashboard** | Operator HUD, notes console, voice routing |
| 🛰️ **Beacon System** | Passive check-ins, task callbacks, encrypted payloads |
| 🧬 **Persistence** | Simulated startup, cron, and service disguises |
| 🧹 **OPSEC Tools** | In-memory ops, log wiping, stealth mode |
| 🔧 **Lateral Modules** | Pass-the-hash, Kerberos probes, local discovery |

---

## 📁 Directory Structure

```

CrossComPJxAI/
├── agents/                 # Field agents: win, linux, droid
├── operator/               # Operator-side tools
│   ├── dashboard/
│   ├── tools/
├── core/                   # Core functions: recon, lateral, opsec
│   ├── ai/
│   ├── recon/
│   ├── lateral/
│   └── opsec/
├── quantum\_mission\_x.py    # Orchestration script
├── reconbot\_skynet.py      # Passive recon scanner
├── README.md
└── requirements.txt

````

---

## 🚀 Usage

### 1. Setup & Install

```bash
git clone https://github.com/1man-army/CrossComPJxAI.git
cd CrossComPJxAI
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
````

---

### 2. Agent Deployment

Edit C2 URLs inside:

* `agents/windows/win_agent.py`
* `agents/linux/linux_agent.py`
* `agents/android/droid_agent.py`

Then deploy to your targets (sandbox/lab only 🔒).

---

### 3. Operator Tools

```bash
python operator/dashboard/main_dashboard.py
```

Use supporting tools:

```bash
python operator/tools/note_console.py
python operator/tools/voice_router.py
```

---

### 4. Recon & Lateral Movement

```bash
python core/recon/dns_profiler.py
python core/lateral/pass_the_hash.py
```

AI Command Center:

```bash
python core/ai/ai_task_suggest.py
```

---

## ⚠️ Legal Disclaimer

> **This project is for authorized red team simulation, training, and educational research only.
> Deploy only in labs or controlled environments. Unauthorized use is strictly prohibited.**

---

🧠 *Developed by* [1man-army](https://github.com/1man-army) × *Professor Johnny (PJxAI)*
🎭 *We walk in shadows so others may learn in light.*