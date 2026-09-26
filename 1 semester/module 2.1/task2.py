def tribonacci(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# Пример использования
n = int(input("Введите номер числа Трибоначчи: "))
result = tribonacci(n)
print(f"T({n}) = {result}")