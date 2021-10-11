
if __name__ == "__main__":
    fibonacci()

def fibonacci(n: int):
    """
    return the NTH number of the fibonacci
    """
    if n<0:
        print("wrong number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas(n):
    pass