import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

files = [('./data/G1.csv', 'red', 221), ('./data/G2.csv', 'blue', 222), ('./data/G3.csv', 'green', 223), ('./data/G4.csv', 'black', 224)]

fig = plt.figure()

for group, color, axis in files:

    yes = []
    no = []
    undecided = []

    with open(group) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            yes.append(int(row[0]))
            no.append(int(row[1]))
            undecided.append(int(row[2]))
        ax = fig.add_subplot(axis, projection='3d')
        ax.scatter(yes, no, undecided, color=color)
        ax.set_xlabel('Yes')
        ax.set_ylabel('No')
        ax.set_zlabel('Undecided')


plt.show()
