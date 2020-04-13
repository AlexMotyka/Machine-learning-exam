import csv
import numpy as np

files = [('./data/G1.csv', 'Group 1'), ('./data/G2.csv', 'Group 2'), ('./data/G3.csv', 'Group 3'), ('./data/G4.csv', 'Group 4')]

# holds the answers for each group as a dict obj. ie. {name: Group 1, answers: [....]}
groups= []

# calculate what percentage disagreed with the majority
def calc_internal_agreement(answers):
    majorityAns = max(answers)
    return 100 - majorityAns

# get the data for each group
for group, name in files:
    answers = []
    with open(group) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            answers.append([int(row[0]), int(row[1]), int(row[2])])
    groups.append({'name': name, 'answers': answers})

# for each group go through each question and find the level of agreement among group members
for group in groups:
    print("---------------" + group['name'] + "-----------------------")
    comparison_results = []
    question_num = 1
    # for each answer calculate the agreement among members
    for answer in group['answers']:
        score = calc_internal_agreement(answer)
        name = "Question " + str(question_num)
        comparison_results.append({'name': name, 'rating': score})
        question_num+=1
    # sort in ascending rating (most similar to least)
    comparison_results.sort(key=lambda x: x['rating'])
    print("Most agreement to least agreement: ")
    for result in comparison_results:
        print(str(result['name']) + " with rating: " + str(result['rating']))
