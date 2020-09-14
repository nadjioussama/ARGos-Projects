import matplotlib.pyplot as plt
import csv
import math



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


def distance(Xa, Ya,  Xb, Yb):
    dis_x = [math.pow((x1 - x2), 2) for x1, x2 in zip(Xa, Xb)]
    dis_y = [math.pow((y1 - y2), 2) for y1, y2 in zip(Ya, Yb)]

    dis = [math.sqrt(x + y) for x, y in zip(dis_x, dis_y)]
    return dis



with open("dispersion.csv", "r") as csvfile:
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


x_group = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20]
gravity_center_x = [(sum(column)/20) for column in zip(*x_group)]

y_group = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y18, y19, y20]
gravity_center_y = [(sum(column)/20) for column in zip(*y_group)]

distance_to_gravity_center_group = [
    distance(gravity_center_x, gravity_center_y,  x1, y1),
    distance(gravity_center_x, gravity_center_y,  x2, y2),
    distance(gravity_center_x, gravity_center_y,  x3, y3),
    distance(gravity_center_x, gravity_center_y,  x4, y4),
    distance(gravity_center_x, gravity_center_y,  x5, y5),
    distance(gravity_center_x, gravity_center_y,  x6, y6),
    distance(gravity_center_x, gravity_center_y,  x7, y7),
    distance(gravity_center_x, gravity_center_y,  x8, y8),
    distance(gravity_center_x, gravity_center_y,  x9, y9),
    distance(gravity_center_x, gravity_center_y,  x10, y10),
    distance(gravity_center_x, gravity_center_y,  x11, y11),
    distance(gravity_center_x, gravity_center_y,  x12, y12),
    distance(gravity_center_x, gravity_center_y,  x13, y13),
    distance(gravity_center_x, gravity_center_y,  x14, y14),
    distance(gravity_center_x, gravity_center_y,  x15, y15),
    distance(gravity_center_x, gravity_center_y,  x16, y16),
    distance(gravity_center_x, gravity_center_y,  x17, y17),
    distance(gravity_center_x, gravity_center_y,  x18, y18),
    distance(gravity_center_x, gravity_center_y,  x19, y19),
    distance(gravity_center_x, gravity_center_y,  x20, y20)
    
    ]


avg_distance_to_gravity_center = [(sum(column)/20) for column in zip(*distance_to_gravity_center_group)]

Rs = 0.17
dispersion = [((elem)/(4*Rs**2)) for elem in avg_distance_to_gravity_center]

with open('dispersion_list.csv', 'w') as dispersion_list_file:
    for elem in dispersion:
         dispersion_list_file.write(str(elem) + "\n")

time = range(1, len(dispersion)+1)

plt.plot(time, dispersion)

plt.show()
