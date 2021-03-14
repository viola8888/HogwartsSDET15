import datetime
import json

import pytest
import requests
from jsonpath import jsonpath

from service_tag_weixin.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize("tag_id, new_name", [
        ['etf3yRDwAAaLnHR6ImFvpeU_NbKKcPoA', "tag1_viola_new_"],
        ['etf3yRDwAAaLnHR6ImFvpeU_NbKKcPoA', "tag2_viola_中文_"],
        ['etf3yRDwAAaLnHR6ImFvpeU_NbKKcPoA', "tag3_viola_[中文]_"]
    ])
    def test_tag_list(self, tag_id, new_name):
        tag_id = tag_id
        new_name = new_name + str(datetime.datetime.now().strftime("%Y%m%D%H%M"))

        r = self.tag.list()
        r = self.tag.update(id=tag_id, new_name=new_name)
        r = self.tag.list()

        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group['tag'] if tag['name'] == new_name
        #     ]
        # assert tags != []

        # print(r.json(), f"$..[?(@.name=='{new_name}')]")
        print("*" * 50)
        a = jsonpath(r.json(), f"$..[?(@.name=='{new_name}')]")[0]['name']
        print(a)
        print("*" * 50)

        # assert jsonpath(r.json(), f"$..[?(@.name=='{new_name}')]")[0]['name'] == new_name

    def test_tag_list_fail(self):
        pass

    def test_add_tag(self):
        group_name = "TMP0012345"
        tag = [
                  {"name": "TAG13"},
                  {"name": "TAG23"},
                  {"name": "TAG33"},
              ]

        r = self.tag.add(group_name=group_name, tag=tag)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_add_before_detect(self):
        group_name = "TMP001234"
        tag = [
            {"name": "TAG12"},
            {"name": "TAG22"},
            {"name": "TAG32"},
        ]
        r = self.tag.add_and_detect(group_name,tag)
        assert r

    def test_list(self):
        self.tag.list()

    def test_delete_group(self):
        self.tag.delete_group(["etf3yRDwAAn0BkPzjft8ACQ4Q2eGPrIg"])

    def test_delete_tag(self):
        self.tag.delete_tag(["etf3yRDwAAp-iiFzxd18DB63MCsXWhxA"])

    def test_delete_and_detect_group(self):
        r = self.tag.delete_and_detect_group(["etf3yRDwAAwbOSkiLW-LwUj5DDT0Q2sg"])
        assert r.json()['errcode'] == 0


