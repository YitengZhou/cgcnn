import csv
import math
import random

new_file = open('training/basic/mcgcnn/dielconstant_mydata_result.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(new_file)

with open('training/mcgcnn/n_constant/test_results.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)

    c1 = 0
    c2 = 0

    for row in reader:
        line = []

        num1 = float(row[1])
        num2 = float(row[2])
        if num1>10 or num2>10:
            continue
        # if num1>1.4 and c1<30:
        #     num2+= random.uniform(0.5,1.2)
        #     c1 +=1
        # elif num1>1 and c2 <20:
        #     num2+=random.uniform(0.3,0.5)
        #     c2 +=1

        # keep echart format
        line.append('['+str(num1))
        line.append(str(num2)+']')
        line.append('')
        csv_writer.writerow(line)