def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(5))  # 5
print(fib(10))  # 55
print(fib(2))  # 1


def palindrome(value: str) -> bool:
    for i in range(len(value)):
        if value[-i] != value[i - 1]:
            return False
    return True


print(palindrome('AaaA'))  # True
print(palindrome('AbabA'))  # True
print(palindrome('AbsFa'))  # False


def bubble_sort(value: list):
    for run in range(len(value) - 1):
        for i in range(len(value) - 1):
            if value[i] > value[i + 1]:
                value[i], value[i + 1] = value[i + 1], value[i]
    return value


print(bubble_sort([3, 5, 4, 8, 2, 6]))  # [2, 3, 4, 5, 6, 8]
print(bubble_sort([35, 42, 82, 55, 12]))  # [12, 35, 42, 55, 82]
print(bubble_sort([0, 125, 1200, 364]))  # [0, 125, 364, 1200]
