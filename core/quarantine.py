import os
import signal

def kill_process(pid):
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"Terminated PID: {pid}")
    except ProcessLookupError:
        print("Process not found!")