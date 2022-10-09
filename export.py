import json
import os
import csv
import openpyxl
from  openpyxl import  Workbook
from log import add_log


def get_all_contact_list(filename='contact_db.txt'):
    with open(filename, 'r', encoding='utf-8') as file:
        x = [i for i in file]
    return x


def create_dict():

    val = get_all_contact_list()

    dt_value = {}
    for i in val:
        data = i.split()
        name = data[0]
        surname = data[1]
        phone = ''.join([i for i in data[2] if i.isdigit()])
        dt_value[f'{phone}'] = [name.capitalize(), surname.capitalize()]

    return dt_value


def create_dir(dirname):
    directory = dirname
    if not os.path.exists(directory): os.makedirs(directory)


def create_json():
    create_dir('export')

    filename = f'export/export.json'
    val = create_dict()
    data = json.dumps(val)
    data = json.loads(data)

    with open(filename, 'w', encoding='windows-1251') as file:
        json.dump(data, file, indent=4)
        add_log(f'Создан файл для экспорта: {filename}', 2)
def import_csv():
    with open('export.csv', 'r', encoding='windows-1251') as file:
        for line in file:
            print(line)

def import_xlsx():
    book = openpyxl.open("export.xlsx", read_only=True)
    sheet = book.active
    data = []
    for row in range(2,sheet.max_row+1):
        numbers = sheet[row][0].value
        data.append(numbers)
        name = sheet[row][1].value
        data.append(name)
        surname = sheet[row][2].value
        data.append(surname)

    print(data)
def import_json():
    with open('export/export.json', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)

def create_csv():
    create_dir('export')
    val = get_all_contact_list()

    with open('export/export.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Номер телефона', 'Имя', 'Фамилия'])
        for i in val:
            data = i.split()
            writer.writerow(
                [data[2], data[0], data[1]]
            )


def create_xslx():
    val = get_all_contact_list()

    wb = Workbook()
    ws = wb.active

    ws.append(['Номер телефона', 'Имя', 'Фамилия'])

    for i in val:
        data = i.split()
        ws.append([data[2], data[0], data[1]])

    wb.save("export.xlsx")