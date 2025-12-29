from monitor import SystemMonitor
from analyzer import LogAnalyzer
import time

def main():
    monitor = SystemMonitor()
    analyzer = LogAnalyzer('sample.log')  #reads sample.log
    
    print("System & Log Monitor running - press Ctrl+C to stop monitoring")

    while True:
        print("\n" + "="*40)
        print("1. Live Monitor (resources + alerts)")
        print("2. Check Logs for Errors")
        print("3. Quick Report")
        print("4. Make Plot Graph")
        print("5. Exit")
        choice = input("\nPick one: ").strip()

        if choice == '1':
            print("\nMonitoring live... (Ctrl+C to stop)")
            try:
                while True:
                    stats = monitor.update_history()
                    alerts = monitor.check_alerts(stats)
                    print(f"CPU: {stats['cpu']}% | Mem: {stats['memory']}% | Disk: {stats['disk']}%")
                    if alerts:
                        for a in alerts:
                            print(a)
                    time.sleep(5)
            except KeyboardInterrupt:
                print("\nStopped monitoring")

        elif choice == '2':
            print("\nRecent errors:")
            errors = analyzer.analyze_errors()
            if errors:
                for err in errors[-5:]:
                    print(f"{err['time']} [{err['level']}] {err['msg']}")
            else:
                print("No errors found")
            print(analyzer.detect_anomalies())

        elif choice == '3':
            print("\n" + monitor.generate_report())

        elif choice == '4':
            print("\n" + monitor.plot_history())
            print("Check your folder for system_plot.png")

        elif choice == '5':
            print("Goodbye")
            break

        else:
            print("Choose one of the listed options")

if __name__ == "__main__":
    main()