def compress_string(strk):
    if not isinstance(strk, str):
        raise TypeError("Input must be a string")

    if strk == "":
        return ""

    result = ""
    current_char = strk[0]
    count = 1

    for char in strk[1:]:
        if char == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = char
            count = 1
    result += current_char + str(count)

    return result

# Пример использования
test_str = "aaabbbcccaaa"
result = compress_string(test_str)
print("Сжатая строка:", result)