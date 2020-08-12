import re
from collections import defaultdict
import pandas as pd
# Returns a list of list
def get_raw_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return data

def extract_data(dataset, sname = 'Vandalize'):
    ships = defaultdict(list)
    #with open(filename, 'w') as file:
    for data in dataset:
        split = re.split('=|, |', data)
        for entry in range(0,len(split)-1,2):
            ships[split[entry]].append(split[entry+1])
    df = pd.DataFrame.from_dict(ships)
    df.to_excel('/home/malcyan/Documents/Data/EOVessels.xlsx', sheet_name = sname)



if __name__ == '__main__':
    data = get_raw_data('/home/malcyan/Documents/Data/vessel_report.txt')
    extract_data(data)
