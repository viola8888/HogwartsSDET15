import pytest

from pythoncode.calcular import Calculator


class TestCalc:

    def setup_class(self):
        self.calc = Calculator()
        print("计算实例化")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, expect', [
        (13, 15, 28), (-14, 14, 0), (-1, -14, -15), (0, 14, 14), (1, 1, 2)
    ], ids=[
        'positive_integer', 'negative_positive', 'negative_integer', 'negative_zero', 'same_number'
    ])
    def test_add_int(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [
        (1.3, 1.5, 2.8), (-1.4, 1.4, 0), (-1, -1.4, -2.4), (0, 1.4, 1.4), (1.1, 1.1, 2.2)
    ], ids=[
        'decimal_float', 'negative_decimal', 'negative_float', 'negative_zero', 'same_number'
    ])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a, b, expect', [
        (13, 15, -2), (-14, 14, -28), (-1, -14, 13), (14, 5, 9), (1, 1, 0)
    ], ids=[
        'positive_integer', 'negative_positive', 'negative_integer', 'negative_zero', 'same_number'
    ])
    def test_sub_int(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [
        (1.3, 1.5, -0.2), (-1.4, 1.4, -2.8), (-1, -1.4, 0.4), (0, 1.4, -1.4), (1.1, 1.1, 0)
    ], ids=[
        'decimal_float', 'negative_decimal', 'negative_float', 'negative_zero', 'same_number'
    ])
    def test_sub_float(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a, b, expect', [
        (13, 15, 195), (-14, 14, -196), (-1, -14, 14), (1, 1, 1), (0, 1, 0), (1, 0, 0)
    ], ids=[
        'positive_integer', 'negative_positive', 'negative_integer', 'same_number', 'zero_01', 'zero_02'
    ])
    def test_mul_int(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [
        (1.3, 1.5, 1.95), (-1.4, 1.4, -1.96), (-1, -1.4, 1.4), (-1.87, 1.4, -2.62), (1.1, 1.1, 1.21)
    ], ids=[
        'decimal_float', 'negative_decimal', 'negative_float', 'negative_zero', 'same_number'
    ])
    def test_mul_float(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a, b, expect', [
        (13, 15, 0.87), (-14, 14, -1), (-1, -14, 0.07), (1, 1, 1), (10.88, 3.1, 3.51), (0, 3.1, 0)
    ], ids=[
        'positive_integer', 'negative_positive', 'negative_integer', 'same_number', 'float_float', 'zero'
    ])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a, b', [
        (1.5, 0), (-14, 0)
    ])
    def test_div_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)
