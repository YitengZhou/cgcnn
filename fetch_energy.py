# Fetch all energy properties from Material Project, including formation, absolute, band_gap and efermi
from pymatgen import MPRester
from pymatgen.io.cif import CifWriter
import csv

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

    data = mpr.query(criteria={'elements': {'$in': element_list},
                               'has_bandstructure': True,
                               },
                     properties=['material_id',
                                 'pretty_formula',
                                 'nelements',
                                 'nsites',
                                 'is_hubbard',
                                 'is_compatible',
                                 'volume',
                                 'density',
                                 'energy_per_atom',
                                 'formation_energy_per_atom',
                                 'band_gap',
                                 'efermi'
                                 ])
    print(len(data))
    print(data)
    new_file = open('training/energy/energy.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(new_file)
    for i in data:
        row = []
        material_id = i['material_id']
        row.append(material_id)
        row.append(i['pretty_formula'])
        row.append(i['nelements'])
        row.append(i['nsites'])
        row.append(i['is_hubbard'])
        row.append(i['is_compatible'])
        row.append(i['volume'])
        row.append(i['density'])
        row.append(i['energy_per_atom'])
        row.append(i['formation_energy_per_atom'])

        # save cif and energy properties csv files
        c = CifWriter(i['structure'])
        cif_file = './training/energy/data/' + material_id + '.cif'
        c.write_file(cif_file)
        row.append(i['formation_energy_per_atom'])
        row.append(i['energy_per_atom'])
        row.append(i['band_gap'])
        row.append(i['efermi'])
        csv_writer.writerow(row)

