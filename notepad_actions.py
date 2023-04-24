import file_interaction as fi
import notepad as np
import making_note as mn

number = 3  # минимальное количество знаков в тексте заметки


def add():
    note = mn.create_note(number)
    array = fi.read_file()
    for notes in array:
        if np.Note.get_id(note) == np.Note.get_id(notes):
            np.Note.set_id(note)
    array.append(note)
    fi.write_file(array, 'a')
    print('Заметка добавлена')


def show(text):
    logic = True
    array = fi.read_file()
    if text == 'date':
        date = input('Введите дату в формате дд.мм.гггг: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(np.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + np.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in np.Note.get_date(notes):
                print(np.Note.map_note(notes))
    if logic == True:
        print('Заметки отсутствуют')


def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = fi.read_file()
    logic = True
    for notes in array:
        if id == np.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = mn.create_note(number)
                np.Note.set_title(notes, note.get_title())
                np.Note.set_body(notes, note.get_body())
                np.Note.set_date(notes)
                print('Заметка изменена')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена')
            if text == 'show':
                print(np.Note.map_note(notes))
    if logic == True:
        print('Заметка отсутствует, введен неверный id')
    fi.write_file(array, 'a')