# device_driver_b.py
class DeviceDriverB:
    def __init__(self):
        self.status = "idle"

    def start(self):
        self.status = "running"

    def stop(self):
        self.status = "stopped"
