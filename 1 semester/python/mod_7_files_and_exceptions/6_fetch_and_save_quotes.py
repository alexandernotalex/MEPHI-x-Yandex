import requests
import json

def fetch_and_save_quotes(url, file_path, num_quotes=5):
    """
    Собирает случайные цитаты с API и сохраняет их в JSON-файл.

    Args:
        url (str): URL API для получения цитат.
        file_path (str): Путь для сохранения JSON-файла.
        num_quotes (int): Количество цитат для сбора.
    """
    quotes_list = []
    print(f"Сбор {num_quotes} цитат...")

    for i in range(num_quotes):
        try:
            response = requests.get(url, timeout=5)
            # Проверяем, успешен ли запрос
            response.raise_for_status()

            data = response.json()
            quote_info = {
                'quote': data.get('content'),
                'author': data.get('author')
            }
            quotes_list.append(quote_info)
            print(f"Цитата {i+1}/{num_quotes} получена.")

        except requests.exceptions.RequestException as e:
            print(f"Ошибка сети или HTTP: {e}")
            break # Прерываем цикл при ошибке
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON. Получен невалидный ответ.")
            break

    if not quotes_list:
        print("Не удалось собрать ни одной цитаты.")
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(quotes_list, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Не удалось записать в файл {file_path}: {e}")


API_URL = "https://api.quotable.io/random"
OUTPUT_FILE = "quotes.json"

fetch_and_save_quotes(API_URL, OUTPUT_FILE, num_quotes=3)
print(f"Собрано и сохранено 3 цитаты в файл {OUTPUT_FILE}") 