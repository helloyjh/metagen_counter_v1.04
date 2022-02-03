import time

class Counter():
    def __init__(self,):
        self.count_dict = {}
        
    def row_to_info(self, row):
        read_id = str(row).split('\\t')[0].split('@')[1]
        tax_info = str(row).split('\\n')[0].split('\\t')
        if len(tax_info) ==1:
            return read_id, ['U'], 0
        else:
            tax_ids = tax_info[1:]
            taxx = []
            for x in tax_ids:
                [etype, tax_id, mat_len, mat_rat, mat_cnt] = x.split(':')
                mat_len = int(int(mat_len)/int(mat_cnt))
                taxx.append(tax_id)
  
            return read_id, taxx, mat_len

    def add_(self, ti_list):
        c = 1/len(ti_list)
        for ti in ti_list:
            if ti in self.count_dict:
                self.count_dict[ti] += c
            else:
                self.count_dict[ti] = c

    def calcluate(self, R_path):
        start_time = time.time()
        R = open('{}'.format(R_path),'rb')
        while True:
            try:
                row = R.readline()
                read_id, tex_ids, mat_len = self.row_to_info(row)
                self.add_(tex_ids)            
 
            except:
                print('No more line')
                break
        end_time = time.time()
        duration = int(end_time - start_time)

        return self.count_dict, duration
