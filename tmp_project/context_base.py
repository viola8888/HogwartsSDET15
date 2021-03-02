class ContextBase:
    _context = None

    def get_context(self):
        return self._context

    def set_context(self, context):
        self._context = context