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
