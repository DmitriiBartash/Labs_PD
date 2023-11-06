
    def test_delete_all_files_readonly(self):
        """
        Тестирует функцию delete_all_files() на удаление файлов с атрибутом `readonly`.

        """
        # Создаем тестовую папку
        test_dir = os.path.join(os.getcwd(), "test_files")
        os.mkdir(test_dir)

        # Создаем тестовые файлы с атрибутом `readonly`
        for i in range(10):
            file_path = os.path.join(test_dir, f"file_{i}.txt")
            with open(file_path, "w") as f:
                f.write("test_file_content")
            os.chmod(file_path, 0o444)

        # Удаляем все файлы в тестовой папке, включая файлы с атрибутом `readonly`
        Lab5_function.delete_all_files(test_dir)

        # Проверяем, что в тестовой папке не осталось файлов
        self.assertEqual(len(os.listdir(test_dir)), 0)

        # Удаляем тестовую папку
        shutil.rmtree(test_dir)
