import notepad_actions as na
import making_note as mn


def run():
    input_from_user = ''
    while input_from_user != '7':
        mn.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            na.show('all')
        if input_from_user == '2':
            na.add()
        if input_from_user == '3':
            na.show('all')
            na.id_edit_del_show('del')
        if input_from_user == '4':
            na.show('all')
            na.id_edit_del_show('edit')
        if input_from_user == '5':
            na.show('date')
        if input_from_user == '6':
            na.show('id')
            na.id_edit_del_show('show')
        if input_from_user == '7':
            mn.goodbuy()
            break