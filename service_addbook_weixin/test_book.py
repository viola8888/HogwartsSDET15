from time import sleep

import pytest
import yaml

from service_addbook_weixin.book_api import BookApi


def get_yaml():
    with open("add_members.yaml", 'r', encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data["add_data"], data["ids"]


class TestBook:

    def setup_class(self):
        self.book = BookApi()

    @pytest.mark.parametrize("userid, name, mobile", get_yaml()[0], ids=get_yaml()[1])
    def test_add(self, userid, name, mobile):
        r = self.book.add_book(userid, name, mobile)
        sleep(5)
        assert r.json()["errcode"] == 0

    def test_del(self):
        userid = self.book.get_userid("13100000002")
        r = self.book.del_book(userid)
        assert r.json()['errcode'] == 0

    def test_get_member(self):
        userid = self.book.get_userid("13100000003")
        r = self.book.get_book_members(userid)
        assert r.json()['errcode'] == 0
        assert r.json()["userid"] == userid

    @pytest.mark.parametrize("updata_name, phone",[
        ["xiaohong_000","13000000000"],
        ["xiaohong_001", "13000000001"],
        ["xiaohong_002", "13000000002"]
    ], ids=["修改成功","换个数据再来一次", "就是看看"])
    def test_update_name(self, updata_name, phone):
        userid = self.book.get_userid(phone)
        r = self.book.updata_member_name(userid, updata_name)
        r = self.book.get_book_members(userid)
        assert r.json()["name"] == updata_name
