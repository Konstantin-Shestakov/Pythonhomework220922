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