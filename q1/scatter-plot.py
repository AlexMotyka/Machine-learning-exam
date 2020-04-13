import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets


files = [('./data/G1.csv', 'red', 221, 'Group 1'), ('./data/G2.csv', 'blue', 222, 'Group 2'), ('./data/G3.csv', 'green', 223, 'Group 3'), ('./data/G4.csv', 'black', 224, 'Group 4')]

fig = plt.figure()

# get the data for each group
for group, color, axis, name in files:
    # get the data for a single group
    with open(group) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        group_data = []
        for row in csv_reader:
            group_data.append([int(row[0]), int(row[1]), int(row[2])])
        group_data = np.asarray(group_data)

        ax = fig.add_subplot(axis, projection='3d', elev=25, azim=120)
        ax.scatter(group_data[:, 0], group_data[:, 1], group_data[:, 2], color=color, edgecolor='k')

        ax.set_xlabel('Yes')
        ax.set_ylabel('No')
        ax.set_zlabel('Undecided')
        ax.set_title(name + " Responses")
        ax.dist = 12

plt.show()
