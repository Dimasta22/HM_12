def input_error(func):
    def inner(sentence: str):
        try:
            result = func(sentence)
            return result
        except ValueError:
            return 'Введите все параметры'
        except KeyError:
            return 'Такого пользователя нет'
        except IndexError:
            return 'Превышен размер словаря'
    return inner

