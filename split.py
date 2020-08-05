import csv
import math

# function for splitting each property
new_file = open('training/elasticity/elasticity_poisson.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(new_file)

with open('training/elasticity/elasticity.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        line = []
        line.append(row[0]) # id
        line.append(row[13]) # property
        # line.append(math.log(float(row[11])))  # log - G, K
        csv_writer.writerow(line)
