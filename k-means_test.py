from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import csv


# file_list = ['G1-Sheet1.csv', 'G2-Sheet1.csv', 'G3-Sheet1.csv', 'G4-Sheet1.csv']
file_list = ['q1_addedVals.csv',
             'q2_addedVals.csv',
             'q3_addedVals.csv',
             'q4_addedVals.csv',
             'q5_addedVals.csv',
             'q6_addedVals.csv',
             'q7_addedVals.csv',
             'q8_addedVals.csv',
             'q9_addedVals.csv',
             'q10_addedVals.csv',
             'q11_addedVals.csv',
             'q12_addedVals.csv',
             'q13_addedVals.csv',
             'q14_addedVals.csv',
             'q15_addedVals.csv']
answers_arr = []
input_arr = []
for filename in file_list:
    with open(filename) as csvf:
        csvf_read = csv.reader(csvf, delimiter=',')

        for row in csvf_read:
            input_arr.append([int(row[0]), int(row[1]), int(row[2])])


X = np.asanyarray(input_arr)
df = pd.DataFrame(X)
km = KMeans(n_clusters=4)
km.fit(X)
predict = km.predict(X)
labels = km.labels_

#Plotting
fig = plt.figure(1, figsize=(7,7))
ax = Axes3D(fig, rect=[0, 0, 0.95, 1], elev=48, azim=134)
ax.scatter(X[:, 0], X[:, 1], X[:, 2],
          c=labels.astype(np.float), edgecolor="k", s=50)
ax.set_xlabel("Yes")
ax.set_ylabel("No")
ax.set_zlabel("Undecided")
plt.title("K Means", fontsize=14)
# plt.show()


df = pd.DataFrame(X)
df.columns = ["Yes", "No", "Un"]
df["cluster"] = predict
df.to_csv("NewClusters.csv")