import notepad as np


def create_note(number):
    title = check_len_text_input(
        input('Название заметки: '), number)
    body = check_len_text_input(
        input('Тема: '), number)
    return np.Note(title=title, body=body)


def menu():
    print("\nДля работы с заметками выберите функцию:\n\n1 - вывод всех заметок\
          \n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\
          \n5 - выборка заметок по дате\n6 - вывести заметку по id\n7 - выход \
          \n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен превышать {n} символов\n')
        text = input('Текст заметки: ')
    else:
        return text


def goodbuy():
    print("Работа программы прекращена.")