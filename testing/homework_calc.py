"""
作业一：
    1.补全计算器（加减乘除）的测试用例
    2.使用数据的数据驱动，节省代码编写量
    3.创建Fixure方法实现，测试开始前打印[计算开始],测试结束后打印[计算结束]
    4.将Fixture方法存放在conftest.py，设置scope=module
作业二：
    1.控制测试用例执行顺序，加-除-减-乘
    2.结合allure生成测试结果报告
"""
import pytest
import yaml

from pythoncode.calcular import Calculator


def add_datas():
    with open('./datas/add.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        add_int_data = datas['int']['datas']
        add_int_ids = datas['int']['ids']
        add_float_data = datas['float']['datas']
        add_float_ids = datas['float']['ids']
        return (add_int_data, add_int_ids, add_float_data, add_float_ids)


def sub_datas():
    with open('./datas/sub.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        sub_int_data = datas['int']['datas']
        sub_int_ids = datas['int']['ids']
        sub_float_data = datas['float']['datas']
        sub_float_ids = datas['float']['ids']
        return (sub_int_data, sub_int_ids, sub_float_data, sub_float_ids)


def mul_datas():
    with open('./datas/mul.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        mul_int_data = datas['int']['datas']
        mul_int_ids = datas['int']['ids']
        mul_float_data = datas['float']['datas']
        mul_float_ids = datas['float']['ids']
        return (mul_int_data, mul_int_ids, mul_float_data, mul_float_ids)


def div_datas():
    with open('./datas/div.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        div_data = datas['datas']
        div_ids = datas['ids']
        return (div_data, div_ids)


class TestCalc:

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a, b, expect', add_datas()[0], ids=add_datas()[1])
    def test_add_int(self, a, b, expect, get_calc):
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect', add_datas()[2], ids=add_datas()[3])
    def test_add_float(self, a, b, expect, get_calc):
        result = get_calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a, b, expect', sub_datas()[0], ids=sub_datas()[1])
    def test_sub_int(self, a, b, expect, get_calc):
        result = get_calc.sub(a, b)
        assert result == expect

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('a, b, expect', sub_datas()[2], ids=sub_datas()[3])
    def test_sub_float(self, a, b, expect, get_calc):
        result = get_calc.sub(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('a, b, expect', mul_datas()[0], ids=mul_datas()[1])
    def test_mul_int(self, a, b, expect, get_calc):
        result = get_calc.mul(a, b)
        assert result == expect

    @pytest.mark.run(order=8)
    @pytest.mark.parametrize('a, b, expect', mul_datas()[2], ids=mul_datas()[3])
    def test_mul_float(self, a, b, expect, get_calc):
        result = get_calc.mul(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expect', div_datas()[0], ids=div_datas()[1])
    def test_div(self, a, b, expect, get_calc):
        result = get_calc.div(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a, b', [
        (1.5, 0), (-14, 0)
    ])
    def test_div_zero(self, a, b, get_calc):
        with pytest.raises(ZeroDivisionError):
            get_calc.div(a, b)
