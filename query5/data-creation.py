import csv
import random

"""
This script takes each groups answer to question 4 and creates 20 data points that are similar to it (each index value is within +/- 5% of the original group answer)
These data points are saved in a csv that is used by the neural net for testing and training
Each row in the csv has the following structure: yes,no,undecided,group_number
"""

files = [('./data/G1.csv', 'Group 1', 0), ('./data/G2.csv', 'Group 2', 1), ('./data/G3.csv', 'Group 3', 2), ('./data/G4.csv', 'Group 4', 3)]

# genereate this many data points
num_generated = 20
# store the generated data points for writing to a csv
all_generated_responses = []

# for each group read in the original response and generate a speficied number of similar responses
for file, name, group_num in files:
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # generate the responses
            for i in range(num_generated):
                generated_response = []
                # modify each value +/- 5%
                for value in row:
                    # random precentage between 0-5%
                    mutation = random.uniform(0, 0.05)
                    add = random.choice([True, False])
                    # if add is true, add the mutation value
                    if add == True:
                        generated_response.append(round(int(value) + int(value) * mutation))
                    # else subtract the mutation value
                    else:
                        generated_response.append(round(int(value) - int(value) * mutation))
                # add the group number to the end of the data point for training/testing the neural net
                generated_response.append(group_num)
                all_generated_responses.append(generated_response)

# write each data point to a csv file
save_filename = "neural-net-data.csv"
with open(save_filename, 'w') as resultFile:
    writer = csv.writer(resultFile, delimiter=',')
    writer.writerows(all_generated_responses)
