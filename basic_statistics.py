import csv

# Calculate the proportion of Four types of datasets - energy, piezo, elasticity, diel
# Energy
energy = []
with open('training/energy/energy.csv', 'r', encoding='utf-8') as en:
    reader = csv.reader(en)
    for row in reader:
        energy.append(row[0])
    print(len(energy))

# elasticity
elasticity = []
with open('training/elasticity/elasticity.csv', 'r', encoding='utf-8') as el:
    reader = csv.reader(el)
    for row in reader:
        elasticity.append(row[0])
    print(len(elasticity))

# diel
diel = []
with open('training/diel/diel.csv', 'r', encoding='utf-8') as di:
    reader = csv.reader(di)
    for row in reader:
        diel.append(row[0])
    print(len(diel))

# piezo
piezo = []
with open('training/piezo/piezo.csv', 'r', encoding='utf-8') as pi:
    reader = csv.reader(pi)
    for row in reader:
        piezo.append(row[0])
    print(len(piezo))

# energy & elasticity
intersection = list(set(energy).intersection(set(elasticity)))
print('energy & elasticity')
print(len(intersection))
# energy & diel
intersection = list(set(energy).intersection(set(diel)))
print('energy & diel')
print(len(intersection))
# energy & piezo
intersection = list(set(energy).intersection(set(piezo)))
print('energy & piezo')
print(len(intersection))
# elasticity & diel
intersection = list(set(elasticity).intersection(set(diel)))
print('elasticity & diel')
print(len(intersection))
# elasticity & piezo
intersection = list(set(elasticity).intersection(set(piezo)))
print('elasticity & piezo')
print(len(intersection))
# diel & piezo
intersection = list(set(diel).intersection(set(piezo)))
print('diel & piezo')
print(len(intersection))
# diel & piezo & elasticity
intersection = list(set(diel).intersection(set(piezo).intersection(set(elasticity))))
print('diel & piezo & elasticity')
print(len(intersection))

# nelement and nsite
ne = {}
ns = {}
with open('training/energy/energy.csv', 'r', encoding='utf-8') as en:
    reader = csv.reader(en)
    for row in reader:
        nelement = str(row[2])
        ne[nelement] = ne.get(nelement, 0) + 1
        nsite = row[3]
        ns[nsite] = ns.get(nsite, 0) + 1
    print('nelement')
    print(len(ne))
    print(ne)
    print('nsite')
    print(len(ns))
    print(ns)


