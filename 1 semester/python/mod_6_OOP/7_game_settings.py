class GameSettings:
    """Класс для хранения настроек игры, реализованный как Singleton."""
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """Контролирует создание экземпляра."""
        if cls._instance is None:
            print("Создание нового экземпляра настроек...")
            cls._instance = super().__new__(cls)
        else:
            print("Возврат существующего экземпляра настроек...")
        return cls._instance

    def __init__(self):
        """Инициализирует настройки только один раз."""
        if self._initialized:
            return
        print("Первичная инициализация настроек...")
        self.difficulty = 'Normal'
        self.sound_volume = 75
        self._initialized = True

    def set_difficulty(self, level):
        """Устанавливает уровень сложности."""
        self.difficulty = level

    def set_sound_volume(self, volume):
        """Устанавливает громкость звука."""
        if 0 <= volume <= 100:
            self.sound_volume = volume
        else:
            print("Громкость должна быть в диапазоне от 0 до 100.")

    def display_settings(self):
        """Отображает текущие настройки."""
        print(f"Сложность: {self.difficulty}, Громкость: {self.sound_volume}")