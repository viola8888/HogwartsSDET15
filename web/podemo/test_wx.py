from web.podemo.index_page import IndexPage


class TestWX:
    def setup(self):
        self.index = IndexPage()

    def teardown(self):
        pass

    def test_register(self):
        # assert self.index.goto_login().goto_register().register_success()
        assert self.index.goto_register().register_success()
