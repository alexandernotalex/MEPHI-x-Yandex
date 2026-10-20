import functools
import time
from collections.abc import Iterable

def _make_predicate(retry_on):
    # Возвращает функцию predicate(result) -> True, если нужен повтор
    if retry_on is None:
        return lambda res: not bool(res)  # повторяем для falsy
    if callable(retry_on):
        return retry_on
    # Если передали итерируемое (tuple/list/set) — проверяем membership
    if isinstance(retry_on, Iterable) and not isinstance(retry_on, (str, bytes)):
        values = set(retry_on)
        return lambda res: res in values
    # Иначе — сравниваем на равенство
    return lambda res: res == retry_on

def retry(times=3, delay=0, retry_on=None):
    # Нормализация times (не используем raise)
    try:
        times = int(times)
    except Exception:
        times = 1
    if times < 1:
        times = 1

    predicate = _make_predicate(retry_on)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_result = None
            for attempt in range(1, times + 1):
                result = func(*args, **kwargs)
                last_result = result
                # Если predicate возвращает True — значит нужно повторить
                if predicate(result) and attempt < times:
                    if delay:
                        time.sleep(delay)
                    continue
                # Либо успех (predicate == False), либо последний попытка — вернуть result
                return result
            # Все попытки исчерпаны — вернуть последний результат
            return last_result
        return wrapper
    return decorator