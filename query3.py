import csv
import numpy as np

files = [('./data/q1.csv', 'Question 1'), ('./data/q2.csv','Question 2'), ('./data/q3.csv','Question 3'), ('./data/q4.csv','Question 4'), ('./data/q5.csv','Question 5'),
         ('./data/q6.csv', 'Question 6'), ('./data/q7.csv','Question 7'), ('./data/q8.csv','Question 8'), ('./data/q9.csv','Question 9'), ('./data/q10.csv','Question 10'),
         ('./data/q11.csv', 'Question 11'), ('./data/q12.csv','Question 12'), ('./data/q13.csv','Question 13'), ('./data/q14.csv','Question 14'), ('./data/q15.csv','Question 15')]


def calculate_agreement(answers):
    answers_sum = answers[0] + answers[1] + answers[2] + answers[3]
    return 400 - max(answers_sum)

question_ratings = []

# get the data for each question
for question, name in files:
    answers = []
    # get the data for a single question
    with open(question) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            answers.append(np.array([int(row[0]), int(row[1]), int(row[2])]))
    question_rating = calculate_agreement(answers)
    question_ratings.append({'name': name, 'rating': question_rating})


# sort in ascending rating (most agreement across groups to least)
question_ratings.sort(key=lambda x: x['rating'])

print("Questions in order of most group agreement to least: ")
for question in question_ratings:
    print(question['name'] + " rating: " + str(question['rating']))
