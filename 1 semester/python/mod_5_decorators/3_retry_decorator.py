import functools
import time

def retry(times=3, exceptions=(Exception,), delay=0):
    if not isinstance(times, int) or times < 1:
        raise ValueError("times must be integer >= 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    if attempt == times:
                        break
                    if delay:
                        time.sleep(delay)
            # если все попытки неудачны — пробрасываем последнее исключение
            raise last_exc
        return wrapper
    return decorator
