import os
import time
import numpy as np

def tree_dictionary(tree_path):
    tree = open('{}'.format(tree_path),'rb')
    cnt = 0
    tree_dict = {}
    start = time.time()
    finish = 0
    while True:
        row = str(tree.readline())[2:]
        info = row.split('$')
        if len(info)==4:
            finish = 0
            tax_id = info[0]
            tax_name = info[1]
            par_id = info[-2]
            rank = info[-1].split('\\n')[0]
            tree_dict[tax_id] = [par_id, rank, tax_name]
        else:
            finish += 1
        
        if finish == 50:
            return tree_dict

def find_name(x, t2s_dict):
    key = x.split('|')
    if len(key) == 5:
        name = key[-1]
        name_arr = name.split(' ')[1:]
        for w in range(len(name_arr)):
            try:
                if w == 0:
                    find = ' '.join(name_arr)
                else:
                    find = ' '.join(name_arr[:-w])
                tax_id = s2t_dict[find]
                return tax_id, True
            except:
                continue
 
    return x, False

def get_parent_rank(tree_dict, tax_id, target_rank):
    while True:
        try:
            rank = tree_dict[tax_id][1]
            tax_name = tree_dict[tax_id][2]
            tax_id = tree_dict[tax_id][0]
            if rank == target_rank:
                return tax_name, True
        except:
            return 'Unclassified', False

def spec_table():
    table_path = '../../../storage-gard/metagen/poseidon/poseidon.idx'
    X = open(table_path, 'rb')
    table_dict = {}
    for [_, info] in enumerate(X):
        info = str(info).split(':')
        GI = info[0]
        tex_id = info[1]
        spec_strain = info[-1].split('_')[0].split(' ')

        if len(spec_strain)==1:
            spec = spec_strain[0]
        else:
            spec = ' '.join(spec_strain[:-1])
        table_dict[tex_id] = spec