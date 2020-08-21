# The aim of this file is to find * in each epoch to fetch MAE, RMSE, R2
import csv

new_file = open('training/basic/100cycle/total_data.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(new_file)

with open('training/basic/100cycle/raw3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for row in lines:
        if '*' in row:
            line = []
            one = row.split(' ')
            for word in one:
                if '\t' in word:
                    two = word.split('\t')
                    line.append(two[0])
                elif '\n' in word:
                    word = word.replace('\n','')
                    line.append(word)
            csv_writer.writerow(line)