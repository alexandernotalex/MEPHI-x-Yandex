import time

def move_to_end(my_list, element):
    """Перемещает элемент в конец списка (обычный метод)."""
    if element not in my_list:
        return False
    result = [item for item in my_list if item != element]
    result.extend([element] * my_list.count(element))
    return result

def move_to_end_recursive(my_list, element):
    """Перемещает элемент в конец списка (рекурсивный метод)."""
    if not my_list:
        return []
    if my_list[0] == element:
        return move_to_end_recursive(my_list[1:], element) + [element]
    return [my_list[0]] + move_to_end_recursive(my_list[1:], element)

def time_measurement(func, *args, **kwargs):
    """Измеряет время выполнения функции и возвращает результат и время выполнения."""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed

# Примеры входных данных
test_cases = [
    ([2, 1, 3, 2, 4, 2, 5], 2),    # Стандартный случай
    ([1, 2, 3, 4], 5),             # Элемент отсутствует
    ([], 1),                       # Пустой список
    ([7, 7, 7, 7], 7),             # Все элементы одинаковые
    (list(range(1000)), 500)       # Большой список (для сравнения производительности)
]

print("Сравнение производительности методов:")
print("-" * 50)

for i, test_data in enumerate(test_cases):

    lst, elem = test_data if len(test_data) == 2 else (test_data[0], None)
            
    res_iter, time_iter = time_measurement(move_to_end, lst, elem)
    print(f"Обычный метод: {res_iter}, Время: {time_iter:.6f} сек")
    
    
    try:
        res_rec, time_rec = time_measurement(move_to_end_recursive, lst, elem)
        print(f"Рекурсивный метод: {res_rec}, Время: {time_rec:.6f} сек") 

        if time_iter < time_rec:
            print(f"Обычный метод быстрее на {time_rec/time_iter:.2f}x")
        else:
            print(f"Рекурсивный метод быстрее на {time_iter/time_rec:.2f}x")
            
    except RecursionError:
        print("Рекурсивный метод: Превышена глубина рекурсии!")
    
    print("-" * 50)

