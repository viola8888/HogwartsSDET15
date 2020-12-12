import pytest


@pytest.mark.login
def test_login1():
    print("登入用例1")


@pytest.mark.login
def test_login2():
    print("登入用例2")


def test_login3():
    print("登入用例3")


@pytest.mark.search
def test_search1():
    print("搜索用例1")


@pytest.mark.search
def test_search2():
    print("搜索用例2")
