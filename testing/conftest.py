import pytest

# pytest 会自动寻找conftest.py文件，执行里面的fixture内容
# 以被test_fixture.py调用
from pythoncode.calcular import Calculator


@pytest.fixture(params=['tom', 'jerry'])
def login(request):
    # yield 前面相当于setup  后面相当于 teardown
    print("登入操作")
    username = request.param
    # yield 相当于 return,如果后续需要调用 yield的返回值，只能使用装饰器的方式，传参的方式，不能获取到返回值
    yield username
    print("登出操作")


# @pytest.fixture(scope="session", autouse=True)
# def conn_db():
#     print("完成数据库连接")
#     yield "database"
#     print("关闭数据库连接")

@pytest.fixture(scope='module')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
