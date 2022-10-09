

def import_contact():
    with open('contact_db.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            print(line)

