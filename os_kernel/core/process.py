# process.py
from dataclasses import dataclass, field
from typing import List, Optional
import time

@dataclass
class PCB:
    pid: int
    priority: int
    state: str = "READY"
    cpu_time: float = 0.0
    created_at: float = field(default_factory=time.time)

class Scheduler:
    def __init__(self, quantum: float = 0.1):
        self.quantum = quantum
        self.ready_queue: List[PCB] = []
        self.current: Optional[PCB] = None
        self.time_slice = 0.0

    def add_process(self, pcb: PCB):
        self.ready_queue.append(pcb)

    def schedule(self):
        if not self.ready_queue:
            self.current = None
            return
        # Round Robin
        self.current = self.ready_queue.pop(0)
        self.time_slice = self.quantum
        self.current.state = "RUNNING"

    def tick(self, dt: float):
        if self.current:
            self.current.cpu_time += dt
            self.time_slice -= dt
            if self.time_slice <= 0:
                self.current.state = "READY"
                self.ready_queue.append(self.current)
                self.schedule()

# memory.py
class MemoryManager:
    def __init__(self, total: int = 1024):
        self.total = total
        self.used = 0
        self.allocations = {}

    def allocate(self, pid: int, size: int):
        if self.used + size > self.total:
            raise MemoryError("Out of memory")
        self.allocations[pid] = size
        self.used += size

    def free(self, pid: int):
        size = self.allocations.pop(pid, 0)
        self.used -= size

# file_system.py
class FileSystem:
    def __init__(self):
        self.files = {}

    def create(self, name: str, content: str = ""):
        self.files[name] = content

    def read(self, name: str) -> str:
        return self.files.get(name, "")

    def write(self, name: str, content: str):
        if name in self.files:
            self.files[name] = content

    def delete(self, name: str):
        self.files.pop(name, None)

# interrupt.py
class InterruptHandler:
    def __init__(self):
        self.handlers = {}

    def register(self, irq: int, handler):
        self.handlers[irq] = handler

    def trigger(self, irq: int, *args, **kwargs):
        if irq in self.handlers:
            return self.handlers[irq](*args, **kwargs)
        raise ValueError("Unhandled IRQ")

# device_driver_a.py
class DeviceDriverA:
    def __init__(self):
        self.status = "idle"

    def start(self):
        self.status = "running"

    def stop(self):
        self.status = "stopped"

# device_driver_b.py
class DeviceDriverB:
    def __init__(self):
        self.status = "idle"

    def start(self):
        self.status = "running"

    def stop(self):
        self.status = "stopped"

# os_types.h
# Placeholder for C type definitions

# os_constants.h
# Placeholder for OS constants
