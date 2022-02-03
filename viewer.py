import os
import pandas
import argparse
import tree
import pickle
import numpy as np


# ----------------setting-------------------------

parser = argparse.ArgumentParser(description='Counter')
parser.add_argument('--vrank', type=str, default='T')
parser.add_argument('--trank', type=str, default='T')
parser.add_argument('--vers', type=str, default='1.04')
parser.add_argument('--rm', type=int, default=1)
args = parser.parse_args()

remove_list = []
view_list = []

# ------------------------------------------

# path of tax_tree.map
tree_path = '../../../storage-gard/metagen/poseidon/tax_tree.map'
tree_dict = tree.tree_dictionary(tree_path)

# path of count table for taxonomy id
tax_frame = pandas.read_csv('count_ranked_v{}/result_tax.csv'.format(args.vers))
taxids = tax_frame.columns[2:]
file_list = tax_frame['f_name'].tolist()

converted_dict = {}
for taxid in taxids:
    if taxid == 'U':
        v_name = 'Unclassified'
        t_name = 'Unclassified'
    elif taxid == '9606':
        v_name = 'Homo Sapiens'
        t_name = 'Homo Sapiens'
    else:
        v_name, gg = tree.get_parent_rank(tree_dict, taxid, args.vrank)
        t_name, gg = tree.get_parent_rank(tree_dict, taxid, args.trank)

    if args.rm==1:
        if t_name in remove_list:
            continue
        else:
            converted_dict[taxid] = v_name
    elif args.rm==0:
        if t_name in view_list:
            converted_dict[taxid] = v_name 
 
use_cols = list(set(converted_dict.values()))
for col in use_cols:
    key_list = []
    for key in converted_dict.keys():
        if converted_dict[key] == col:
            key_list.append(key)
    col_sum = tax_frame[key_list].sum(axis=1)
    tax_frame[col] = -9
    tax_frame[col] = col_sum

view_frame = tax_frame[['f_name']+use_cols]

save_folder_name = 'count_ranked_v{}'.format(args.vers)
view_frame.to_csv('{}/result_rank_{}.csv'.format(save_folder_name, args.vrank))