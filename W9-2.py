#斐波那契數列(遞迴實現)


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
    return
print(fibonacci_recursive(5))