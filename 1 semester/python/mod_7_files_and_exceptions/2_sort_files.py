import os
import shutil


def sort_files(source_dir):
    """
    Сортирует файлы в исходной директории по подпапкам в зависимости от расширения.

    Args:
        source_dir (str): Путь к исходной директории.

    Raises:
        FileNotFoundError: Если исходная директория не существует.
    """
    if not os.path.isdir(source_dir):
        raise FileNotFoundError("Source directory does not exist.")

    file_mappings = {
        'images': ['.jpg', '.png', '.gif'],
        'documents': ['.txt', '.pdf', '.doc'],
        'videos': ['.mp4', '.mov', '.avi'],
    }

    # Создаем папки, если их нет
    for folder in list(file_mappings.keys()) + ['other']:
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Пропускаем папки
        if os.path.isdir(source_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, extensions in file_mappings.items():
            if file_ext in extensions:
                dest_path = os.path.join(source_dir, folder, filename)
                shutil.move(source_path, dest_path)
                moved = True
                break

        if not moved:
            dest_path = os.path.join(source_dir, 'other', filename)
            shutil.move(source_path, dest_path)

# Пример использования
# Перед запуском создайте папку 'downloads' и несколько файлов в ней
# (e.g., test.txt, image.jpg, movie.mp4, archive.zip)
source_directory = 'downloads'
if not os.path.exists(source_directory):
    os.mkdir(source_directory)

try:
    sort_files(source_directory)
    print(f"Файлы в '{source_directory}' были отсортированы.")
except FileNotFoundError as e:
    print(e)