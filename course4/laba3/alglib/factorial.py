def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)
