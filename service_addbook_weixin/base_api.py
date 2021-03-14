import requests



class BaseBookApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = "ww9251b89bc79d8a7d"
        corpsecret = "1COtM7ePLGcc7sWxX4yQf4Hma4kBcTxyR5D42yoOcsE"
        data = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid":corpid,"corpsecret":corpsecret}
        }
        r = self.sent(data)
        token = r.json()['access_token']
        return token

    def sent(self, kwargs):
        r = requests.request(**kwargs)
        return r


