# global temperatures
file = open("C:\\Users\\alish\\PycharmProjects\\pythonProject\\climate change showcase\\files .csv\\World Temperature 1880-2020.csv", "r") #change the path to your own
data = file.readlines()

years = []
for line in data:
    years.append(int(line.split(',')[0]))

temp = []
for line in data:
    numlist = line.split(',')[1].split()
    num = float(''.join(numlist))
    temp.append(num)

from matplotlib import pyplot as plt

plt.plot(years, temp)
plt.ylabel('temperature (C)')
plt.xlabel('years')
plt.show()

