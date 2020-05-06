import pandas as pd

data_file = '../../data/house_tiny.csv'
data = pd.read_csv(data_file)
#print(data)
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
#print(inputs)
inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)