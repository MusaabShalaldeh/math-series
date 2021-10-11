from math_series import __version__
from math_series.series import fibonacci


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_1():
    #Arrange
    number = 10
    expected = 50
    #Act
    result = fibonacci(10)
    #Assert
    assert result == expected