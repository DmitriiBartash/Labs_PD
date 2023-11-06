"""
Модуль для работы с файлами.

Обеспечивает следующие функции:

* `find_and_backup_files()` - находит все файлы в папке и сохраняет их в запасную папку.
* `delete_all_files()` - удаляет все файлы в папке.

"""

import os
import shutil

def find_and_backup_files(source_dir, backup_dir):
    """
    Находит все файлы в папке `source_dir` и сохраняет их в запасную папку `backup_dir`.

    Parameters:
        source_dir: Путь к исходной папке.
        backup_dir: Путь к запасной папке.

    """
    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)

    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        shutil.copy(file_path, os.path.join(backup_dir, file))

def delete_all_files(dir):
    """
    Удаляет все файлы в папке `dir`.

    Parameters:
        dir: Путь к папке.

    """
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        os.remove(file_path)


def choose_dir(prompt):
    """
    Выбирает папку из пользовательского ввода.

    Parameters:
        prompt: Текст приглашения.

    Returns:
        Путь к выбранной папке.

    """

    while True:
        dir = input(prompt)

        # Проверяем, что папка существует
        if os.path.exists(dir):
            return dir

        print("Папка не существует. Попробуйте снова.")