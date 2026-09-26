def num_digits(num):
    ans = 0
    if num < 0:
        raise ValueError("Input must be non-negative")
    if num == 0:
        return 1
    while num != 0:
        num //= 10
        ans += 1
    return ans
        
        

def armstr(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num < 0:
        raise ValueError("Input must be non-negative")
    if num == 0:
        return
    for value in range(1, num + 1):
        ans = 0
        n_digits = num_digits(value)
        tmp = value
        while tmp != 0:
            ans += (tmp % 10) ** n_digits
            tmp //= 10
        if ans == value:
            print(value, end= " ")
    return
            
num = int(input("Введите верхнюю границу диапазона: "))
armstr(num)