import functools

def enforce_types(*types):
    # если нет типов — просто возвращаем декоратор-идентичность
    if len(types) == 0:
        def identity(func):
            return func
        return identity

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, expected in enumerate(types):
                if i >= len(args):
                    break  # не передан этот позиционный аргумент
                if not isinstance(args[i], expected):
                    raise TypeError(
                        f"argument {i+1} must be {expected!r}, got {type(args[i])!r}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator
