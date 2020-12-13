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


"""
作业3【选做】：
    1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
    2、env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据
"""


def pytest_addoption(parser):
    group = parser.getgroup('hogwards')
    group.addoption(
        '--env',
        action='store',
        dest='env',
        default='test',
        choices=['dev', 'test', 'st'],
        help='自定义命令 --env  当前环境'
    )


@pytest.fixture
def get_env(request):
    ip_type = request.config.getoption("env")
    if ip_type == "test":
        return ("10.10.10.1")
    elif ip_type == "dev":
        return ("10.10.10.2")
    elif ip_type == 'st':
        return ("送审环境")
