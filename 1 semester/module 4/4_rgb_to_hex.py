def rgb2hex(r=0, g=0, b=0):
    """
    Конвертирует значения RGB в шестнадцатеричную строку.
    
    Параметры:
    r, g, b (int): Значения цветовых компонент (0-255)
    
    Возвращает:
    str: Цвет в формате #rrggbb
    
    Выбрасывает:
    TypeError: Если компоненты не целые числа
    ValueError: Если значения вне диапазона 0-255
    """

    for name, val in (("r", r), ("g", g), ("b", b)):
        if not isinstance(val, int):
            raise TypeError(f"{name} component must be int, got {type(val).__name__}")
        if not (0 <= val <= 255):
            raise ValueError(f"{name} component {val} out of range 0..255")
    return "#{:02x}{:02x}{:02x}".format(r, g, b).lower()


def hex2rgb(hex_str):
    """
    Конвертирует шестнадцатеричную строку в словарь RGB.
    
    Поддерживаемые форматы:
    - #rrggbb
    - rrggbb
    - #rgb → расширяется в #rrggbb
    
    Параметры:
    hex_str (str): Шестнадцатеричное представление цвета
    
    Возвращает:
    dict: Словарь с ключами 'r', 'g', 'b' и значениями 0-255
    
    Выбрасывает:
    TypeError: Если вход не строка
    ValueError: При неверном формате или недопустимых символах
    """

    if not isinstance(hex_str, str):
        raise TypeError("hex value must be a string")
    
    # Нормализация строки (удаление пробелов и решетки)
    clean_hex = hex_str.strip().lstrip('#')
    
    # Проверка длины
    if len(clean_hex) == 3:
        # Расширение формата #rgb до #rrggbb
        clean_hex = ''.join(c * 2 for c in clean_hex)
    elif len(clean_hex) != 6:
        raise ValueError("hex string must be in format rrggbb or rgb (with or without leading #)")
    
    return {
        'r': int(clean_hex[0:2], 16),
        'g': int(clean_hex[2:4], 16),
        'b': int(clean_hex[4:6], 16)
    }
