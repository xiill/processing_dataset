import csv
import os

filename1 = 'transcript.txt'
filename2 = 'texts/'

filename3 = 'audio/'
filename4 = 'audio_clips/'

with open(filename1, 'r+', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter="\n")
    for row in reader:
        i = row[0]
        to_txt = i.split('/', 3)
        to_txt_1 = to_txt[1]
        to_txt_2 = to_txt_1.split('\t', 1)
        name = to_txt_2[0]
        texts = to_txt_2[1]
        texts1 = texts[:-3]
        with open(filename2 + name + '.csv', 'w+') as txt:
            txt.write(name + '|' + texts1)
            
        #audio_files_to_directories
        if not os.path.isdir(filename 4+ name):
            os.mkdir(filename4 + name)
        if os.path.exists(filename3 + name + '.wav'):
            os.replace(filename3 + name + '.wav', filename4 + name + '/' + name + '.wav')
