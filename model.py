class Contact:
    def __int__(self, name='Noname', surname='Nosurname', cell_number='0 (000) 0000000'):
        self.name = name
        self.surname = surname
        self.cell_number = cell_number

    def __str__(self):
        return self.cell_number

    def get_correct_number(self):
        number_lst = [i for i in self.cell_number if i.isdigit()]

        res = "+"
        if len(self.cell_number) == 11:
            if number_lst[0] == '8':
                res += '7('
                count = 0
                for i in range(1, len(number_lst)):
                    count += 1
                    if count == 4:
                        res += f'){number_lst[i]}'
                    else:
                        res += number_lst[i]
            return False, res
        elif len(self.cell_number) == 10:
            res += '7('
            count = 0
            for i in range(len(number_lst)):
                count += 1
                if count == 4:
                    res += f'){number_lst[i]}'
                else:
                    res += number_lst[i]
            return False, res
        else:
            print('Номер телефона не корректен')
            

    def get_contact_value(self):
        return [self.name, self.surname, self.cell_number]
