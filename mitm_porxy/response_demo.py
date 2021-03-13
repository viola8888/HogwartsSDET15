from mitmproxy import http

def response(flow: http.HTTPFlow):
    print(flow.response.content)