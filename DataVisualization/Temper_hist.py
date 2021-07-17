import csv
import matplotlib.pyplot as plt
import random

f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data:
    month = row[0].split('-')[1]
    if(row[-1] != ''):
        if(month == '08'):
            aug.append(float(row[-1]))

        elif(month == '01'):
            jan.append(float(row[-1]))


plt.title("top temperature")
plt.hist(aug, bins=100, color='r', label='aug')
plt.hist(jan, bins=100, color='g', label='jan')
plt.legend()
plt.show()