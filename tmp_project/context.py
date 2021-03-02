class Context:
    def __init__(self):
        self.store = TestCaseStore()
        self.testcase = None
        self._return_value = None


    def load(self, file_name):
        self.store.load(file_name)

    def run_steps_by_testcase(self, steps):
        self.testcase = TestCase(steps, self)
        self.testcase.run_steps()

    def run_steps(self, steps):
        for step in steps:
            step.set_context(self)
            self._return_value = step.run()

    def return_value(self):
        return self._return_value