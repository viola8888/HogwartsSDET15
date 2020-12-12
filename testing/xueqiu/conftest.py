import pytest


@pytest.fixture(scope="session", autouse=True)
def conn_db():
    print("完成数据库连接aaaaaaaa")
    yield "database"
    print("关闭数据库连接aaaaaaaaa")
