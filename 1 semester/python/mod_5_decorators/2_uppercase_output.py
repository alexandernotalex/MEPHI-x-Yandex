import functools

def uppercase_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

# Пример
@uppercase_output
def greeting():
    return "hello"

print(greeting())  # "HELLO"