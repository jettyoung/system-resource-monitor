# System Resource & Log Monitor
Python tool that monitors CPU, memory, and disk usage in real-time and analyzes log files for errors and anomalies.

## Features
- Live system monitoring with alerts for high usage
- Log parsing with regex to detect ERROR/CRITICAL entries
- Anomaly detection (too many errors in short time)
- Generates usage graphs with matplotlib

## Tech Stack
- Python
- psutil (system stats)
- matplotlib (visualization)
- regex for log parsing

## How to Run
```bash
pip install psutil matplotlib
python main.py
