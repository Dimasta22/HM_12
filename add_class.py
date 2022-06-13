from collections import UserDict
from datetime import datetime
import calendar
import pickle
import re


class Field:
    pass


class Name(Field):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Phone(Field):
    def __init__(self, phone: str):
        self.__phone = None
        self.phone = phone

    def __str__(self):
        return self.__phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        self.__phone = (value.strip()
                        .replace('+', '')
                        .replace('(', '')
                        .replace(')', '')
                        .replace('-', '')
                        .replace(' ', ''))[: 12]


class Birthday(Field):
    def __init__(self, birthday: str):
        self.__birthday = None
        self.birthday = birthday

    def __str__(self):
        return self.__birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value: str):
        try:
            day, month, year = value.split('.')
            if int(month) in list(range(1, 13)) and int(year) >= 0 and int(day) in \
                    list(range(1, calendar.monthrange(int(year), int(month))[1] + 1)):
                self.__birthday = value
            else:
                pass
        except:
            pass


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name.name
        self.phones = []
        if phone:
            self.phones.append(phone.phone)
        self.birthday = None
        if birthday:
            self.birthday = birthday.birthday

    def __str__(self):
        return f'{self.name}, {self.phones}, {self.birthday}'

    def add_rec(self, addit_phone: Phone = None):
        add_to_dict = AddressBook({self.name: self.phones})
        add_to_dict.add_record(addit_phone, self.birthday, self.name)
        return add_to_dict

    def change_rec(self, pre_phone: Phone, post_phone: Phone):
        change_in_dict = AddressBook({self.name: self.phones})
        change_in_dict.change_record(pre_phone, post_phone)
        return change_in_dict

    def del_rec(self, delete_phone: Phone):
        del_in_dict = AddressBook({self.name: self.phones})
        del_in_dict.del_record(delete_phone)
        return del_in_dict

    def days_to_birthday(self):
        if self.birthday is not None:
            today_date = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
            day, month, year = self.birthday.split('.')
            birthday_date = datetime(year=datetime.now().year, month=int(month), day=int(day))
            if today_date.month > birthday_date.month:
                birthday_date = datetime(year=datetime.now().year + 1, month=int(month), day=int(day))
                if today_date.day >= birthday_date.day:
                    birthday_date = datetime(year=datetime.now().year + 1, month=int(month), day=int(day))
            return birthday_date - today_date
        else:
            return 'Дата не задана'


class AddressBook(UserDict):
    base_data = []

    def add_record(self, add_phone: Phone = None, birthday_date: Birthday = None, key_name: Name = None):
        if add_phone is None:
            self.data.update()
        else:
            [self.data[key].append(add_phone.phone) for key in self.data.keys()]

        for contact in self.base_data:
            if contact.get('name') == key_name:
                self.base_data.remove(contact)
        self.base_data.append({'name': key_name, 'phone': self.data[key_name], 'birthday': birthday_date})
        #print(key_name)

    def change_record(self, previous_phone: Phone, future_phone: Phone):
        for key, value in self.data.items():
            for num_index in range(len(value)):
                if value[num_index] == previous_phone.phone:
                    value[num_index] = future_phone.phone
        #self.base_data.append(self.data)

    def del_record(self, del_phone: Phone):
        for key, value in self.data.items():
            value.remove(del_phone.phone)

    def save_in_file(self, file_name):
        with open(file_name, "wb") as fh:
            pickle.dump(self.base_data, fh)

    def search_something(self):
        print(self.base_data)

    def __iter__(self):
        return GetAddressBook(self.data, 3)


class GetAddressBook:
    def __init__(self, input_dict: dict, number_of_iter: int):
        self.input_dict = input_dict
        self.number_of_iter = number_of_iter
        self.current_value = 0

    def __next__(self):
        if self.current_value < len(self.input_dict):
            output_dict = self.input_dict[self.current_value: self.current_value + self.number_of_iter]
            self.current_value += self.number_of_iter
            return output_dict
        raise StopIteration


if __name__ == '__main__':
    person_name = Name('Jeka')
    person_phone = Phone('259+++8')
    person_1 = Record(person_name, person_phone)
    print(person_1)

    print(person_1.add_rec(Phone('1122')))
    print(person_1.change_rec(Phone('2598'), Phone('3300')))
    print(person_1.del_rec(Phone('3300')))

    print(person_1.phones)
    print(person_1.add_rec())

    person_2 = Record(Name('Dima'), Phone('067---8'), Birthday('22.01.2000'))
    print(person_2.add_rec())

    person_3 = Record(Name('Misha'), Phone('+38045(8'), Birthday('28.06.2014'))
    print(person_3.days_to_birthday())
    print(person_3.add_rec())
    print(person_3.add_rec(Phone('8956')))
    #print(AddressBook.base_data)

    print(AddressBook.base_data)
    AddressBook(AddressBook.base_data[0]).save_in_file('data_base.bin')

    #print(AddressBook.search_something())
    '''
    print(person_1.add_rec(Phone('2222')))
    print(person_1.phones)
    print(person_1.change_rec(Phone('2598'), Phone('3300')))
    print(person_1.del_rec(Phone('2222')))

    person_2 = Record(Name('Dima'), Phone('067---8'), Birthday('22.01.2000'))
    print(person_2.add_rec())

    print(str(person_2.phones))
    print(str(person_1.phones))
    print(person_2.days_to_birthday())

    person_3 = Record(Name('Dima'), Phone('067---8'), Birthday('28.06.2074'))
    print(person_3.days_to_birthday())
    print(AddressBook.base_data)
    '''

