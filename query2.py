import csv
import numpy as np

files = [('./data/G1.csv', 'Group 1'), ('./data/G2.csv', 'Group 2'), ('./data/G3.csv', 'Group 3'), ('./data/G4.csv', 'Group 4')]

# holds the answers for each group as a dict obj. ie. {name: Group 1, answers: [....]}
groups= []

# get the data for each group
for group, name in files:
    answers = []
    with open(group) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            answers.append([int(row[0]), int(row[1]), int(row[2])])
    groups.append({'name': name, 'answers': answers})


def calc_similarity(zipped_list):
    similarity_rating = 0
    for list, comparison_list in zipped_list:
        # print("Comparing " + str(list) + " and " + str(comparison_list))
        difference = np.array(list)-np.array(comparison_list)
        for value in difference:
            similarity_rating += abs(value)
    return similarity_rating

# {'name': 'Group 1', 'Most Similar': 'Group 2', 'Rating': 23 }
final_scores = []

for group in groups:
    print("---------------" + group['name'] + "-----------------------")
    comparison_results = []
    for comparison_group in groups:
        if comparison_group['name'] == group['name']:
            pass
        else:
            # print("********Comparing with " + comparison_group['name'] + "*********")
            zip_list = zip(group['answers'], comparison_group['answers'])
            score = calc_similarity(zip_list)
            comparison_results.append({'name': comparison_group['name'], 'rating': score})
    # sort in ascending rating (most similar to least)
    comparison_results.sort(key=lambda x: x['rating'])
    print("Most similar to least similar: " + str(comparison_results) + "\n")
