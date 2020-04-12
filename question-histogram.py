import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets


files = [('./data/q1.csv', 3,5,1, 'Question 1'), ('./data/q2.csv', 3,5,2, 'Question 2'), ('./data/q3.csv', 3,5,3, 'Question 3'), ('./data/q4.csv', 3,5,4, 'Question 4'), ('./data/q5.csv', 3,5,5, 'Question 5'),
         ('./data/q6.csv', 3,5,6, 'Question 6'), ('./data/q7.csv', 3,5,7, 'Question 7'), ('./data/q8.csv', 3,5,8, 'Question 8'), ('./data/q9.csv', 3,5,9, 'Question 9'), ('./data/q10.csv', 3,5,10, 'Question 10'),
         ('./data/q11.csv', 3,5,11, 'Question 11'), ('./data/q12.csv', 3,5,12, 'Question 12'), ('./data/q13.csv', 3,5,13, 'Question 13'), ('./data/q14.csv', 3,5,14, 'Question 14'), ('./data/q15.csv', 3,5,15, 'Question 15')]

fig = plt.figure()

# get the data for each group
for group, rows, cols, num, name in files:
    # get the data for a single group
    with open(group) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')

        yes_bars = []
        no_bars = []
        undecided_bars = []

        for row in csv_reader:
            yes_bars.append(int(row[0]))
            no_bars.append(int(row[1]))
            undecided_bars.append(int(row[2]))

        ax = fig.add_subplot(rows, cols, num)
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
        ax.set_xlabel('Groups', fontweight='bold')
        ax.set_xticks([r + barWidth for r in range(len(yes_bars))])
        ax.set_xticklabels(['G1', 'G2', 'G3', 'G4'])

fig.tight_layout()
plt.show()
