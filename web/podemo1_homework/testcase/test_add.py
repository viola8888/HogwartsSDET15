import random
import time

from web.podemo1_homework.page.main import MainPage


class TestAdd:
    def setup(self):
        self.main = MainPage()
        x = str(random.randint(1, 1000))
        y = str(random.randint(100, 999))
        username = 'aaaaaa' + x
        acctid = 'aaaaaa__hogwarts' + x
        phonenum = '13500000' + y

    def test_addmember(self):
        x = str(random.randint(1, 1000))
        y = str(random.randint(100, 999))
        username = 'aaaaaa' + x
        acctid = 'aaaaaa__hogwarts' + x
        phonenum = '13500000' + y

        addmember = self.main.goto_addmenber()
        addmember.add_member(username, acctid, phonenum)
        assert addmember.get_member(username)

    def test_contact_addmember(self):
        x = str(random.randint(1, 1000))
        y = str(random.randint(100, 999))
        username = '霍格沃兹' + x
        acctid = 'bbbbbb__hogwarts' + x
        phonenum = '13600000' + y

        addmember = self.main.goto_contects()
        addmember.add_member(username, acctid, phonenum)
        time.sleep(5)
        assert addmember.get_member(username)
