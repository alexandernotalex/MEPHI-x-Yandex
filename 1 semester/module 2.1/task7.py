def triangle_type(trian1, trian2, trian3):
    if not isinstance(trian1, (int, float)) or \
      not isinstance(trian2, (int, float)) or not isinstance(trian3, (int, float)):
        raise TypeError("Input must be an integer or float")
    
    if trian1 <= 0 or trian2 <= 0 or trian3 <= 0:
        return "Невозможно"
    
    if trian1 + trian2 <= trian3 or trian1 + trian3 <= trian2 or \
      trian2 + trian3 <= trian1:
        return "Невозможно"
    
    if trian1 == trian2 == trian3:
        return "Равносторонний"
    
    if trian1 == trian2 or trian2 == trian3 or trian3 == trian1:
        return "Равнобедренный"
    
    return "Разносторонний"
        

# Пример использования
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

result = triangle_type(a, b, c)
print(f"Тип треугольника: {result}")