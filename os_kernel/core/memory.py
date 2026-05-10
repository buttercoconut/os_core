# memory.py
from .process import PCB

class MemoryManager:
    def __init__(self, total: int = 1024):
        self.total = total
        self.used = 0
        self.allocations = {}

    def allocate(self, pcb: PCB, size: int):
        if self.used + size > self.total:
            raise MemoryError("Out of memory")
        self.allocations[pcb.pid] = size
        self.used += size

    def free(self, pcb: PCB):
        size = self.allocations.pop(pcb.pid, 0)
        self.used -= size
