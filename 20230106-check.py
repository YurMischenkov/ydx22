import csv

with open('wares.csv', newline='') as csvfile:
    r = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(r):
        if index == 0: 
            continue
        if int(row[2]) < int(row[1]):
            print(row[0])


