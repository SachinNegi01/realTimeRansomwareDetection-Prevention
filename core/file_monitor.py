import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, alert_queue):
        self.alert_queue = alert_queue
        self.file_count = 0
        self.start_time = time.time()

    def on_modified(self, event):
        self.file_count += 1
        elapsed = time.time() - self.start_time
        if elapsed >= 2:
            if self.file_count > 100:
                self.alert_queue.put("ALERT: Rapid file changes detected!")
            self.file_count = 0
            self.start_time = time.time()
            if self.file_count > 100:
                self.alert_queue.put({
                    "type": "file",
                    "message": "ALERT: Rapid file changes detected!"
                })

def start_monitoring(alert_queue, path="."):
    observer = Observer()
    observer.schedule(FileChangeHandler(alert_queue), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

