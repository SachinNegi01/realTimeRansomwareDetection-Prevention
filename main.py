from core.file_monitor import start_monitoring
from core.process_analyzer import monitor_processes
from gui.dashboard import AlertGUI
import threading

# Initialize GUI
gui = AlertGUI()

# Start file monitoring with GUI's alert queue
threading.Thread(
    target=start_monitoring,
    args=(gui.alert_queue, "."),
    daemon=True
).start()

# Start process monitoring with GUI's alert queue
threading.Thread(
    target=monitor_processes,
    args=(gui.alert_queue,),
    daemon=True
).start()

# Run the GUI
gui.start()