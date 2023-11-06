import unittest
import os
import shutil
import Lab5_function

class FilesTest(unittest.TestCase):

    def test_find_and_backup_files(self):
        # Создаем тестовую папку
        test_dir = os.path.join(os.getcwd(), "test_files")
        os.mkdir(test_dir)

        # Создаем тестовые файлы
        for i in range(10):
            file_path = os.path.join(test_dir, f"file_{i}.txt")
            with open(file_path, "w") as f:
                f.write("test_file_content")

        # Копируем тестовые файлы в запасную папку
        backup_dir = os.path.join(os.getcwd(), "backup")
        Lab5_function.find_and_backup_files(test_dir, backup_dir)

        # Проверяем, что все тестовые файлы были скопированы в запасную папку
        self.assertEqual(len(os.listdir(backup_dir)), 10)

        # Удаляем тестовую папку и запасную папку
        shutil.rmtree(test_dir)
        shutil.rmtree(backup_dir)

    def test_delete_all_files(self):
        # Создаем тестовую папку
        test_dir = os.path.join(os.getcwd(), "test_files")
        os.mkdir(test_dir)

        # Создаем тестовые файлы
        for i in range(10):
            file_path = os.path.join(test_dir, f"file_{i}.txt")
            with open(file_path, "w") as f:
                f.write("test_file_content")

        # Удаляем все файлы в тестовой папке
        Lab5_function.delete_all_files(test_dir)

        # Проверяем, что в тестовой папке не осталось файлов
        self.assertEqual(len(os.listdir(test_dir)), 0)

        # Удаляем тестовую папку
        shutil.rmtree(test_dir)

    def test_find_and_backup_files_no_duplicates(self):
        # Создаем тестовую папку
        test_dir = os.path.join(os.getcwd(), "test_files")
        os.mkdir(test_dir)

        # Создаем тестовые файлы
        file_path = os.path.join(test_dir, "file.txt")
        with open(file_path, "w") as f:
            f.write("test_file_content")

        # Копируем тестовый файл в запасную папку
        backup_dir = os.path.join(os.getcwd(), "backup")
        Lab5_function.find_and_backup_files(test_dir, backup_dir)

        # Проверяем, что в запасной папке нет дубликатов
        self.assertEqual(len(os.listdir(backup_dir)), 1)

        # Удаляем тестовую папку и запасную папку
        shutil.rmtree(test_dir)
        shutil.rmtree(backup_dir)

    def test_delete_all_files_large_directory(self):
        """
        Тестирует функцию delete_all_files() на удаление большого количества файлов.

        """
        # Создаем тестовую папку
        test_dir = os.path.join(os.getcwd(), "test_files")
        os.mkdir(test_dir)

        # Создаем тестовые файлы в количестве 1000
        for i in range(1000):
            file_path = os.path.join(test_dir, f"file_{i}.txt")
            with open(file_path, "w") as f:
                f.write("test_file_content")

        # Удаляем все файлы в тестовой папке
        Lab5_function.delete_all_files(test_dir)

        # Проверяем, что в тестовой папке не осталось файлов
        self.assertEqual(len(os.listdir(test_dir)), 0)

        # Удаляем тестовую папку
        shutil.rmtree(test_dir)

if __name__ == "__main__":
    unittest.main()
