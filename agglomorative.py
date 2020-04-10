from sklearn.cluster import AgglomerativeClustering
import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(5)

data = []

with open('./data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append([int(row[0]), int(row[1]), int(row[2])])

X = np.array(data)

clustering = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
clustering.fit_predict(X)
labels = clustering.labels_
print(labels)
fig = plt.figure()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
ax.scatter(X[:, 0], X[:, 1], X[:, 2],
           c=clustering.labels_, cmap='rainbow',edgecolor='k')


ax.set_xlabel('Yes')
ax.set_ylabel('No')
ax.set_zlabel('Undecided')
ax.set_title('4 clusters')
ax.dist = 12

plt.show()
