"""Создание файлов csv, содержащие название файлов, разделитель и текст"""

import csv

filename1 = 'C:/Users/tansa/Desktop/DataSet/metadata.csv'
filename2 = 'C:/Users/tansa/Desktop/DataSet/texts/'
"""Формат файла"""
filename3 = '.csv'
"""Разделитель"""
filename4 = '|'

with open(filename1, 'r', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter="\n")
    for row in reader:
        i = row[0]
        to_txt = i.split('|', 3)
        with open(filename2 + to_txt[0] + filename3, 'w') as txt:
            """Название разделить содержание"""
            txt.write(to_txt[0] + filename4 + to_txt[1])
