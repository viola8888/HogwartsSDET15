import time
import random

from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = 'aaaaaag'
        account = 'aaaaag__hogwarts'
        phonenum = '13200000006'

        addmember = self.main.goto_addmenber()
        addmember.add_member(username, account, phonenum)
        time.sleep(5)
        assert username in addmember.get_member()

    def test_contact_addmember(self):
        x = str(random.randint(1, 1000))
        y = str(random.randint(100, 999))
        username = '霍格沃兹' + x
        account = 'bbbbb__hogwarts' + x
        phonenum = '13200000' + y

        addmember = self.main.goto_contacts()
        addmember.add_member(username, account, phonenum)

        time.sleep(5)
        # assert username in addmember.get_member()
        assert addmember.get_member(username)
