import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = "ww9251b89bc79d8a7d"
        corpsecret = "Y-RBYO3uBdjcmavA0PUhi35Qu80zSbk3cRxSVWXMIJo"
        data ={
            "method": 'get',
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        r = self.send(data)
        # 获取token
        # r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        #                  params={"corpid": corpid, "corpsecret": corpsecret})
        # print(json.dumps(r.json(), indent=2))
        # assert r.status_code == 200
        # assert r.json()['errcode'] == 0
        token = r.json()["access_token"]
        return token


    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r