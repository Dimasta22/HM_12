from handler import handler
from parser import parser
from add_class import AddressBook


def main():
    print('Вас приветствует Бот-помощник')
    print('Комманды доступные Вам: hello, add, change, phone, show all, days, exit, good bye, close')
    print('Полная запись: комманда, параметры(имя, телефон, дата рождения в стиле 31.12.2000)')
    print('Команда пишеться через пробел')
    print('Параметры add: Имя телефон*, дата рождения*')
    print('Параметры change: Доп. параметр(change, delete, add),'
          ' Имя, старий телефон, новый телефон')
    print('* - не обязательно к заполнению')
    print('Параметр phone: Имя')
    print('Параметр days: Имя')
    print('Параметр Date (Загружает предыдущие данные)')
    print('Параметр Search: name (Ищет совпадения)')

    while True:
        command = input('Введите название комманды и параметры: ')
        if parser(command) in ['EXIT', 'CLOSE', 'GOOD BYE']:
            file = 'data_base.bin'
            data = handler(command)
            for record in data:
                AddressBook(record).save_in_file(file)
            #AddressBook(data).save_in_file(file)
            print('До новых встреч')
            break
        print(handler(command))


if __name__ == '__main__':
    main()


