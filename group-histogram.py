import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets


files = [('./data/G1.csv', 221, 'Group 1'), ('./data/G2.csv', 222, 'Group 2'), ('./data/G3.csv', 223, 'Group 3'), ('./data/G4.csv', 224, 'Group 4')]

fig = plt.figure()

# get the data for each group
for group, axis, name in files:
    # get the data for a single group
    with open(group) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        yes_bars = []
        no_bars = []
        undecided_bars = []

        for row in csv_reader:
            yes_bars.append(int(row[0]))
            no_bars.append(int(row[1]))
            undecided_bars.append(int(row[2]))

        ax = fig.add_subplot(axis)
        ax.set_title(name)

        # set width of bar
        barWidth = 0.25

        # Set position of bar on X axis
        r1 = np.arange(len(yes_bars))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        # Make the plot
        ax.bar(r1, yes_bars, color='green', width=barWidth, edgecolor='white', label='Yes')
        ax.bar(r2, no_bars, color='red', width=barWidth, edgecolor='white', label='No')
        ax.bar(r3, undecided_bars, color='grey', width=barWidth, edgecolor='white', label='Und.')

        # Add xticks on the middle of the group bars
        ax.set_xlabel('Question Responses', fontweight='bold')
        ax.set_xticks([r + barWidth for r in range(len(yes_bars))])
        ax.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15'])

ax =fig.add_subplot(222)
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
fig.tight_layout()
plt.show()
