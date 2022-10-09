from datetime import datetime as dt


def add_log(data, mode=1):
    with open('log.txt', 'a+', encoding='utf-8') as file:
        time = dt.now()
        if mode == 1:
            file.write(f'{" / ".join(data)} / запись добавлена: {time} \n')
        else:
            file.write(f'{data} / запись добавлена: {time} \n')


def get_log():
    with open('log.txt', 'r', encoding='utf-8') as file:
        data_set = [i for i in file]

    return data_set


