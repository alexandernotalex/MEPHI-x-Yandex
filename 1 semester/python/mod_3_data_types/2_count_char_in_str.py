def count_char(lst, char):
    if not isinstance(lst, list):
        raise TypeError("lst must be a list of strings")
    if not isinstance(char, str) or len(char) != 1:
        raise TypeError("char must be single characters and str")
    count_char = []
    for i in range(len(lst)):
        count_char.append(lst[i].count(char))
    return count_char

# Пример использования
print(count_char(["helloo", "world"], "o"))             # [2, 1]
print(count_char(["apple", "banana", "avocado"], "a"))  # [1, 3, 2]
print(count_char(["", " ", "a"], " "))                  # [0, 1, 0]
print(count_char([], "a"))                              # []