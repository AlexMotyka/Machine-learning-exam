import csv
import numpy as np

files = [('./data/q1.csv', 'Question 1'), ('./data/q2.csv','Question 2'), ('./data/q3.csv','Question 3'), ('./data/q4.csv','Question 4'), ('./data/q5.csv','Question 5'),
         ('./data/q6.csv', 'Question 6'), ('./data/q7.csv','Question 7'), ('./data/q8.csv','Question 8'), ('./data/q9.csv','Question 9'), ('./data/q10.csv','Question 10'),
         ('./data/q11.csv', 'Question 11'), ('./data/q12.csv','Question 12'), ('./data/q13.csv','Question 13'), ('./data/q14.csv','Question 14'), ('./data/q15.csv','Question 15')]


questions = []

# calculate the similarity two questions have to one another
def calc_similarity(zipped_list):
    # a similarity_rating of 0 indicates the answers were identical
    similarity_rating = 0
    for list, comparison_list in zipped_list:
        # subtract the arrays to find the difference between each index
        difference = np.array(list)-np.array(comparison_list)
        for value in difference:
            # add the absolute difference to the similarity rating
            similarity_rating += abs(value)
    return similarity_rating


# get the data for each question
for question, name in files:
    answers = []
    # get the data for a single question
    with open(question) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            answers.append([int(row[0]), int(row[1]), int(row[2])])
    questions.append({'name': name, 'answers': answers})

# for each question compare it against the other questions
for question in questions:
    print("---------------" + question['name'] + "-----------------------")
    comparison_results = []
    # compare the question against each other question
    for comparison_question in questions:
        # don't compare a question against itself
        if comparison_question['name'] == question['name']:
            pass
        else:
            # zip this questions answers with the comparison questions answers
            zip_list = zip(question['answers'], comparison_question['answers'])
            score = calc_similarity(zip_list)
            comparison_results.append({'name': comparison_question['name'], 'rating': score})
    # sort in ascending rating (most similar to least)
    comparison_results.sort(key=lambda x: x['rating'])
    print("Most similar to least similar: " + str(comparison_results) + "\n")
    # print("Most similar to " + question['name'] + ": " + str(comparison_results[0]['name']) + " with rating: " + str(comparison_results[0]['rating']) + "\n")
