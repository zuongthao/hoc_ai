import pandas as pd
from mxnet import np

data_file = '../../data/house_tiny.csv'
data = pd.read_csv(data_file)
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
X, y = np.array(inputs.values), np.array(outputs.values)
print(X, y)