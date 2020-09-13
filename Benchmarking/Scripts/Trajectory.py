import matplotlib.pyplot as plt
import csv

x1, y1 = [], []
x2, y2 = [], []
x3, y3 = [], []
x4, y4 = [], []
x5, y5 = [], []
x6, y6 = [], []
x7, y7 = [], []
x8, y8 = [], []
x9, y9 = [], []
x10, y10 = [], []
x11, y11 = [], []
x12, y12 = [], []
x13, y13 = [], []
x14, y14 = [], []
x15, y15 = [], []
x16, y16 = [], []
x17, y17 = [], []
x18, y18 = [], []
x19, y19 = [], []
x20, y20 = [], []


with open("trajectory.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for i, line in enumerate(reader):
        
        x_str = float(line[2].replace(',', '.'))
        y_str = float(line[3].replace(',', '.'))
        if i % 20 == 0:
            x1.append(x_str)
            y1.append(y_str)
        elif i % 20 == 1:
            x2.append(x_str)
            y2.append(y_str)
        elif i % 20 == 2:
            x3.append(x_str)
            y3.append(y_str)
        elif i % 20 == 3:
            x4.append(x_str)
            y4.append(y_str)
        elif i % 20 == 4:
            x5.append(x_str)
            y5.append(y_str)
        elif i % 20 == 5:
            x6.append(x_str)
            y6.append(y_str)
        elif i % 20 == 6:
            x7.append(x_str)
            y7.append(y_str)
        elif i % 20 == 7:
            x8.append(x_str)
            y8.append(y_str)
        elif i % 20 == 8:
            x9.append(x_str)
            y9.append(y_str)
        elif i % 20 == 9:
            x10.append(x_str)
            y10.append(y_str)
        elif i % 20 == 10:
            x11.append(x_str)
            y11.append(y_str)
        elif i % 20 == 11:
            x12.append(x_str)
            y12.append(y_str)
        elif i % 20 == 12:
            x13.append(x_str)
            y13.append(y_str)
        elif i % 20 == 13:
            x14.append(x_str)
            y14.append(y_str)
        elif i % 20 == 14:
            x15.append(x_str)
            y15.append(y_str)
        elif i % 20 == 15:
            x16.append(x_str)
            y16.append(y_str)
        elif i % 20 == 16:
            x17.append(x_str)
            y17.append(y_str)
        elif i % 20 == 17:
            x18.append(x_str)
            y18.append(y_str)
        elif i % 20 == 18:
            x19.append(x_str)
            y19.append(y_str)
        else:
            x20.append(x_str)
            y20.append(y_str)



plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.plot(x6, y6)
plt.plot(x7, y7)
plt.plot(x8, y8)
plt.plot(x9, y9)
plt.plot(x10, y10)
plt.plot(x11, y11)
plt.plot(x12, y12)
plt.plot(x13, y13)
plt.plot(x14, y14)
plt.plot(x15, y15)
plt.plot(x16, y16)
plt.plot(x17, y17)
plt.plot(x18, y18)
plt.plot(x19, y19)
plt.plot(x20, y20)


plt.show()
