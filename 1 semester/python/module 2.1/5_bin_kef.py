def bin_kef(num, kef):
    if not isinstance(num, int) or not isinstance(kef, int):
        raise TypeError("Arguments must be integers.")
    if num < 0 or kef < 0 or kef > num:
        raise ValueError("Invalid values: require 0 ≤ kef ≤ num")
    if kef > num - kef:
        kef = num - kef
    ans = 1
    for i in range(kef):
        ans *= num - i
    for i in range(1, kef + 1):
        ans //= i
    return ans

# Пример использования
num = int(input("Введите число n: "))
kef = int(input("Введите число k: "))
result = bin_kef(num, kef)
print(f"C({num}, {kef}) = {result}")