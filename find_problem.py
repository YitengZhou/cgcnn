import csv

with open('training/energy/energy_efe.csv', 'r', encoding='utf-8') as en:
    reader = csv.reader(en)
    for row in reader:
        print(row[0])
        print(row[1])
        float(row[1])
