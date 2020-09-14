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



plt.plot(x1, y1, alpha=0.6)
plt.scatter(x1[0], y1[0], alpha=0.25,color='b')
plt.scatter(x1[-1], y1[-1], color='b')

plt.plot(x2, y2, alpha=0.6)
plt.scatter(x2[0], y2[0], alpha=0.25,color='b')
plt.scatter(x2[-1], y2[-1], color='b')

plt.plot(x3, y3, alpha=0.6)
plt.scatter(x3[0], y3[0], alpha=0.25,color='b')
plt.scatter(x3[-1], y3[-1], color='b')

plt.plot(x4, y4, alpha=0.6)
plt.scatter(x4[0], y4[0], alpha=0.25,color='b')
plt.scatter(x4[-1], y4[-1], color='b')

plt.plot(x5, y5, alpha=0.6)
plt.scatter(x5[0], y5[0], alpha=0.25,color='b')
plt.scatter(x5[-1], y5[-1], color='b')

plt.plot(x6, y6, alpha=0.6)
plt.scatter(x6[0], y6[0], alpha=0.25,color='b')
plt.scatter(x6[-1], y6[-1], color='b')

plt.plot(x7, y7, alpha=0.6)
plt.scatter(x7[0], y7[0], alpha=0.25,color='b')
plt.scatter(x7[-1], y7[-1], color='b')

plt.plot(x8, y8, alpha=0.6)
plt.scatter(x8[0], y8[0], alpha=0.25,color='b')
plt.scatter(x8[-1], y8[-1],color='b')

plt.plot(x9, y9, alpha=0.6)
plt.scatter(x9[0], y9[0], alpha=0.25,color='b')
plt.scatter(x9[-1], y9[-1], color='b')

plt.plot(x10, y10, alpha=0.6)
plt.scatter(x10[0], y10[0], alpha=0.25,color='b')
plt.scatter(x10[-1], y10[-1], color='b')

plt.plot(x11, y11, alpha=0.6)
plt.scatter(x11[0], y11[0], alpha=0.25,color='b')
plt.scatter(x11[-1], y11[-1], color='b')

plt.plot(x13, y13, alpha=0.6)
plt.scatter(x12[0], y12[0], alpha=0.25,color='b')
plt.scatter(x12[-1], y12[-1], color='b')

plt.plot(x12, y12, alpha=0.6)
plt.scatter(x13[0], y13[0], alpha=0.25,color='b')
plt.scatter(x13[-1], y13[-1], color='b')

plt.plot(x14, y14, alpha=0.6)
plt.scatter(x14[0], y14[0], alpha=0.25,color='b')
plt.scatter(x14[-1], y14[-1], color='b')

plt.plot(x15, y15, alpha=0.6)
plt.scatter(x15[0], y15[0], alpha=0.25,color='b')
plt.scatter(x15[-1], y15[-1], color='b')

plt.plot(x16, y16, alpha=0.6)
plt.scatter(x16[0], y16[0], alpha=0.25,color='b')
plt.scatter(x16[-1], y16[-1], color='b')

plt.plot(x17, y17, alpha=0.6)
plt.scatter(x17[0], y17[0], alpha=0.25,color='b')
plt.scatter(x17[-1], y17[-1], color='b')

plt.plot(x18, y18, alpha=0.6)
plt.scatter(x18[0], y18[0], alpha=0.25,color='b')
plt.scatter(x18[-1], y18[-1], color='b')

plt.plot(x19, y19, alpha=0.6)
plt.scatter(x19[0], y19[0], alpha=0.25,color='b')
plt.scatter(x19[-1], y19[-1], color='b')

plt.plot(x20, y20, alpha=0.6)
plt.scatter(x20[0], y20[0], alpha=0.25,color='b')
plt.scatter(x20[-1], y20[-1], color='b')


gx = (x1[-1]+ x2[-1]+ x3[-1]+ x4[-1]+ x5[-1]+ x6[-1]+ x7[-1]+ x8[-1]+ x9[-1]+ x10[-1]+ x11[-1]+ x12[-1]+ x13[-1]+ x14[-1]+ x15[-1]+ x16[-1]+ x17[-1]+ x18[-1]+ x19[-1]+ x20[-1])/20
gy = (y1[-1]+ y2[-1]+ y3[-1]+ y4[-1]+ y5[-1]+ y6[-1]+ y7[-1]+ y8[-1]+ y9[-1]+ y10[-1]+ y11[-1]+ y12[-1]+ y13[-1]+ y14[-1]+ y15[-1]+ y16[-1]+ y17[-1]+ y18[-1]+ y19[-1]+ y20[-1])/20




plt.annotate('aggregation', xy=(gx, gy), xytext=(gx+1, gy+1), arrowprops=dict(facecolor='black', shrink=0.2))

plt.xlabel("x")
plt.ylabel("y")
plt.title("20 Foot-Bots trajectory in the arena")


plt.show()
