import tkinter as tk
import queue

# class AlertGUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("GuardianOS")
#         self.root.geometry("300x100")
#         self.label = tk.Label(self.root, text="System Secure", fg="green", font=("Arial", 14))
#         self.label.pack(pady=20)
#         self.alert_queue = queue.Queue()
#         self.root.after(100, self.check_alerts)  # Start checking for alerts

#     def check_alerts(self):
#         try:
#             alert = self.alert_queue.get_nowait()
#             self.label.config(text=alert, fg="red")
#         except queue.Empty:
#             pass
#         self.root.after(100, self.check_alerts)  # Repeat every 100ms

#     def start(self):
#         self.root.mainloop()


import tkinter as tk
from tkinter import ttk
import queue

class AlertGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GuardianOS")
        self.root.geometry("400x150")
        
        # Alert display
        self.label = tk.Label(self.root, text="System Secure", fg="green", font=("Arial", 14))
        self.label.pack(pady=10)
        
        # Action buttons (hidden initially)
        self.button_frame = ttk.Frame(self.root)
        self.kill_btn = ttk.Button(self.button_frame, text="Kill Process", command=self.kill_process)
        self.ignore_btn = ttk.Button(self.button_frame, text="Ignore", command=self.clear_alert)
        
        # Alert data storage
        self.alert_queue = queue.Queue()
        self.current_pid = None
        self.root.after(100, self.check_alerts)

    def check_alerts(self):
        try:
            alert_data = self.alert_queue.get_nowait()
            self.current_pid = alert_data.get("pid")
            
            # Update GUI
            self.label.config(text=alert_data["message"], fg="red")
            if alert_data["type"] == "process":
                self.kill_btn.pack(side="left", padx=10)
                self.ignore_btn.pack(side="left")
                self.button_frame.pack()
            else:
                self.button_frame.pack_forget()
                
        except queue.Empty:
            pass
        self.root.after(100, self.check_alerts)

    def kill_process(self):
        from core.quarantine import kill_process  # Import here to avoid circular dependency
        if self.current_pid:
            kill_process(self.current_pid)
            self.clear_alert()

    def clear_alert(self):
        self.label.config(text="System Secure", fg="green")
        self.button_frame.pack_forget()
        self.current_pid = None

    def start(self):
        self.root.mainloop()
