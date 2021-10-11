from math_series import __version__
from math_series.series import fibonacci, lucas


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_1():
    #Arrange
    number = 10
    expected = 55
    #Act
    result = fibonacci(10)
    #Assert
    assert result == expected

def test_lucas_1():
    #Arrange
    number = 5
    expected = 18
    #Act
    result = lucas(5)
    #Assert
    assert result == expected