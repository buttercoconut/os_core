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
