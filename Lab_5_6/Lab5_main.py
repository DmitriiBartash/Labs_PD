# Импортируем модуль
import Lab5_function
import os

# Выбираем папку для резервного копирования
main_dir = Lab5_function.choose_dir("Введите путь к папке для нахождения: ")
backup_dir = Lab5_function.choose_dir("Введите путь к папке для резервного копирования: ")
delete_dir = Lab5_function.choose_dir("Введите путь к папке для удаления: ")
# print(backup_dir)
# work_files/files
# work_files/backup
# work_files/example_test

# Найти все файлы в папке `/tmp/files` и сохранить их в запасную папку `/tmp/backup`
Lab5_function.find_and_backup_files(main_dir, backup_dir)

# Удалить все файлы в папке `/tmp/files`
Lab5_function.delete_all_files(main_dir)

# Проверяем, что все файлы были удалены
assert len(os.listdir(delete_dir)) == 0


