import sys, csv, shutil

def newline(): print()

def print_data():
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        newline()
        print("Номер телефона".center(25), "Фамилия".center(25), "Имя".center(25), "Отчество".center(25), sep=" | ", end=f'\n{"-"*(28*4)}\n')
        for row in reader:
            if not row == []:
                print(' | '.join([e.ljust(25) for e in row]), end=f'\n{"-"*(28*4)}\n')
        newline()
        file.close()

def add_data():
    newline()

    phone = input('Введите номер телефона: ')
    surname, name, third_name = input("ФИО: ").split(' ')

    with open(file_path, 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([phone, surname, name, third_name])
        newline()
        print("Данные занесены, файл сохранён")
        newline()
        file.close()

def search():
    newline()
    print('1. Полное совпадение\n2. Неполное совпадение')
    answer = int(input('Ваш выбор: '))
    newline()
    print('1. Поиск по номеру телефона\n2. Поиск по фамилии\n3. Поиск по имени\n4. Поиск по отчеству')
    answer1 = int(input('Ваш выбор: '))
    newline()
    answer2 = input('Введите значение: ')

    found_rows = []

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row == []:
                if answer == 1:
                    if row[answer1-1].upper() == answer2.upper():
                        found_rows.append(row)
                elif answer == 2:
                    if answer2.upper() in row[answer1-1].upper():
                        found_rows.append(row)

    newline()
    print("Найдено: ")
    newline()
    if not found_rows == []:
        print("Номер телефона".center(25), "Фамилия".center(25), "Имя".center(25), "Отчество".center(25), sep=" | ", end=f'\n{"-"*(28*4)}\n')
        for row in found_rows:
            print(' | '.join([e.ljust(25) for e in row]), end=f'\n{"-"*(28*4)}\n')
    else:
        print("Ничего")
    newline()

def export_data():
    newline()
    answer = input("Введите номер телефона, который нужно экспортировать: ")
    answer1 = input("Введите путь к файлу: ")
    
    with open(answer1, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        with open(file_path, 'r', encoding='utf-8') as file1:
            reader = csv.reader(file1)
            for elem in reader:
                if not elem == []:
                    if elem[0] == answer:
                        writer.writerows([['Номер телефона', 'Имя', 'Фамилия', 'Отчество'], elem])

    newline()

    print('Данные успешно экспортированы')

    newline()

def import_data():
    newline()
    print('1. Импортировать с перезаписью\n2. Добавить')
    answer = int(input('Ваш выбор: '))
    answer1 = input('Введите путь к файлу: ')

    with open(answer1, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        if answer == 1:
            with open(file_path, 'w', encoding='utf-8') as file1:
                writer = csv.writer(file1)
                writer.writerows(list(reader))
                file1.close()
        elif answer == 2:
            with open(file_path, 'a', encoding='utf-8') as file1:
                writer = csv.writer(file1)
                writer.writerows(list(reader))
                file1.close()
        file.close()

    newline()
    print('Данные импортированы')
    newline()

def choice_dialogue():
    print('1. Вывести справочник\n2. Добавить данные\n3. Поиск\n4. Экспорт\n5. Импорт\n6. Выход')

    answer = int(input("Ваш выбор: "))

    if answer == 1:
        print_data()
    elif answer == 2:
        add_data()
    elif answer == 3:
        search()
    elif answer == 4:
        export_data()
    elif answer == 5:
        import_data()
    elif answer == 6:
        sys.exit(0)
    else:
        print("Неизвестное число")

if __name__ == "__main__":

    file_path = input("Введите путь к файлу: ")
    newline()

    print('Телефонный справочник'.center(28*4))
    newline()

    while True:
        choice_dialogue()