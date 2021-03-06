import csv
import math

# function for splitting each property
# new_file = open('training/elasticity/elasticity_poisson.csv', 'w', encoding='utf-8')
# new_file = open('training/piezo/piezo_eij.csv', 'w', encoding='utf-8')
# new_file = open('training/diel/diel_x.csv', 'w', encoding='utf-8')
# Energy
new_file = open('training/energy/energy_for.csv', 'w', encoding='utf-8')

# Elasticity
new_file = open('training/elasticity/elasticity_logG.csv', 'w', encoding='utf-8')

csv_writer = csv.writer(new_file)

# Energy
# with open('training/energy/energy.csv', 'r', encoding='utf-8') as f:

# Elasticity
with open('training/elasticity/elasticity.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        line = []
        # id
        line.append(row[0])
        # property
        line.append(row[10])

        # log G, K in elasticity
        # line.append(math.log(float(row[11]),10))

        # warning label logG and logK in elasticity
        # num = float(row[11])  # log - G, K
        # if num == 0:
        #     line.append(0)
        # elif num < 0:
        #     line.append(-math.log(abs(num)))
        # else:
        #     line.append(math.log(num))

        csv_writer.writerow(line)


