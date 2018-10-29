import sys
import pandas as pd
import pickle
import csv
import numpy as np

csvFile = sys.argv[1]

dataset = pd.read_csv(csvFile)
X = dataset.iloc[:, [6,7,8,9,10,11,12]].values

loaded_model = pickle.load(open("./ML Training Files/MLModel.sav","rb"))
y = loaded_model.predict(X)
y = pd.Series(y)

result = pd.concat([dataset,y], axis=1)

result.to_csv('./Files/output.csv', sep=',', encoding='utf-8',index=False)


r = csv.reader(open('./Files/output.csv'))

lines = list(r)

finallist = [["timestamp","value"]]
sublist = []
for i in range(len(lines)):
    sublist = []
    sublist.append("new Date('{}')".format(lines[i][0]))
    sublist.append(int(lines[i][13]))
    finallist.append(sublist)

with open('./Files/finalresult.txt', 'w') as f:
    f.write(repr(finallist))





