class Vehicle:
    """Базовый класс для транспортных средств."""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """Возвращает основную информацию о транспортном средстве."""
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    """Класс для автомобилей, наследующийся от Vehicle."""
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        """Переопределенный метод для отображения информации об автомобиле."""
        base_info = super().display_info()
        return f"{base_info}, {self.num_doors} двери"

class Motorcycle(Vehicle):
    """Класс для мотоциклов, наследующийся от Vehicle."""
    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume

    def display_info(self):
        """Переопределенный метод для отображения информации о мотоцикле."""
        base_info = super().display_info()
        return f"{base_info}, объем двигателя: {self.engine_volume}cc"
