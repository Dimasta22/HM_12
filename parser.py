import re


ACTION_LIST = [
    'HELLO',
    'ADD',
    'CHANGE',
    'PHONE',
    'SHOW ALL',
    'SHOW DAYS',
    'DAYS',
    'DATA',
    'SEARCH',
    'GOOD BYE',
    'CLOSE',
    'EXIT'
]

ACTION_LIST_FOR_CHANGE_COMMAND = [
    'CHANGE',
    'ADD',
    'DELETE'
]


def parser(sentence):
    sentence = sentence.upper().strip()
    for key in ACTION_LIST:
        func = re.search(fr'^{key}\b', sentence)
        if func is not None:
            return func.group()


def change_parser(sentence: str):
    sentence = sentence.upper().strip().split(' ')
    sentence = ' '.join(sentence[1:])
    for key in ACTION_LIST_FOR_CHANGE_COMMAND:
        func = re.search(fr'^{key}\b', sentence)
        if func is not None:
            return func.group()


if __name__ == '__main__':
    sen = 'change delete Dima 167 050 789 87joi odi'
    print(change_parser(sen))

