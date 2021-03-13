from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # 发起请求，判断url是不是我们预期的url
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 创造一个 response
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )