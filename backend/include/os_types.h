"""OS type definitions."""

# Example types
class Process:
    def __init__(self, pid: int, name: str, state: str):
        self.pid = pid
        self.name = name
        self.state = state

    def dict(self):
        return {"pid": self.pid, "name": self.name, "state": self.state}
