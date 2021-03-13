from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 发起请求，判断url是不是我们预期的url
    if "quote.json" in flow.request.pretty_url :
        # 打开保存在本地的数据文件
        with open("D:\/testdata\stock1.json" , encoding='utf8') as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # 读取文件中的数据作为返回内容
                f.read(),
                {"Content-Type": "application/json"}  # (optional) headers
            )