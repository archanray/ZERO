import csv
import numpy as np

erate_list = []
with open('./data/erates/20181005.csv', 'r') as inp:
    for row in csv.reader(inp):
      if len(row) > 5 and row[5] == "LOAD ZONE" and row[4] == ".Z.WCMASS":
        erate_list.append(float(row[6]))

erate_list = np.array([erate_list])
np.save('./data/erate_simplified_20181005.npy', erate_list)
