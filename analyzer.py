import re
from datetime import datetime

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logs = []
        self.load_logs()

    def load_logs(self):
        try:
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
                print(f"Found {len(lines)} lines in log file")
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s*\[(\w+)\]\s*(.*)', line)
                    if match:
                        time_str, level, msg = match.groups()
                        try:
                            dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
                            self.logs.append({'time': dt, 'level': level.upper(), 'msg': msg})
                            print(f"Parsed: {level} - {msg}")
                        except ValueError:
                            print(f"Bad date: {time_str}")
                    else:
                        print(f"Skipped line (no match): {line}")
            print(f"Total parsed logs: {len(self.logs)}")
        except FileNotFoundError:
            print("sample.log not found")

    def analyze_errors(self):
        errors = [log for log in self.logs if log['level'] in ['ERROR', 'CRITICAL']]
        return sorted(errors, key=lambda x: x['time'])

    def detect_anomalies(self):
        recent = self.logs[-10:]
        error_count = sum(1 for log in recent if log['level'] in ['ERROR', 'CRITICAL'])
        if error_count > 3:
            return "🚨 ANOMALY: Too many errors in recent logs!"
        return "All good, no anomalies"