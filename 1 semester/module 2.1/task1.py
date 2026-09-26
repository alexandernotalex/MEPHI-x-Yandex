def calculate_months_to_threshold(start, rate, threshold):
    if rate <= 0:
        raise ValueError("Growth rate must be greater than 0.")
    if start <= 0 or threshold <= 0:
        raise ValueError("Start and threshold must be positive numbers.")
    counter = 0
    while start < threshold:
        start = start * (1 + rate / 100)
        counter += 1
    return counter

# Пример использования
start = int(input("Введите начальное количество пользователей: "))
rate = float(input("Введите темп роста в процентах: "))
threshold = int(input("Введите пороговое значение: "))

months = calculate_months_to_threshold(start, rate, threshold)
print(f"Количество месяцев для достижения порога: {months}")