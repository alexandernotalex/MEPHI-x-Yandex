class Employee:
    """Класс для представления сотрудников с подсчетом их количества."""
    total_employees = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.total_employees += 1

    @classmethod
    def get_total_employees(cls):
        """Возвращает общее количество созданных сотрудников."""
        return cls.total_employees

    @classmethod
    def from_string(cls, employee_string):
        """Создает экземпляр сотрудника из строки 'Имя-Должность'."""
        try:
            name, position = employee_string.split('-')
            return cls(name, position)
        except ValueError:
            raise ValueError("Строка должна быть в формате 'Имя-Должность'")

    @staticmethod
    def is_valid_email(email):
        """Проверяет, является ли строка валидным email-адресом (упрощенная проверка)."""
        if '@' in email and '.' in email.split('@')[1]:
            return True
        return False