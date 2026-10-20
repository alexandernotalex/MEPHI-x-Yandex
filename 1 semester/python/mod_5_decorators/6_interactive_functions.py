import functools
import inspect

def asks(arg_name, prompt):
    """
    Декоратор: добавляет описание одного аргумента функции.
    arg_name: имя параметра функции
    prompt: строка, которая будет показана пользователю при запросе
    """
    def decorator(func):
        # Создаём/дополняем список метаданных на самой функции
        asks_list = getattr(func, '__asks__', None)
        if asks_list is None:
            func.__asks__ = []
        func.__asks__.append((arg_name, prompt))
        return func
    return decorator

def interactive(title=None):
    """
    Декоратор: превращает функцию в интерактивную программу.
    title: заголовок, печатаемый перед началом диалога
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if title:
                print(title)

            asks_list = getattr(func, '__asks__', [])

            # Переворачиваем, чтобы восстановить порядок появления декораторов в файле
            prompts = list(reversed(asks_list))

            collected = {}
            for name, prompt in prompts:
                try:
                    value = input(prompt)
                except EOFError:
                    # Если вход неожиданно кончился, используем пустую строку
                    value = ''
                collected[name] = value

            # Попытка вызвать функцию по именованным аргументам
            try:
                result = func(**collected)
            except TypeError:
                # Если функция не принимает именованные аргументы, попробуем собрать позиционные
                sig = inspect.signature(func)
                positional = []
                for param in sig.parameters.values():
                    if param.name in collected:
                        positional.append(collected[param.name])
                    elif param.default is not inspect._empty:
                        positional.append(param.default)
                    else:
                        positional.append(None)
                result = func(*positional)

            # Печатаем результат (если он не None)
            if result is not None:
                print(result)
            return None
        return wrapper
    return decorator

@interactive('Calculator Program')
@asks('x', 'Enter first number: ')
@asks('y', 'Enter second number: ')
def calculate(x, y):
    """Складывает два числа."""
    return int(x) + int(y)

calculate()
