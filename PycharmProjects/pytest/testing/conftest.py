import pytest


@pytest.fixture(scope="session", autouse=True)
def login():
    print("开始计算")
    yield "yield"
    print("计算结束")
