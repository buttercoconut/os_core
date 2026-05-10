# device_driver_a.py
class DeviceDriverA:
    def __init__(self):
        self.status = "idle"

    def start(self):
        self.status = "running"

    def stop(self):
        self.status = "stopped"
