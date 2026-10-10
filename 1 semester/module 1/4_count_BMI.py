def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if (bmi < 16):
        return "Выраженный дефицит массы тела"
    elif (bmi < 18.5):
        return "Недостаточная масса тела"
    elif (bmi < 25):
        return "Нормальная масса тела"
    elif (bmi < 30):
        return "Избыточная масса тела (предожирение)"
    elif (bmi < 35):
        return "Ожирение I степени"
    elif (bmi < 40):
        return "Ожирение II степени"
    else:
        return "Ожирение III степени (морбидное)"

weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

print("Ваш ИМТ: ", round(bmi, 5))
print("Категория: ", category)