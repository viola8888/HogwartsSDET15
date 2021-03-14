import pytest
import yaml


@pytest.mark.parametrize('a, b', yaml.safe_load(open('test_demo.yaml', encoding="utf-8")))
def test_foo(a,b):
    print(f"a + b = {a + b}")