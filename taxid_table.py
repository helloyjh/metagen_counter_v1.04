import os
import pandas
import argparse
import tree
import pickle
import numpy as np

parser = argparse.ArgumentParser(description='Counter')
parser.add_argument('--vers', type=str, default='1.04')
args = parser.parse_args()

count_path = '../../../storage-gard/metagen/poseidon/count_taxid_v{}'.format(args.vers)

taxids = []
for x in os.listdir(count_path):
    with open('{}/{}'.format(count_path, x), 'rb') as f:
        count_dict = pickle.load(f)
    taxids = np.union1d(list(count_dict.keys()), taxids)

cols = list(taxids)

frame = pandas.DataFrame(None, columns=['f_name'] +cols)
time = pandas.DataFrame(None, columns=['f_name', 'second'])

cnt = 0
for x in os.listdir(count_path):
    with open('{}/{}'.format(count_path, x), 'rb') as f:
        count_dict = pickle.load(f)
    temp_frame = pandas.DataFrame(np.zeros((1,len(cols)+1)), columns=['f_name']+cols)
    for tax in list(count_dict.keys()):
        count = count_dict[tax]
        temp_frame[tax] += count
    
    f_name = x.split('.fastq')[0]
    temp_frame['f_name']=f_name
    
    frame = pandas.concat([frame, temp_frame])
  
    duration = x.split('time')[1].split('.')[0]
    time.loc[cnt] = [f_name, duration]
    cnt += 1

save_folder_name = 'count_ranked_v{}'.format(args.vers)
os.makedirs(save_folder_name, exist_ok=True)
frame.to_csv('{}/result_tax.csv'.format(save_folder_name))
time.to_csv('{}/taxid_counting_time.csv'.format(save_folder_name))