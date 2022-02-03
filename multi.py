import os
import counter
import numpy as np
import argparse
import pickle
from multiprocessing import Process

parser = argparse.ArgumentParser(description='Counter')
parser.add_argument('--n_core', type=int, default=10)
args = parser.parse_args()

dir_path = '../../../storage-gard/metagen/poseidon/v1.04'

def Proc(R_proc):
    for i in range(len(R_proc)):
        R_path = '{}/{}'.format(dir_path, R_proc[i])
      
        Counter = counter.Counter()
        count_dict, duration = Counter.calcluate(R_path)

        os.makedirs('count_taxid', exist_ok=True)
        with open('count_taxid/{}_time{}.pickle'.format(R_proc[i], duration), 'wb') as f:
            pickle.dump(count_dict, f)
   
    proc = os.getpid()

R_list = os.listdir(dir_path)
R_list = np.array_split(R_list, args.n_core)

procs = []
for index, R_proc in enumerate(R_list):
    proc = Process(target = Proc, args=(R_proc,))
    procs.append(proc)
    proc.start()

for proc in procs:
    proc.join()

    