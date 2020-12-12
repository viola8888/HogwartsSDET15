import time

import pytest


# pytest 会自动寻找conftest.py文件，执行里面的fixture内容


# @pytest.fixture()
# def login():
#     # yield 前面相当于setup  后面相当于 teardown
#     print("登入操作")
#     # yield 相当于 return,如果后续需要调用 yield的返回值，只能使用装饰器的方式，传参的方式，不能获取到返回值
#     yield ['tom', '123456']
#     print("登出操作")
#
# @pytest.fixture()
# def conn_db():
#     print("完成数据库连接")

@pytest.mark.run(order=2)
def test_case1(login):
    print(login)
    print("用例1")


# @pytest.mark.flaky(reruns=5, reruns_delay=2)
@pytest.mark.parametrize('a', ['1', '2', '2', '4'])
@pytest.mark.run(order=3)
def test_case2(a):
    time.sleep(2)
    print(a)
    assert False


@pytest.mark.run(order=4)
def test_case3(login, conn_db):
    # 有多个fixture时，按照传入的顺序执行
    print("用例3")


@pytest.mark.run(order=1)
@pytest.mark.usefixtures("login")
def test_case4():
    print("用例4")
    assert True
    assert False
    assert 1 == 2


@pytest.mark.run(order=5)
@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    pytest.assume(x == y)
    pytest.assume(True)
    pytest.assume(False)
