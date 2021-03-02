from context_base import ContextBase

class TextCase(ContextBase):
    def __init__(self, steps, context):
        self.steps = steps
        self._context = context

    def run_steps(self):
        self.get_context().run_steps(self.steps)