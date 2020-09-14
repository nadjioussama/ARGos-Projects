import matplotlib.pyplot as plt
import csv
import math

import os

ctrl1 = []
ctrl2 = []
ctrl3 = []

ctrl1 = open("bonfire.csv", 'r')
ctrl2 = open("catch.csv", 'r')
ctrl3 = open("light.csv", 'r')

bonfire = [float(line[0]) for line in csv.reader(ctrl1)]
blob = [float(line[0]) for line in csv.reader(ctrl2)]
light = [float(line[0]) for line in csv.reader(ctrl3)]

time = [10, 20, 30, 40, 50]

plt.plot(time, bonfire, label="bonfire controller")
plt.plot(time, blob, label="blob controller")
plt.plot(time, light, label="light controller")

plt.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.xlabel("Number of robots")
plt.ylabel("Time to aggregate(steps)")
plt.title("Execution time comparaison using four light sources")
plt.show()