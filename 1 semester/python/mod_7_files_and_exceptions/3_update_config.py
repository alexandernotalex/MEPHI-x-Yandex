import json

def update_config(config_path, new_settings):
    """
    Читает JSON-конфигурацию, обновляет ее и сохраняет обратно.

    Args:
        config_path (str): Путь к файлу конфигурации.
        new_settings (dict): Словарь с новыми настройками.

    Returns:
        dict: Обновленная конфигурация.

    Raises:
        ValueError: Если файл содержит некорректный JSON.
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in file.")

    config.update(new_settings)

    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    return config

# Пример использования
# Создайте файл config.json с начальными данными
settings_to_update = {'font_size': 16, 'show_notifications': False}
try:
    updated_config = update_config('config.json', settings_to_update)
    print("Конфигурация обновлена:", updated_config)
except ValueError as e:
    print(e)