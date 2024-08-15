import random

def menu():
    print('1. создать папку')
    print('2. удалить папку')
    print('3. копировать папку')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')



def bank_acount(bank_account, history_purchase):
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = int(input('Выберите пункт меню банковскх операций '))
        if choice == 1:
            print(f'На счету {bank_account} рублей')
            sum_input = int(input('Введите сумму: '))
            bank_account += sum_input
            print(bank_account)
        elif choice == 2:
            purchase_price = int(input('Введите сумму покупки: '))
            if purchase_price > bank_account:
                print('Денег на покупку не хватает')
            else:
                bank_account -= purchase_price
                purchase_name = input('Введите наименование покупки: ')
                purchase = {'purchase_name': purchase_name, 'purchase_price': purchase_price}
                history_purchase.append(purchase)
                print(history_purchase)
        elif choice == 3:
            for hist in history_purchase[:]:
                print(hist)
        elif choice == 4:
            break
        else:
            print('Неверный пункт меню')


def quiz(num_choise=2):
    famouse_people = {'Мария Шарапова': '19.04.1987',
                  'Александр Овечкин': '17.09.1985',
                  'Никита Михалков': '21.10.1941',
                  'Ксения Собчак': '05.11.1981',
                  'Валерий Гергиев': '02.05.1953',
                  'Татьяна Навка': '13.04.1975',
                  'Артём Дзюба': '22.08.1988',
                  'Иван Ургант': '16.04.1978',
                  'Павел Дуров': '10.10.1984',
                  'Федор Конюхов': '12.12.1951'}

    months = {'01': 'января',
              '02': 'февраля',
              '03': 'марта',
              '04': 'апреля',
              '05': 'мая',
              '06': 'июня',
              '07': 'июля',
              '08': 'августа',
              '09': 'сентября',
              '10': 'октября',
              '11': 'ноября',
              '12': 'декабря'
    }

    days = {'01': 'первое',
            '02': 'втрое',
            '03': 'третье',
            '04': 'четвертое',
            '05': 'пятое',
            '10': 'десятое',
            '12': 'двенадцатое',
            '13': 'тринадцатое',
            '16': 'шестнадцатое',
            '17': 'семнадцатое',
            '19': 'девятнадцатое',
            '21': 'двадцать первое',
            '22': 'двадцать втрое'
    }

    choise = random.sample(list(range(1,11)), num_choise)

    while True:
        count_true = 0
        for i in choise:
            question = input(f'Введите дату рождения {list(famouse_people.keys())[i]}: ')
            if question == list(famouse_people.values())[i]:
                print('Ответ верный')
                count_true += 1
            else:
                day, month, year = list(famouse_people.values())[i].split('.')
                print('Правильный ответ: ', days[day], months[month], year)
        print('Количество верных ответов:', count_true)
        print('Количество ошибок:', num_choise - count_true)
        game_continue = input('Хотите начать игру сначала? ')
        if not game_continue == 'да'.lower():
            break

    print('Игра окончена.')

