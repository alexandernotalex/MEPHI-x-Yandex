def is_palindrome(strk):
    if not isinstance(strk, str):
        raise TypeError("Input must be a string")

    return strk == strk[::-1]