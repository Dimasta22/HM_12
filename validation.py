import calendar


def sanitize_phone(number: str) -> str:
    output = (number
              .strip()
              .replace('+', '')
              .replace('(', '')
              .replace(')', '')
              .replace('-', '')
              .replace(' ', ''))

    return output[: 12]


def sanitize_birthday(birthday: str):
    day, month, year = birthday.split('.')
    if int(month) in list(range(1, 13)) and int(year) >= 0 and int(day) in list(range(1, calendar.monthrange(int(year), int(month))[1] + 1)):
        return True
    return False


if __name__ == '__main__':
    print(sanitize_phone(' +38(0 67 )- 544-98 -98 111 '))
    print(sanitize_birthday('31.01.2000'))