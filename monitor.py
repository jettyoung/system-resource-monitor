import psutil
import time
from collections import deque
import matplotlib.pyplot as plt

class SystemMonitor:
    def __init__(self, history_size=60):
        self.cpu_history = deque(maxlen=history_size)
        self.memory_history = deque(maxlen=history_size)
        self.disk_history = deque(maxlen=history_size)
        self.alert_threshold = {'cpu': 80, 'memory': 80, 'disk': 90}

    def get_current_stats(self):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        return {'cpu': cpu, 'memory': memory, 'disk': disk}

    def update_history(self):
        stats = self.get_current_stats()
        self.cpu_history.append(stats['cpu'])
        self.memory_history.append(stats['memory'])
        self.disk_history.append(stats['disk'])
        return stats

    def check_alerts(self, stats):
        alerts = []
        for key, value in stats.items():
            if value > self.alert_threshold[key]:
                alerts.append(f"⚠️ High {key.upper()} usage: {value}%")
        return alerts

    def generate_report(self):
        if not self.cpu_history:
            return "No data yet bro"
        avg_cpu = sum(self.cpu_history) / len(self.cpu_history)
        avg_mem = sum(self.memory_history) / len(self.memory_history)
        avg_disk = sum(self.disk_history) / len(self.disk_history)
        return f"Avg CPU: {avg_cpu:.1f}% | Mem: {avg_mem:.1f}% | Disk: {avg_disk:.1f}%"

    def plot_history(self, output_file='system_plot.png'):
        if not self.cpu_history:
            return "No data to plot yet"
        times = list(range(len(self.cpu_history)))
        plt.figure(figsize=(10, 6))
        plt.plot(times, self.cpu_history, label='CPU', color='red')
        plt.plot(times, self.memory_history, label='Memory', color='blue')
        plt.plot(times, self.disk_history, label='Disk', color='green')
        plt.xlabel('Time (samples)')
        plt.ylabel('Usage %')
        plt.title('System Resource Usage')
        plt.legend()
        plt.grid(True)
        plt.savefig(output_file)
        plt.close()
        return f"Plot saved as {output_file} 📈"