import pytest

from context import Context

class TestMain:
    context = Context()
    context.load("./tmp.yaml")

    @pytest.mark.parametrize("testcase", context.store.testcase.values(), ids=context.store.testcase.keys())
    def test_main(self, testcase):
        self.context.run_steps_by_testcase(testcase)