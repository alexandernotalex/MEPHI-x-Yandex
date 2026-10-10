def decimal_to_binary(num):
    if not isinstance(num, int):
        raise TypeError("Input must be a integer")
    if num < 0:
        raise ValueError("Only non-negative integers are allowed.")
    if num == 0:
        return 0
    ans = ""
    while num != 0:
        ans += str(num % 2)
        num //= 2
    ans = ans[::-1]
    return ans

# Пример использования
num = int(input("Введите десятичное число: "))
binary = decimal_to_binary(num)
print(f"Двоичное представление: {binary}")