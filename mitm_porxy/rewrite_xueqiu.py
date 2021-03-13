import json
from mitmproxy import http

def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if 'quote.json' in flow.request.pretty_url and 'x=' in flow.request.pretty_url:
        # 把响应数据转换为python对象，保存到data对象中
        data = json.loads(flow.response.content)
        # 修改数据
        # data['data']['items'][0]['quote']['name'] = 'hogwards0000000000000'
        data['data']['items'][1]['quote']['name'] = data['data']['items'][1]['quote']['name'] * 2
        data['data']['items'][2]['quote']['name'] = ' '
        # 把修改后的内容赋值 response  原始数据格式
        flow.response.text = json.dumps(data)
