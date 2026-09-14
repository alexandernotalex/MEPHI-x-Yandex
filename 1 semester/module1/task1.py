def sum(number_1, number_2):
    return number_1 + number_2

def difference(number_1, number_2):
    return number_1 - number_2

def composition(number_1, number_2):
    return number_2 * number_1

def division(number_1, number_2):
    return number_1 / number_2

number_1 = int(input("Введите 1 число:"))
number_2 = int(input("Введите 2 число:"))

print("Сумма:", sum(number_1, number_2))
print("Разность:", difference(number_1, number_2))
print("Произведение:", composition(number_1, number_2))
print("Деление:", division(number_1, number_2))