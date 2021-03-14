from service_addbook_weixin.base_api import BaseBookApi


class BookApi(BaseBookApi):
    def __init__(self):
        super().__init__()

    def add_book(self, userid, name, mobile):
        data = {
            "method":"post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token": self.token},
            "json":{
                    "userid": userid,
                    "name": name,
                    "mobile": mobile,
                    "department": [1],       # 成员所属部门id列表,不超过100个
                }}
        r = self.sent(data)
        return r


    def get_userid(self,phone):
        data = {
            "method":"post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/getuserid",
            "params": {"access_token":self.token},
            "json":{"mobile": phone}
        }
        r = self.sent(data)
        print(r)
        return r.json()["userid"]

    def del_book(self, userid):
        data = {
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params":{"access_token": self.token, "userid":userid}
        }
        r = self.sent(data)
        return r

    def get_book_members(self, userid):
        data = {
            "method":"get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {"access_token": self.token, "userid":userid}
        }
        r = self.sent(data)
        return r

    def updata_member_name(self, userid, name):
        data ={
            "method":'post',
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params":{"access_token": self.token},
            "json":{
                "userid":userid,
                "name": name
            }
        }
        r = self.sent(data)
        return r
