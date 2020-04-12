import csv
import random


# files = [('./data/q1.csv', 'Question1'), ('./data/q2.csv','Question2'), ('./data/q3.csv','Question3'), ('./data/q4.csv','Question4'), ('./data/q5.csv','Question5'),
#          ('./data/q6.csv', 'Question6'), ('./data/q7.csv','Question7'), ('./data/q8.csv','Question8'), ('./data/q9.csv','Question9'), ('./data/q10.csv','Question10'),
#          ('./data/q11.csv', 'Question11'), ('./data/q12.csv','Question12'), ('./data/q13.csv','Question13'), ('./data/q14.csv','Question14'), ('./data/q15.csv','Question15')]

files = [('./data/G1.csv', 'Group 1', 0), ('./data/G2.csv', 'Group 2', 1), ('./data/G3.csv', 'Group 3', 2), ('./data/G4.csv', 'Group 4', 3)]

num_generated = 20
all_generated_responses = []

for file, name, group_num in files:
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for i in range(num_generated):
                generated_response = []
                for value in row:
                    # random precentage between 0-5%
                    mutation = random.uniform(0, 0.05)
                    add = random.choice([True, False])
                    if add == True:
                        generated_response.append(round(int(value) + int(value) * mutation))
                    else:
                        generated_response.append(round(int(value) - int(value) * mutation))
                generated_response.append(group_num)
                all_generated_responses.append(generated_response)

save_filename = "Query5.csv"
with open(save_filename, 'w') as resultFile:
    writer = csv.writer(resultFile, delimiter=',')
    writer.writerows(all_generated_responses)
