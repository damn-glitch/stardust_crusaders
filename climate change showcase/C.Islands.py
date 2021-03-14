# C.Islands temperatures
file_2 = open('C:\\Users\\alish\\PycharmProjects\\pythonProject\\climate change showcase\\files .csv\\Carribean Islands Temperature 1910-2019.csv', "r") #change the path to your own
data_2 = file_2.readlines()

years_2 = []
for line in data_2:
    years_2.append(int(line.split(',')[0]))

temp_2 = []
for line in data_2:
    numlist_2 = line.split(',')[1].split()
    num_2 = float(''.join(numlist_2))
    temp_2.append(num_2)
from matplotlib import pyplot as plt

plt.plot(years_2, temp_2)
plt.ylabel('temperature (C)')
plt.xlabel('years')
plt.show()
