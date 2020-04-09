
import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5)

data = []

with open('./data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append([int(row[0]), int(row[1]), int(row[2])])

data = np.asarray(data)
estimators = [('k_means_4', KMeans(n_clusters=4))]

for name, est in estimators:
    fig = plt.figure()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
    est.fit(data)
    labels = est.labels_

    ax.scatter(data[:, 0], data[:, 1], data[:, 2],
               c=labels.astype(np.float), edgecolor='k')

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('Yes')
    ax.set_ylabel('No')
    ax.set_zlabel('Undecided')
    ax.set_title('4 clusters')
    ax.dist = 12

plt.show()
