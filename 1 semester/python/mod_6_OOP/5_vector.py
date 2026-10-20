class VectorOperationError(Exception):
    """Пользовательское исключение для некорректных операций с векторами."""
    pass

class Vector:
    """Класс для представления и операций с 2D-векторами."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Возвращает строковое представление вектора."""
        return f"Вектор({self.x}, {self.y})"

    def __add__(self, other):
        """Реализует сложение векторов."""
        if not isinstance(other, Vector):
            raise VectorOperationError("Операция сложения возможна только с другим вектором.")
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        """Реализует умножение вектора на скаляр."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Умножение возможно только на число.")
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Реализует проверку на равенство векторов."""
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y