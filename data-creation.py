import csv
import random


files = [('./data/q1.csv', 'Question1'), ('./data/q2.csv','Question2'), ('./data/q3.csv','Question3'), ('./data/q4.csv','Question4'), ('./data/q5.csv','Question5'),
         ('./data/q6.csv', 'Question6'), ('./data/q7.csv','Question7'), ('./data/q8.csv','Question8'), ('./data/q9.csv','Question9'), ('./data/q10.csv','Question10'),
         ('./data/q11.csv', 'Question11'), ('./data/q12.csv','Question12'), ('./data/q13.csv','Question13'), ('./data/q14.csv','Question14'), ('./data/q15.csv','Question15')]

num_generated = 5

for file, name in files:
    group_num = 0
    responses = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            for i in range(num_generated):
                # random precentage between 0-5%
                mutation = random.uniform(0, 0.05)
                add = random.choice([True, False])
                if add == True:
                    yes = round(int(row[0]) + int(row[0]) * mutation)
                    no = round(int(row[1]) + int(row[1]) * mutation)
                    und = round(int(row[2]) + int(row[2]) * mutation)
                    responses.append([yes, no, und, group_num])
                else:
                    yes = round(int(row[0]) - int(row[0]) * mutation)
                    no = round(int(row[1]) - int(row[1]) * mutation)
                    und = round(int(row[2]) - int(row[2]) * mutation)
                    responses.append([yes, no, und, group_num])

            group_num += 1
        save_filename = "./results/" + name + ".csv"
        with open(save_filename, 'w') as resultFile:
            writer = csv.writer(resultFile, delimiter=',')
            writer.writerows(responses)
