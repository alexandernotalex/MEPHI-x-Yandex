def how_many_times(message):
    counter = 0
    if not isinstance(message, str):
        raise TypeError("Input must be a string.")
    for char in message:
        if not (ord('a') <= ord(char) <= ord('z')) and ord(char) != 32:
            raise ValueError("Message contains unknown character.")
        counter += (ord(char) - ord('a') + 1)
    return counter
    


# Пример использования
message = input("Введите сообщение (строчные буквы): ")
clicks = how_many_times(message)
print(f"Количество нажатий: {clicks}")