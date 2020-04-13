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
            # get the response
            answers.append([int(row[0]), int(row[1]), int(row[2])])
    groups.append({'name': name, 'answers': answers})


# take 2 lists and calculate the difference between each index as an absolute value
def calc_similarity(zipped_list):
    similarity_rating = 0
    for list, comparison_list in zipped_list:
        difference = np.array(list)-np.array(comparison_list)
        for value in difference:
            similarity_rating += abs(value)
    return similarity_rating

# {'name': 'Group 1', 'Most Similar': 'Group 2', 'Rating': 23 }
final_scores = []

# go through each group and compare there answers against the other groups
for group in groups:
    print("---------------" + group['name'] + "-----------------------")
    comparison_results = []
    # compare against the other groups
    for comparison_group in groups:
        # a group doesn't compare against its own answers so it is skipped
        if comparison_group['name'] == group['name']:
            pass
        else:
            # zip this groups answers with the comparison groups answers
            zip_list = zip(group['answers'], comparison_group['answers'])
            score = calc_similarity(zip_list)
            comparison_results.append({'name': comparison_group['name'], 'rating': score})
    # sort in ascending rating (most similar to least)
    comparison_results.sort(key=lambda x: x['rating'])
    print("Most similar to least similar: " + str(comparison_results) + "\n")
