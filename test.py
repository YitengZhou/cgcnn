from pymatgen import MPRester
from pymatgen.io.cif import CifWriter
import csv
import os
import json
import math

if __name__ == "__main__":
    MAPI_KEY = "aT5BgxSEFI3bAcZ8"  # You must change this to your Materials API key! (or set MAPI_KEY env variable)
    QUERY = "mp-1180346"  # change this to the mp-id of your compound of interest
    # QUERY = "TiO"  # change this to a formula of interest
    # QUERY = "Ti-O"  # change this to a chemical system of interest

    mpr = MPRester(MAPI_KEY)  # object for connecting to MP Rest interface

    # all information 2+2 warning label
    result = mpr.get_data("mp-9272")
    print(result)
    print()
    result = mpr.get_data("mp-571420")
    print(result)
    print()

    result = mpr.get_data("mp-1094115")
    print(result)
    print()
    result = mpr.get_data("mp-1180226")
    print(result)
    print()
    # structures = mpr.get_structures(QUERY)
    # for s in structures:
    #     print(s)
    # 精度更高
    results = mpr.query(criteria={'material_id': QUERY},
                        properties=['formation_energy_per_atom', 'structure','cif','elasticity','piezo','diel','band_gap'])
    # print(results)
    formation_energy = results[0]['formation_energy_per_atom']
    # print(formation_energy)
    structure = results[0]['structure']
    # print(structure)
    cif = results[0]['cif']
    elasticity = results[0]['elasticity']
    # print(elasticity)
    piezo = results[0]['piezo']
    print(piezo)
    diel = results[0]['diel']
    print(diel)
    print(results[0]['band_gap'])

    # k = math.log(elasticity['K_Voigt_Reuss_Hill'])
    # 本处使用log
    # g = math.log(elasticity['G_Voigt_Reuss_Hill'])
    # 本处使用log
    # poisson_ratio = elasticity['poisson_ratio']
    # elastic_anisotropy = elasticity['elastic_anisotropy']
    # print(k, g,poisson_ratio,elastic_anisotropy)
    # save cif as file
    # c = CifWriter(structure)
    # c.write_file('./test/1/22862.cif')

    # test all entity 0804 - 89 elements
    element_list = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar',
                    'K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr',
                    'Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe',
                    'Cs','Ba','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi',
                    'La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu',
                    'Ac','Th','Pa','U','Np','Pu']
    # element_list = ['C','O']
    # print(len(element_list))

    # results = mpr.query(criteria={'material_id': QUERY},
    #                     properties=['full_formula','band_gap','exp.tags', 'icsd_ids','formation_energy_per_atom'])
    # results = data = mpr.query(criteria={'elements': {'$in': element_list},"has_bandstructure": True}, properties=['full_formula','band_gap','exp.tags', 'icsd_ids','formation_energy_per_atom'])


    # search all elements without warning label
    results = data = mpr.query(criteria={'elements': {'$in':element_list},"has_bandstructure": True,"elasticity": {"$exists": True}}, properties=['pretty_formula','band_gap','exp.tags', 'icsd_ids','formation_energy_per_atom'])
    print(len(results))
    print(results)
    for i in results:
        pretty_formula = i['pretty_formula']
        print(pretty_formula)

    # search all elasticity
    # results = mpr.query({"elasticity": {"$exists": True}},
    #                     properties=['material_id', 'pretty_formula', 'elasticity'])
    # for i in results:
    #     material_id = i['material_id']
    #     pretty_formula = i['pretty_formula']
    #     elasticity = i['elasticity']
    #     print(material_id)
    #     print(pretty_formula)
    #     print(elasticity)

    # print(results)


    # MAPI_KEY = "Kp8jstspRdzK1N2srqRI"
    # mpr = MPRester(MAPI_KEY)

    # # read 3402 csv file
    # dataset_csv = csv.reader(open('./data/material-data/mp-ids-3402.csv', 'r'))
    # dataset_count = 0
    # # read new csv file
    # new_file = open('new.csv', 'w', encoding='utf-8')
    # csv_writer = csv.writer(new_file)
    # new_file_fail = open('new_fail.csv', 'w', encoding='utf-8')
    # csv_writer_fail = csv.writer(new_file_fail)
    # for ids in dataset_csv:
    #     QUERY = ids[0]
    #     results = mpr.query(criteria={'material_id': QUERY},
    #                         properties=['structure','formation_energy_per_atom'])
    #     try:
    #         structure = results[0]['structure']
    #         formation_energy = results[0]['formation_energy_per_atom']
    #         c = CifWriter(structure)
    #         filename = './test/3402/'+ids[0].split("-")[1] + '.cif'
    #         c.write_file(filename)
    #         print('create '+ filename +' success')
    #         dataset_count += 1
    #         ids.append(formation_energy)
    #         csv_writer.writerow(ids)
    #     except:
    #         print("Error:" + ids[0])
    #         csv_writer_fail.writerow(ids)
    # # success 3207
    # print(dataset_count)
    #
    # # read 27430 csv file -> 19966
    # dataset_csv = csv.reader(open('./data/material-data/mp-ids-27430.csv', 'r'))
    # dataset_count = 0
    # # read new csv file
    # new_file = open('new2.csv', 'w', encoding='utf-8')
    # csv_writer = csv.writer(new_file)
    # new_file_fail = open('new2_fail.csv', 'w', encoding='utf-8')
    # csv_writer_fail = csv.writer(new_file_fail)
    # for ids in dataset_csv:
    #     QUERY = ids[0]
    #     results = mpr.query(criteria={'material_id': QUERY},
    #                         properties=['structure','formation_energy_per_atom'])
    #     try:
    #         structure = results[0]['structure']
    #         formation_energy = results[0]['formation_energy_per_atom']
    #         c = CifWriter(structure)
    #         filename = './test/27430/' + ids[0].split("-")[1] + '.cif'
    #         c.write_file(filename)
    #         print('create ' + filename + ' success')
    #         dataset_count += 1
    #         ids.append(formation_energy)
    #         csv_writer.writerow(ids)
    #     except:
    #         print("Error:" + ids[0])
    #         csv_writer_fail.writerow(ids)
    # print(dataset_count)
    # # success 19966
    #
    # # read 46744 csv file -> 36835
    # dataset_csv = csv.reader(open('./data/material-data/mp-ids-46744.csv', 'r'))
    # dataset_count = 0
    # # read new csv file
    # new_file = open('new3.csv', 'w', encoding='utf-8')
    # csv_writer = csv.writer(new_file)
    # new_file_fail = open('new3_fail.csv', 'w', encoding='utf-8')
    # csv_writer_fail = csv.writer(new_file_fail)
    # for ids in dataset_csv:
    #     QUERY = ids[0]
    #     results = mpr.query(criteria={'material_id': QUERY},
    #                         properties=['structure','formation_energy_per_atom'])
    #     try:
    #         structure = results[0]['structure']
    #         formation_energy = results[0]['formation_energy_per_atom']
    #         c = CifWriter(structure)
    #         filename = './test/46744/' + ids[0].split("-")[1] + '.cif'
    #         c.write_file(filename)
    #         print('create ' + filename + ' success')
    #         dataset_count += 1
    #         ids.append(formation_energy)
    #         csv_writer.writerow(ids)
    #     except:
    #         print("Error:" + ids[0])
    #         csv_writer_fail.writerow(ids)
    # print(dataset_count)
    # # success 36835

    # # elasticity - K_Voigt_Reuss_Hill (bulk), G_Voigt_Reuss_Hill (shear), poisson_ratio, elastic_anisotropy
    # # read 3402 csv file
    # dataset_csv = csv.reader(open('./test/mp-ids-3207.csv', 'r'))
    # # read new csv file (totol property)
    # new_file = open('id_prop.csv', 'w', encoding='utf-8')
    # csv_writer = csv.writer(new_file)
    # # fail data
    # new_file_fail = open('test/elasticity/elasticity_fail.csv', 'w', encoding='utf-8')
    # csv_writer_fail = csv.writer(new_file_fail)
    # for ids in dataset_csv:
    #     QUERY = ids[0]
    #     print(QUERY)
    #     results = mpr.query(criteria={'material_id': QUERY},
    #                         properties=['structure','elasticity'])
    #     try:
    #         structure = results[0]['structure']
    #         elasticity = results[0]['elasticity']
    #
    #         k = math.log(elasticity['K_Voigt_Reuss_Hill']) # 本处使用log
    #         g = math.log(elasticity['G_Voigt_Reuss_Hill']) # 本处使用log
    #         poisson_ratio = elasticity['poisson_ratio']
    #         elastic_anisotropy = elasticity['elastic_anisotropy']
    #
    #         c = CifWriter(structure)
    #         filename = './test/elasticity/'+ids[0] + '.cif'
    #         c.write_file(filename)
    #         print('create '+ filename +' success')
    #         ids.append(k)
    #         ids.append(g)
    #         ids.append(poisson_ratio)
    #         ids.append(elastic_anisotropy)
    #         csv_writer.writerow(ids)
    #     except:
    #         print("Error:" + ids[0])
    #         csv_writer_fail.writerow(ids)

    #
