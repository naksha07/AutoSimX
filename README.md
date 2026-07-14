# 🚗 AutoSimX – Automotive ECU Simulator

> A Python-based Automotive ECU Simulator featuring a Virtual CAN Bus, Multi-ECU Communication, Digital Dashboard, CAN Analyzer, DTC Management, Fault Injection, CAN Log Replay, and a lightweight AUTOSAR Runtime Environment.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![PySide6](https://img.shields.io/badge/PySide6-GUI-green)
![CAN](https://img.shields.io/badge/Protocol-CAN-orange)
![AUTOSAR](https://img.shields.io/badge/AUTOSAR-RTE-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Project Overview

AutoSimX is a software-based simulation platform that mimics communication between multiple automotive Electronic Control Units (ECUs) using a Virtual CAN Bus.

The simulator demonstrates how ECUs exchange CAN messages, update vehicle status, generate diagnostic information, monitor ECU health, and communicate through an AUTOSAR-inspired Runtime Environment (RTE).

The project is designed for learning Automotive Embedded Systems, CAN Communication, AUTOSAR concepts, and ECU software development.

---

# ✨ Features

- Virtual CAN Bus Simulation
- Multi-ECU Communication
- Engine ECU
- Instrument Cluster ECU
- Body ECU
- Gateway ECU
- Digital Dashboard (PySide6)
- Live CAN Analyzer
- ECU Health Monitoring
- Diagnostic Trouble Codes (DTC)
- Fault Injection
- CAN Message Logger
- CSV Log Export
- CAN Replay Mode
- AUTOSAR Runtime Environment (RTE)
- Software Components (SWCs)

---

# 🏗 System Architecture

```

Application Software Components
│
▼
AUTOSAR Runtime Environment (RTE)
│
▼
ECUs
├── Engine ECU
├── Cluster ECU
├── Body ECU
└── Gateway ECU
│
▼
Virtual CAN Bus
│
▼
Dashboard + Logger + Replay

```

---

# 📁 Project Structure

```

AUTOSIMX/
│
├── autosar/
│   ├── rte.py
│   ├── software_component.py
│   ├── engine_component.py
│   └── cluster_component.py
│
├── communication/
│   ├── can_bus.py
│   ├── can_frame.py
│   └── message_ids.py
│
├── ecu/
│   ├── ecu.py
│   ├── engine_ecu.py
│   ├── cluster_ecu.py
│   ├── body_ecu.py
│   └── gateway_ecu.py
│
├── gui/
│   └── dashboard.py
│
├── logger/
│   ├── can_logger.py
│   └── csv_logger.py
│
├── replay/
│   └── can_replay.py
│
├── scheduler/
│   └── task_scheduler.py
│
├── models/
│
├── logs/
│
├── docs/
│
├── main.py
├── run_dashboard.py
└── run_replay.py

```

---

# ⚙ Technologies Used

- Python
- PySide6
- Object-Oriented Programming
- CAN Protocol
- Automotive ECU Concepts
- AUTOSAR Runtime Environment
- CSV Logging
- Multithreading

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AUTOSIMX.git

cd AUTOSIMX
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install PySide6
```

---

# ▶ Running the Simulator

Console Mode

```bash
python main.py
```

Dashboard

```bash
python run_dashboard.py
```

Replay Recorded CAN Logs

```bash
python run_replay.py
```

---

# 🖥 Dashboard Features

- Live Vehicle Speed
- RPM
- Fuel Level
- Headlights
- Door Lock Status
- ECU Health Monitor
- Live CAN Monitor
- DTC Viewer

---

# 📡 CAN Message Flow

```

Engine ECU
│
▼
Virtual CAN Bus
│
├────────► Cluster ECU
│
├────────► Body ECU
│
└────────► Gateway ECU

```

---

# 🔄 Replay Mode

The simulator records every CAN frame into

```

logs/can_log.csv

```

Replay the recorded communication using

```bash
python run_replay.py
```

---

# 🚨 Fault Injection

Supports simulation of

- Engine Failure
- CAN Message Loss
- ECU Offline
- Communication Faults

---

# 🔧 Diagnostic Trouble Codes (DTC)

Example DTCs

| Code | Description |
|------|-------------|
| P0100 | Mass Air Flow Sensor Fault |
| P0200 | Fuel Injector Circuit |
| U0100 | Lost Communication With ECU |

---

# 🚘 AUTOSAR Runtime Environment

The project includes a lightweight AUTOSAR-inspired Runtime Environment (RTE) allowing Software Components (SWCs) to communicate independently of ECU implementation.

Implemented Components

- Engine Software Component
- Cluster Software Component
- Runtime Environment

---

# 📷 Screenshots

Add screenshots inside

```

docs/

```

Example

```

docs/
dashboard.png
can_monitor.png
ecu_health.png
dtc.png
replay.png

```

---

# 📈 Future Improvements

- CAN FD Support
- LIN Bus Simulation
- UDS Diagnostics
- ISO-TP Transport Layer
- OBD-II Scanner
- ECU Firmware Update Simulation
- Secure CAN Authentication
- Automotive Ethernet Support

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

Nakshathraa N B

B.E. Electronics and Communication Engineering

Specialization:
- Automotive Software
- Embedded Systems
- CAN Communication
- AUTOSAR
- Python Development

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.