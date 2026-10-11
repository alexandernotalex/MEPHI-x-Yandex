def is_palindrome(string):
    """Обычная проверка палиндрома."""
    return string == string[::-1]


def is_palindrome_recursive(string):
    """Рекурсивная проверка палиндрома."""
    if len(string) <= 1:
        return True
    res = string[0] == string[-1]
    return res and is_palindrome_recursive(string[1:-1])


# Основная программа
string_input = input("Введите строку: ")

print("Обычный палиндром: ", is_palindrome(string_input))
print("Палиндром через рекурсию: ", is_palindrome_recursive(string_input))