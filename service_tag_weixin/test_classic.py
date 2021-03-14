import datetime
import json

import requests


def test_tag_list():
    corpid = "ww9251b89bc79d8a7d"
    corpsecret = "Y-RBYO3uBdjcmavA0PUhi35Qu80zSbk3cRxSVWXMIJo"
    # 获取token
    r =  requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                 params={"corpid": corpid, "corpsecret": corpsecret})
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    token = r.json()["access_token"]
    print(token)

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={"tag_id": [], "group_id": []},
    )
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    new_name =  "new_name" + str(datetime.datetime.now().strftime("%Y%m%D%H%M"))

    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
        params = {"access_token":token},
        json = {
            "id": "etf3yRDwAAaLnHR6ImFvpeU_NbKKcPoA",
            "name": new_name,
        }
    )
    print("*" * 50)
    print(json.dumps(r.json(), indent=2))
    print("*" * 50)
    assert r.status_code == 200
    assert r.json()['errcode'] == 0


    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={"tag_id": [], "group_id": []},
    )

    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == 'python15'
        for tag in group['tag'] if tag['name'] == new_name
        ]

    assert tags != []
