import psutil
import time

# def monitor_processes(alert_queue):
#     while True:
#         for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
#             # Skip System Idle Process (Windows) and invalid PIDs
#             if proc.info['name'] == "System Idle Process" or proc.info['pid'] == 0:
#                 continue
#             if proc.info['cpu_percent'] > 70:
#                 alert = f"High CPU: {proc.info['name']} (PID: {proc.info['pid']})"
#                 print(alert)
#                 alert_queue.put(alert)  # Send alert to GUI
#         time.sleep(2)


def monitor_processes(alert_queue):
    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            if proc.info['name'] == "System Idle Process" or proc.info['pid'] == 0:
                continue
            if proc.info['cpu_percent'] > 70:
                alert_data = {
                    "type": "process",
                    "message": f"High CPU: {proc.info['name']} (PID: {proc.info['pid']})",
                    "pid": proc.info['pid'],
                    "name": proc.info['name']
                }
                alert_queue.put(alert_data)
        time.sleep(2)