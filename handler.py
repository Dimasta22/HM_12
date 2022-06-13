from parser import parser, change_parser
from input_error import input_error
from add_class import Record, Name, Phone, Birthday

#data_base = [{'name': 'Dima', 'phone': ['064', '050'], 'birthday': '22.01.2000'},
             #{'name': 'Jeka', 'phone': ['033'], 'birthday': '16.01.1985'}]


@input_error
def handler(sentence: str, data_base=[]):
    def all_function(sentence: str):

        if parser(sentence) == 'HELLO':
            return "How can I help you?"

        elif parser(sentence) == 'SHOW ALL':
            output = ''
            for contact in data_base:
                output += f'{contact["name"]}, {contact["phone"]}, {contact["birthday"]};\n'
            return output[:-2]

        elif parser(sentence) in ['EXIT', 'CLOSE', 'GOOD BYE']:
            # Тут будет запись файла
            return False

        elif parser(sentence) is None:
            return 'Введите команду из списка доступных команд!'

        elif parser(sentence) == 'DAYS':
            _, name, *args = sentence.split(' ')
            for contact in data_base:
                if contact.get('name') == name and contact.get('birthday') is not None:
                    record = Record(Name(name), Phone(' '), Birthday(contact.get('birthday')))
                    return record.days_to_birthday()
            return 'ДР не задан или такого человека нет!!!'

        elif parser(sentence) == 'ADD':
            _, name, *args = sentence.split(' ')
            if len(args) == 1:
                number = args[0]
                record = Record(Name(name), Phone(number))
            elif len(args) >= 2:
                number, date = args[0], args[1]
                record = Record(Name(name), Phone(number), Birthday(date))
            else:
                record = Record(Name(name))
            for contact in data_base:
                if contact.get('name') == name:
                    return 'Такой пользователь уже есть'
            record.add_rec()
            data_base.append({'name': record.name, 'phone': record.phones, 'birthday': record.birthday})
            return 'Операция прошла успешно'

        elif parser(sentence) == 'PHONE':
            _, name, *args = sentence.split(' ')
            for contact in data_base:
                if contact.get('name') == name:
                    return contact.get('phone', 'Такого пользователья нет')

        elif parser(sentence) == 'CHANGE':
            if change_parser(sentence) == 'CHANGE':
                _, _, name, old_number, new_number, *args = sentence.split(' ')
                for contact in data_base:
                    if contact.get('name') == name:
                        record = Record(Name(name))
                        for number in contact['phone']:
                            record.add_rec(Phone(number))
                        record.change_rec(Phone(old_number), Phone(new_number))
                        contact['phone'] = record.phones
                        return 'Операция прошла успешно'
                else:
                    return 'Такого пользователя нет или старый номер не совпадает с введенным номером'

            elif change_parser(sentence) == 'ADD':
                _, _, name, new_number, *args = sentence.split(' ')
                for contact in data_base:
                    print(contact)
                    if contact.get('name') == name:
                        record = Record(Name(name))
                        for number in contact['phone']:
                            record.add_rec(Phone(number))
                        record.add_rec(Phone(new_number))
                        contact['phone'] = record.phones
                        return 'Операция прошла успешно'
                else:
                    return 'Такого пользователя нет'

            elif change_parser(sentence) == 'DELETE':
                _, _, name, old_number, *args = sentence.split(' ')
                for contact in data_base:
                    if contact.get('name') == name:
                        record = Record(Name(name))
                        for number in contact['phone']:
                            record.add_rec(Phone(number))
                        record.del_rec(Phone(old_number))
                        contact['phone'] = record.phones
                        return 'Операция прошла успешно'
                else:
                    return 'Такого пользователя нет'

            elif change_parser(sentence) is None:
                return 'Введите подкоманду из списка доступных команд!'
            else:
                raise ValueError

        elif parser(sentence) is None:
            return 'Введите команду из списка доступных команд!'
        else:
            return 'Не понятно_2'

        return 'Операция прошла успешно'
    return all_function(sentence)


if __name__ == '__main__':

    while True:
        command = input('Введите название комманды и параметры: ')
        print(handler(command))
        if parser(command) in ['EXIT', 'CLOSE', 'GOOD BYE']:
            print('До новых встреч')
            break






'''
    sen = 'show all'
    print(handler(sen))

    sen = 'add Yuri 050 22.05.1980'
    print(handler(sen))

    sen = 'show all'
    print(handler(sen))

    sen = 'change add Yuri 088 22.05.1980'
    print(handler(sen))

    sen = 'show all'
    print(handler(sen))

    sen = 'change add Dima 089 22.05.1980'
    print(handler(sen))

    sen = 'show all'
    print(handler(sen))

    sen = 'change add Dima 08-+)8 22.05.1980'
    print(handler(sen))

    print(data_base)
'''



