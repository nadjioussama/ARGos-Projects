import matplotlib.pyplot as plt
import csv
import math

import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))




def normalize(disper_list, max_len):  
    for i in range(len(disper_list), max_len):
        disper_list.append(disper_list[-1])
    return disper_list


exp1 = []
exp2 = []
exp3 = []
exp4 = []

exp1 = open("disper1.csv", 'r')
exp2 = open("disper2.csv", 'r')
exp3 = open("disper3.csv", 'r')
exp4 = open("disper4.csv", 'r')

exp1_Dispersion_list = [float(line[0]) for line in csv.reader(exp1)]
exp2_Dispersion_list = [float(line[0]) for line in csv.reader(exp2)]
exp3_Dispersion_list = [float(line[0]) for line in csv.reader(exp3)]
exp4_Dispersion_list = [float(line[0]) for line in csv.reader(exp4)]

max_len = max(len(exp1_Dispersion_list), len(exp2_Dispersion_list), len(exp3_Dispersion_list), len(exp4_Dispersion_list))

exp1_Dispersion_list = normalize(exp1_Dispersion_list, max_len)
exp2_Dispersion_list = normalize(exp2_Dispersion_list, max_len)
exp3_Dispersion_list = normalize(exp3_Dispersion_list, max_len)
exp4_Dispersion_list = normalize(exp4_Dispersion_list, max_len)

avg_Dispersion = [(d1+ d2+ d3+ d4)/4 for d1, d2, d3, d4 in zip(exp1_Dispersion_list, exp2_Dispersion_list, exp3_Dispersion_list, exp4_Dispersion_list)]

with open('avg_dispersion.csv', 'w') as avg_dispersion_file:
    for elem in avg_Dispersion:
         avg_dispersion_file.write(str(elem) + "\n")

time = range(1, max_len+1)

plt.plot(time, avg_Dispersion)
plt.show()
