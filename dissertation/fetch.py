# Fetch all elasticity, piezo and diel properties from Material Project
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

    # search_key in material project, including elasticity, piezo and diel
    search_key = 'elasticity'

    data = mpr.query(criteria={'elements': {'$in': element_list},
                               'has_bandstructure': True,
                               search_key: {'$exists': True},
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
                                 'structure',
                                 search_key])

    if search_key == 'elasticity':
        new_file = open('./training/' + search_key + '/' + search_key + '.csv', 'w', encoding='utf-8')
        csv_writer = csv.writer(new_file)
        new_file_warnings = open('./training/elasticity/elasticity_warnings.csv', 'w', encoding='utf-8')
        csv_writer_warnings = csv.writer(new_file_warnings)
    else:
        new_file = open('./training/' + search_key + '/' + search_key + '.csv', 'w', encoding='utf-8')
        csv_writer = csv.writer(new_file)


    # 10666 with elasticity and 3948 with warnings label, 6718 without warnings label
    # 2791 with piezo
    # 5796 with diel

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
        # save cif and csv files
        c = CifWriter(i['structure'])

        # add G_Voigt_Reuss_Hill, K_Voigt_Reuss_Hill, elastic_anisotropy, poisson_ratio
        if search_key == 'elasticity':
            elasticity = i['elasticity']
            row.append(elasticity['G_Voigt_Reuss_Hill'])
            row.append(elasticity['K_Voigt_Reuss_Hill'])
            row.append(elasticity['elastic_anisotropy'])
            row.append(elasticity['poisson_ratio'])
            cif_file = './training/elasticity/data/' + material_id + '.cif'
            c.write_file(cif_file)
            csv_writer_warnings.writerow(row)
            if elasticity['warnings']:
                continue
            else:
                csv_writer.writerow(row)

        # add eij_max
        elif search_key == 'piezo':
            piezo = i['piezo']
            row.append(piezo['eij_max'])

        # add n - dielectric constant, poly_electronic - refractive index, poly_total - ferroelectricity
        elif search_key == 'diel':
            diel = i['diel']
            row.append(diel['n'])
            row.append(diel['poly_electronic'])
            row.append(diel['poly_total'])

        cif_file = './training/' + search_key + '/data/' + material_id + '.cif'
        c.write_file(cif_file)
        csv_writer.writerow(row)
