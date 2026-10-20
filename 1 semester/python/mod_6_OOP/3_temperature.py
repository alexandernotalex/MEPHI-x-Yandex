class Temperature:
    """Класс для работы с температурой в Цельсиях и Фаренгейтах."""
    def __init__(self, celsius):
        self.celsius = celsius  # Используем сеттер при инициализации

    @property
    def celsius(self):
        """Геттер для температуры в Цельсиях."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Сеттер для температуры в Цельсиях с валидацией."""
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля.")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Геттер, вычисляющий температуру в Фаренгейтах."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Сеттер, устанавливающий температуру через Фаренгейты."""
        self.celsius = (value - 32) * 5/9