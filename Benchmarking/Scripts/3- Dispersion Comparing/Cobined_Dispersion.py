import matplotlib.pyplot as plt
import csv
import math

import os

def normalize(disper_list, max_len):
    for i in range(len(disper_list), max_len):
        disper_list.append(disper_list[-1])
    return disper_list


ctrl1 = []
ctrl2 = []
ctrl3 = []

ctrl1 = open("bonfire.csv", 'r')
ctrl2 = open("catch.csv", 'r')
ctrl3 = open("light.csv", 'r')

controller1_Dispersion_list = [float(line[0]) for line in csv.reader(ctrl1)]
controller2_Dispersion_list = [float(line[0]) for line in csv.reader(ctrl2)]
controller3_Dispersion_list = [float(line[0]) for line in csv.reader(ctrl3)]


max_len = max(len(controller1_Dispersion_list), len(controller2_Dispersion_list), len(controller3_Dispersion_list))

controller1_Dispersion_list = normalize(controller1_Dispersion_list, max_len)
controller2_Dispersion_list = normalize(controller2_Dispersion_list, max_len)
controller3_Dispersion_list = normalize(controller3_Dispersion_list, max_len)


time = range(1, max_len+1)

plt.plot(time, controller1_Dispersion_list, label="bonfire controller")
plt.plot(time, controller2_Dispersion_list, label="catch controller")
plt.plot(time, controller3_Dispersion_list, label="light controller")



plt.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.xlabel("time(step)")
plt.ylabel("average Dispersion value")
plt.title("Dispersion values Comparaison")
plt.show()
