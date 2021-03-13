from mitmproxy import http

def request(flow: http.HTTPFlow):
    # 增加请求的头信息中的字段
    flow.request.headers['myheader'] = 'violaa'
    print(flow.request.headers)