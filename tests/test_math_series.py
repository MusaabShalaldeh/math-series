from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_1():
    #Arrange
    number = 10
    expected = 55
    #Act
    actual = fibonacci(number)
    #Assert
    assert actual == expected

def test_lucas_1():
    #Arrange
    number = 6
    expected = 18
    #Act
    actual = lucas(number)
    #Assert
    assert actual == expected

def test_lucas_2():
    #Arrange
    number = 2
    expected = 3
    #Act
    actual = lucas(number)
    #Assert
    assert actual == expected


def test_sum_series_1():
    #Arrange
    number = 7
    expected = 13
    #Act
    actual = sum_series(0,1,number)
    #Assert
    assert actual == expected

def test_sum_series_2():
    #Arrange
    number = 9
    expected = 76
    #Act
    actual = sum_series(2,1,number)
    #Assert
    assert actual == expected

def test_sum_series_3():
    #Arrange
    number = 2
    expected = 7
    #Act
    actual = sum_series(3,4,number)
    #Assert
    assert actual == expected