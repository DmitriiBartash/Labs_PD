import datetime
import os

# 1_part
with open('lab_3_first_part/xset.csv', 'w') as xdataset, open('lab_3_first_part/yset.csv', 'w') as ydataset:
    fp = open('dataset.csv', 'r')
    massiv = fp.readlines()
    stroke1 = ''
    stroke2 = ''

    for mass in massiv:
        stroke1 = mass.split(",")
        stroke1 = stroke1[0] + "\n"

        index = mass.find(",")
        stroke2 = mass[index + 2:]
        for i in stroke1:
            xdataset.write(i)

        for i in stroke2:
            ydataset.write(i)

# 2 part of lab
t2 = open('dataset.csv', 'r')
massiv = t2.readlines()

# Получаем список всех дат в исходном файле.
dates = []
for line in massiv:
    date = line.split("T")[0]
    dates.append(date)

# Находим границы каждого года.
boundaries = []
for i in range(len(dates)):
    if i == 0:
        boundaries.append(dates[i])
    elif dates[i].split("-")[0] != dates[i - 1].split("-")[0]:
        boundaries.append(dates[i])

# Создаем список файлов, которые будут созданы.
filenames = []
for i in range(len(boundaries) - 1):
    filename = "{}_{}".format(boundaries[i], boundaries[i + 1])
    filenames.append("lab_3_second_part/" + filename + ".csv")

# Создаем и заполняем каждый файл.
for i in range(len(boundaries) - 1):
    with open(filenames[i], "w") as f:
        for line in dates:
            date = line.split(",")[0]
            if boundaries[i] >= date >= boundaries[i + 1]:
                line = line + "\n"
                f.write(line)

# 3 part of lab
# Получаем список всех дат в исходном файле.
dates = []
for line in massiv:
    date = line.split("T")[0]
    dates.append(date)

# Получаем номера недель для всех дат.
week_numbers = []
for date in dates:
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    week_number = date.isocalendar()[1]
    week_numbers.append(week_number)

# Находим границы каждой недели.
boundaries = []
boundaries.append(dates[0])
for i in range(1, len(dates)):
    if week_numbers[i] != week_numbers[i - 1]:
        boundaries.append(dates[i])

# Создаем список файлов, которые будут созданы.
filenames = []
for i in range(len(boundaries) - 1):
    filename = "{}_{}".format(boundaries[i], boundaries[i + 1])
    filenames.append("lab_3_third_part/" + filename + ".csv")

# Создаем и заполняем каждый файл.
for i in range(len(boundaries) - 1):
    with open(filenames[i], "w") as week:
        for line in dates:
            date = line.split(",")[0]
            if boundaries[i] >= date >= boundaries[i + 1]:
                line = line + "\n"
                week.write(line)


# 4 part of lab
def get_user_choice(choices):
    # Выводим список вариантов выбора.
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

    # Получаем ввод пользователя.
    user_input = input("Введите свой выбор: ")

    # Проверяем правильность ввода пользователя.
    try:
        user_choice = int(user_input)
    except ValueError:
        print("Неправильный ввод.")
        return get_user_choice()

    # Если выбор пользователя некорректен, возвращаем None.
    if user_choice < 1 or user_choice > len(choices):
        print("Некорректный выбор.")
        return None

    # Возвращаем выбор пользователя.
    return user_choice


def get_data_from_xset(date_user, filename):

    # Открываем файл для чтения.
    with open(filename, "r") as reader:
        # Получаем список всех дат в исходном файле.
        dates = []
        for line in reader:
            date = line.split("T")[0]
            # Преобразуем строку в объект datetime.
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            dates.append(date)

           # Ищем строку с указанной датой.
        for index, line in enumerate(dates):
            if line == date_user:
                print("Ваш результат является: ", line, "По номеру строки: ", index+1)
                return line

    # Если данные для указанной даты не найдены, возвращаем None.
    return None


def get_data_from_year(date_user, file_path):
    # Получаем список всех файлов в папке.
    files = os.listdir(file_path)
  
    # Читаем данные из файлов.
    for file in files:
        # Открываем файл для чтения.
        with open(os.path.join(file_path, file), "r") as reader:
            # Получаем список всех дат в исходном файле.
            dates = []
            for line in reader:
                date = line.split('\n')[0]

                # Преобразуем строку в объект datetime.
                date = datetime.datetime.strptime(date, "%Y-%m-%d")
                dates.append(date)

            # Ищем строку с указанной датой.
            for index, line in enumerate(dates):
                if line == date_user:
                    print("Ваш результат является: ", line, "По номеру строки: ", index+1)
                    return line
    # Если данные для указанной даты не найдены, возвращаем None.
    return None

def get_data_from_week(date_user, file_path):
   
    # Получаем список всех файлов в папке.
    files = os.listdir(file_path)
    # Читаем данные из файлов.
    for file in files:
        # Открываем файл для чтения.
        with open(os.path.join(file_path, file), "r") as reader:
            # Получаем список всех дат в исходном файле.
            dates = []
            for line in reader:
                date = line.split('\n')[0]
                # Преобразуем строку в объект datetime.
                date = datetime.datetime.strptime(date, "%Y-%m-%d")
                dates.append(date)

            # Ищем строку с указанной датой.
            for index, line in enumerate(dates):
                if line == date_user:
                    print("Ваш результат является: ", line, "По номеру строки: ", index+1)
                    return line

    # Если данные для указанной даты не найдены, возвращаем None.
    return None

def get_data_from_dataset(date_user, filename):

    # Открываем файл для чтения.
    with open(filename, "r") as reader:
        # Получаем список всех дат в исходном файле.
        dates = []
        for line in reader:
            date = line.split("T")[0]
            # Преобразуем строку в объект datetime.
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            dates.append(date)

           # Ищем строку с указанной датой.
        for index, line in enumerate(dates):
            if line == date_user:
                print("Ваш результат является: ", line, "По номеру строки: ", index+1)
                return line

    # Если данные для указанной даты не найдены, возвращаем None.
    return None


def main():
    # Получаем дату от пользователя.
    date = datetime.datetime.strptime(input("Введите дату: "), "%Y-%m-%d")

    print("Выберите в каком файле вы будете искать дату")
    # Список вариантов выбора.
    choices = ["X.csv", "По годам", "По неделям", "Из dataset.csv"]

    # Получаем выбор пользователя.
    user_choice = get_user_choice(choices)

    # Выводим выбор пользователя.
    if user_choice is not None:
        print("Вы выбрали:", user_choice)

    if user_choice == 1:
        filename = "lab_3_first_part/xset.csv"
        results = get_data_from_xset(date, filename)
        if results is None:
            print("Нет результатов поиска.")

    elif user_choice == 2:
        file_path = "lab_3_second_part/"
        results = get_data_from_year(date, file_path)
        if results is None:
            print("Нет результатов поиска.")
    
    elif user_choice == 3:
        file_path = "lab_3_third_part/"
        results = get_data_from_week(date, file_path)
        if results is None:
            print("Нет результатов поиска.")
    
    elif user_choice == 4:
        filename = "dataset.csv"
        results = get_data_from_dataset(date, filename)
        if results is None:
            print("Нет результатов поиска.")

if __name__ == "__main__":
    main()
