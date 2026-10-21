def parse_log_file(log_path):
    """
    Анализирует лог-файл и подсчитывает количество записей каждого уровня.

    Args:
        log_path (str): Путь к лог-файлу.

    Returns:
        dict: Словарь с количеством записей по уровням ('INFO', 'WARNING', 'ERROR').

    Raises:
        FileNotFoundError: Если файл не найден.
    """
    log_levels = ['INFO', 'WARNING', 'ERROR']
    counts = {}

    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            for line in f:
                for level in log_levels:
                    if line.startswith(level + ':'):
                        # Увеличиваем счетчик или инициализируем, если ключ новый
                        counts[level] = counts.get(level, 0) + 1
                        break  # Переходим к следующей строке после нахождения уровня
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file not found at path: {log_path}")

    return counts