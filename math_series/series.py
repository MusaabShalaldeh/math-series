
if __name__ == "__main__":
    fibonacci()

def fibonacci(n: int):
    """
    return the NTH number of the fibonacci
    """
    if n<0:
        return("wrong number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas(n: int):
    """
    return the NTH number of the lucas
    """
    if n<0:
        return("wrong number")
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def sum_series(a,b,num):
    if num<0:
        return("wrong number")
    elif num == 0:
        return a
    elif num == 1:
        return b
    else:
        return sum_series(a,b,num-1)+sum_series(a,b,num-2)

