from mkdir_if_not_exist import mkdir_if_not_exist

data_file = '../../data/house_tiny.csv'
mkdir_if_not_exist('../../data')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # Column names
    f.write('NA,Pave,127500\n')  # Each row is a data point
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')