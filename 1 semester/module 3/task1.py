def replace_characters(lst, old, new):
    if not isinstance(lst, list):
        raise TypeError("lst must be a list of strings")
    if not isinstance(old, str) or not isinstance(new, str) or len(old) != 1 or len(new) != 1:
        raise TypeError("old and new must be single characters and str")
    
    new_str = ""
    for i in range(len(lst)):
        new_str += (lst[i] + (" " if i != len(lst) - 1 else ""))
    string = new_str.replace(old, new)
    return string.split()

# Пример использования
test_list = ["hello", "world"]
old_char = "o"
new_char = "1"

result = replace_characters(test_list, old_char, new_char)
print("Результат:", result)