import datetime
import json

import requests

from service_tag_weixin.base_api import BaseApi


class Tag(BaseApi):
    # token = None

    def __init__(self):
        super().__init__()

    # def get_token(self):
    #     corpid = "ww9251b89bc79d8a7d"
    #     corpsecret = "Y-RBYO3uBdjcmavA0PUhi35Qu80zSbk3cRxSVWXMIJo"
    #     # 获取token
    #     r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
    #                      params={"corpid": corpid, "corpsecret": corpsecret})
    #     print(json.dumps(r.json(), indent=2))
    #     assert r.status_code == 200
    #     assert r.json()['errcode'] == 0
    #     token = r.json()["access_token"]
    #     return token

    def find_group_id_by_name(self, group_name):
        # 查询元素是否不存在，如果不存在，报错
        for group in self.list().json()["tag_group"]:
            if group_name in group["group_name"]:
                return group['group_id']
        print("group name not in group")
        # todo：如果 group_id 是 “”， 也会类似false
        # return ValueError("group name not in group")
        return ""

    def is_group_id_exist(self, group_id):
        # 查询元素是否不存在，如果不存在，报错
        for group in self.list().json()["tag_group"]:
            if group_id in group["group_id"]:
                return True
        # return ValueError("group id not in group")
        return False

    def add(self, group_name, tag, **kwargs):
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        #     params={"access_token": self.token},
        #     json={"group_name": group_name, "tag": tag, **kwargs}
        # )
        # print(json.dumps(r.json(), indent=2))
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.token},
            "json": {"group_name": group_name, "tag": tag, **kwargs}
        }
        r = self.send(data)
        return r

    def add_and_detect(self, group_name, tag, **kwargs):
        r = self.add(group_name, tag, **kwargs)
        # 如果删除的元素已经存在
        if r.json()["errcode"] == 40071:
            group_id = self.find_group_id_by_name(group_name)
            if not group_id:
                return ""
            self.delete_group(group_id)
            self.add(group_name, tag, **kwargs)
        result = self.find_group_id_by_name(group_name)
        if not result:
            print("add not success")
        return result

    def list(self):
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        #     params={"access_token": self.token},
        #     json={"tag_id": [], "group_id": []},
        # )
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            "params": {"access_token": self.token},
            "json": {"tag_id": [], "group_id": []},
        }
        r = self.send(data)
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def update(self, id, new_name):
        # r = requests.post(
        #     "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
        #     params={"access_token": self.token},
        #     json={
        #         "id": id,
        #         "name": name,
        #     }
        # )
        data = {
            "method":"post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {"access_token": self.token},
            "json": {"id": id, "name": new_name, }
        }
        r = self.send(data)
        # print(json.dumps(r.json(), indent=2))
        return r

    # 查询 tag_id  ——>  删除tag_id
    # 如果正常：成功
    # 如果异常：失败
    def delete_group(self, goup):
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
        #                   params={"access_token": self.token},
        #                   json={
        #                       "group_id": goup
        #                   }
        #                   )
        # print(json.dumps(r.json(), indent=2))
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "parmas":{"access_token": self.token},
            "json":{"group_id": goup}

        }
        r = self.send(data)
        return r

    def delete_tag(self, tag):
        # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
        #                   params={"access_token": self.token},
        #                   json={
        #                       "tag_id": tag
        #                   }
        #                   )
        # print(json.dumps(r.json(), indent=2))
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {"tag_id": tag}
        }
        r = self.send(data)
        return r

    def delete_and_detect_group(self, group_ids):
        delete_group_ids = []
        r = self.delete_group(group_ids)
        if r.json()['errcode'] == 40068:
            # 如果标签不存在，就添加一个标签，将它的 group_id 存储起来
            for group_id in group_ids:
                if not self.is_group_id_exist(group_id):
                    group_id_tmp = self.add_and_detect("TMP000000", [{"name": "TAG12"}])
                    delete_group_ids.append(group_id_tmp)
                #     如果标签存在，就将它存入标签组
                else:
                    delete_group_ids.append(group_id)

            r = self.delete_group(delete_group_ids)
        return r
