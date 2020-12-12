import pytest
import yaml

from pythoncode.calcular import Calculator


def get_datas():
    with open('./datas/calc.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        add_datas = datas['add']['datas']
        add_ids = datas['add']['ids']
        print(add_datas, add_ids)
        return (add_datas, add_ids)


def steps(addstepsfile, calc, a, b, expect):
    with open('./steps/add.yml', encoding='utf-8') as f:
        steps = yaml.safe_load(f)

        for step in steps:
            if 'add' == step:
                result = calc.add(a, b)
            elif 'add1' == step:
                result = calc.add1(a, b)
            assert result == expect


class TestCalc:
    # def setup_class(self):
    #     print("开始计算")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    # print("结束计算")

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        # calc = Calculator()
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert result == expect

    # def test_add1(self):
    #     # calc = Calculator()
    #     result = self.calc.add(100, 100)
    #     assert result == 200
    #
    # def test_add2(self):
    #     # calc = Calculator()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2

    @pytest.mark.parametrize('a, b', [
        (1.5, 0), (-14, 0)
    ])
    def test_div(self, get_calc, a, b):
        with pytest.raises(ZeroDivisionError):
            # self.calc.div(a, b)
            get_calc.div(a, b)

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add_steps(self, a, b, expect, get_calc):
        # assert 2 == self.calc.add(1, 1)
        # assert 3 == self.calc.add1(1, 2)
        # assert 0 == self.calc.add(-1, 1)
        # steps('./steps/add.yml', self.calc, a, b, expect)
        steps('./steps/add.yml', get_calc, a, b, expect)
