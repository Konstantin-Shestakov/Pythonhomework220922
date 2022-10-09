from model import Contact
from log import add_log, get_log
from export import create_json, create_csv, create_xslx, import_csv, import_json, import_xlsx


def create_contact():
    print('введите данные нового контакта')
    name, surname, cell_number = input('Введите ваше имя: '), input('Введите фамилию: '), input('Введите номер телефона: ')

    new_contact = Contact()
    flag = True

    while flag:
        new_contact.name = name
        new_contact.surname = surname
        new_contact.cell_number = cell_number
        data = new_contact.get_correct_number()
        flag = data[0]
        new_contact.cell_number = data[1]

    data_contact = new_contact.get_contact_value()
    # logging data
    add_log(data_contact)
    # Write data
    with open('contact_db.txt', 'a+', encoding='utf-8') as db:
        db.write(f'{" ".join(data_contact)} \n')


def export_contact(mode):
    if mode == '1':
        create_json()
    elif mode == '2':
        create_csv()
    elif mode == '3':
        create_xslx()
    elif mode == '4':
        pass

def import_contact(mode):
    if mode == '1':
        import_json()
    elif mode == '2':
        import_csv()
    elif mode == '3':
        import_xlsx()
    elif mode == '4':
        pass


def get_dict(filename='contact_db.txt'):

    with open(filename, 'r', encoding='utf-8') as file:
        x = [i for i in file]

    dt_value = {}
    for i in x:
        data = i.split()
        name = data[0]
        surname = data[1]
        phone = ''.join([i for i in data[2] if i.isdigit()])
        dt_value[f'{phone}'] = [name.capitalize(), surname.capitalize()]

    return dt_value


def find_name():
    number = input('Введите желаемый номер телефона: ')
    value = get_dict()
    if len(number) == 10:
        result = value.get('7'+number)
    else:
        result = value.get(number)
    add_log(f'Выполнен поиск контакта по запросу - {number}|  {result[0]} {result[1]}',2)
    if result:
        print(f"_____Контакт_____\n{result[0].capitalize()} {result[1].capitalize()}\n_________________")
    else:
        print('Ничего не найдено!')


def mode(select):
    flag = True
    while flag:
        if select == '1':
            create_contact()
            flag = False
        elif select == '2':
            print('Форматы выгрузки: \n'
                  '1) JSON\n'
                  '2) CSV\n'
                  '3) XLSX\n'
                  '4) TXT\n')
            sub_select = input('В каком формате желаете выгрузить контакты ?')
            export_contact(sub_select)
            flag = False
        elif select == '3':
            print('Форматы загрузки: \n'
                  '1) JSON\n'
                  '2) CSV\n'
                  '3) XLSX\n'
                  '4) TXT\n')
            sub_select = input('В каком формате желаете загрузить контакты ?')
            import_contact(sub_select)
            flag = False
        elif select == '4':
            print(*get_log())
            flag = False
        elif select == '5':
            find_name()
            flag = False
        else:
            print('такой команды нет, выбирите команду от 1 до 4')
            flag = False


def start():
    print('---------------Телефонный справочник---------------')
    print('Программа может: \n'
          '1) Добавлять новые контакты\n'
          '2) Выгружать контакты в формате txt, json, csv, xlsx\n'
          '3) Импорт контактов из txt, json, csv, xlsx\n'
          '4) Посмотреть все логи\n'
          '5) Найти аббонента\n')

    select_mode = input('Что вы желате сделать (1 добавить / 2 export / 3 import / 4 посмотреть логи / 5 Поиск)? ввод: ')
    mode(select_mode)

   
    print('-----Выражаю свою благодарность команде этого справочника--Komlevskiy Pavel /  Alexey Sidorkin / Obzherin Danila / Evgeniy ---------------')