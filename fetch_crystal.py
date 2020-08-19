from pymatgen import MPRester
from pymatgen.io.cif import CifWriter
import numpy as np
import csv
import os
import math

# Fetch elasticity properties from Material Project
if __name__ == '__main__':
    MAPI_KEY = 'h9GBsMfA1JvXbC7n'  # You must change this to your Materials API key! (or set MAPI_KEY env variable)
    QUERY = 'mp-1180346'  # change this to the mp-id of your compound of interest

    mpr = MPRester(MAPI_KEY)  # object for connecting to MP Rest interface

    # All 89 elements in MP
    element_list = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                    'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br',
                    'Kr',
                    'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I',
                    'Xe',
                    'Cs', 'Ba', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi',
                    'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
                    'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu']
    # data = mpr.query(criteria={'material_id': 'mp-1'},
    #                  properties=['material_id',
    #                              'elements',
    #                              'spacegroup'])

    data = mpr.query(criteria={'elements': {'$in': element_list},
                               'has_bandstructure': True,
                               },
                     properties=['material_id',
                                 'elements',
                                 'spacegroup'])

    element = {}
    cry = {}
    group = {}
    num = {}
    h = {}
    new_file = open('training/basic/basic.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(new_file)
    for i in data:
        row = []
        material_id = i['material_id']
        row.append(material_id)
        spacegroup = i['spacegroup']

        crystal_system = spacegroup['crystal_system']
        cry[crystal_system] = cry.get(crystal_system, 0) + 1
        row.append(crystal_system)

        point_group = spacegroup['point_group']
        group[point_group] = group.get(point_group, 0) + 1
        row.append(point_group)

        number = spacegroup['number']
        num[number] = num.get(number, 0) + 1

        hall = spacegroup['hall']
        h[hall] = h.get(hall,0) + 1



        elements = i['elements']
        for ele in elements:
            element[ele] = element.get(ele, 0) + 1
            row.append(ele)
        # save csv files
        csv_writer.writerow(row)

    print('Total element')
    print(len(element))
    print(element)

    print('Crystal System')
    print(len(cry))
    print(cry)

    print('Point group')
    print(len(group))
    print(group)

    print('Number')
    print(len(num))
    print(num)

    print('Hall')
    print(len(h))
    print(h)