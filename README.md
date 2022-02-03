# metagen_counter_v1.04

- multi.py
  read .tax files and counting. saving result as pickle
 
- taxid_table.py
  Create a table with column taxonomy ID and row .tax file name from pickle files
  
- viewer.py
  Create any type of table you want, such as rank, exclusion, inclusion
  
  #option in the top of viewer.py
  
  parser = argparse.ArgumentParser(description='Counter')
  parser.add_argument('--vrank', type=str, default='T') 
  parser.add_argument('--trank', type=str, default='T')
  parser.add_argument('--vers', type=str, default='1.04')
  parser.add_argument('--rm', type=int, default=1)
  args = parser.parse_args()

  remove_list = []
  view_list = []
  
  args.vrank : view rank you want to see
  args.trank : target rank you want to remove or include
  args.rm : if 1, remove x in remove_list for args.trank
             elif 0, only include view_list for args.trank
  remove_list : list you want to remove from all columns
  view_list : list of only the parts you want to include in the whole
