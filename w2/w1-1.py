import csv
#with open('data01.csv', newline='') as csvfile:
with open('data01.csv',newline='',encoding='utf8') as csvfile:
    readFile = csv.reader(csvfile)
    for row in readFile:
        print(row)
input()