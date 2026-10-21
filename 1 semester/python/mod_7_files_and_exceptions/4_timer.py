import time

class Timer:
    """
    Контекстный менеджер для измерения времени выполнения блока кода.
    """
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"Execution time: {execution_time:.2f} seconds")

        # Если было исключение, оно будет проброшено дальше,
        # так как мы не возвращаем True.
        # Это позволяет увидеть время выполнения даже при ошибке.
        return False

print("Запускаем долгую операцию...")
with Timer():
    time.sleep(2)
print("Операция завершена.")

print("\nЗапускаем операцию с ошибкой...")
try:
    with Timer():
        time.sleep(0.5)
        raise ValueError("Что-то пошло не так!")
except ValueError as e:
    print(f"Поймано исключение: {e}") 