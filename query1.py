import csv

files = [('./data/G1.csv', 'Group 1'), ('./data/G2.csv', 'Group 2'), ('./data/G3.csv', 'Group 3'), ('./data/G4.csv', 'Group 4')]

# calculate how much of the group disagrees with the majority answer
def calc_internal_agreement(answers):
    majorityAns = max(answers)
    return 100 - majorityAns

group_ratings = []

# get the data for each group
for group, name in files:
    group_agreement_rating = 0
    # calculate the agreement for each question for that group
    with open(group) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            answers = [int(row[0]), int(row[1]), int(row[2])]
            group_agreement_rating += calc_internal_agreement(answers)
    group_ratings.append({'name': name, 'rating': group_agreement_rating})

# sort in ascending rating (most internal agreement to least)
group_ratings.sort(key=lambda x: x['rating'])

print("Groups in order of most internal agreement to least: ")
for group in group_ratings:
    print(group['name'] + " rating: " + str(group['rating']))
