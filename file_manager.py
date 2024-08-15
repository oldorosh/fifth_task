import os
import shutil
import function_used as fu

while True:
    anw = input('Вывести меню? ')
    if anw == 'да'.lower() or anw == 'yes'.lower():
        fu.menu()
    else:
        break
    choice = int(input('Выберите пункт меню '))
    if choice == 1:
        name_folder = input('Введите название папки: ')
        if not os.path.exists(name_folder):
            os.mkdir(name_folder)
    elif choice == 2:
        name_remove_folder = input('Введите название папки для удаления: ')
        os.rmdir(name_remove_folder)
    elif choice == 3:
        name_file = input('введите имя файла (папки) для копирования ')
        copy_file = input('Введите новое имя файла ')
        shutil.copy(name_file, copy_file)
    elif choice == 4:
        print(os.listdir())
    elif choice == 5:
        contents = os.listdir()
        folders = [folder for folder in contents if os.path.isdir(folder)]
        for folder in folders:
            print(folder)
    elif choice == 6:
        contents = os.listdir()
        files = [file for file in contents if os.path.isfile(file)]
        for file in files:
            print(file)
    elif choice == 7:
        print(os.name)
        print(os.environ)
    elif choice == 8:
        print('Olga Doroshenko')
    elif choice == 11:
        path = input('Введите путь к каталогу, который нужно сделать текущим рабочим каталогом: ')
        os.chdir(path)
        print(os.getcwd())
    elif choice == 10:
        bank_account = 0
        history_purchase = []
        fu.bank_acount(bank_account, history_purchase)
    elif choice == 9:
        fu.quiz(num_choise=3)
    elif choice == 12:
        break
    else:
        print('Неверный пункт меню')
