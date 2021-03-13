import json

from mitm_porxy.generate_testcase import json_travel


def test_json_travel():
    # print("看看问题在哪")
    # with open("demo.json") as f:
    #     data = json.load(f)
    #     print(data)
    #     # print(json.dumps(json_travel(data, array=3), indent=2, ensure_ascii=False))
    #     # print(json.dumps(json_travel(data, text=4), indent=2, ensure_ascii=False))
    #     print(json.dumps(json_travel(data, num=6), indent=2, ensure_ascii=False))
    with open("demo_demo.json", encoding='utf8') as f:
        data = json.load(f)
        print(data)
        print(json.dumps(json_travel(data, text=4), indent=2, ensure_ascii=False))