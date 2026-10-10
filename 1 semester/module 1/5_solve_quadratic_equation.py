import math

def discriminant(a, b, c):
    return b ** 2 - 4 * a * c

def solve_quadratic(a, b, c):
    d = discriminant(a, b, c)
    if (d < 0):
        return "Комплексные"
    if (d == 0):
        x = round(- b / (2 * a), 5)
        return "1 действительный корень: " + x
    x_1 = round((- b + math.sqrt(d)) / (2 * a), 5)
    x_2 = round((- b - math.sqrt(d)) / (2 * a), 5)
    return "2 действительных корня: " + str(x_1) + " и " + str(x_2)
    
        

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

roots = solve_quadratic(a, b, c)
print("Корни уравнения:", roots)