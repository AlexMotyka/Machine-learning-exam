import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

file_list = ['Master.csv']
answers_arr = []
input_arr = []
# Get the data from the csv file
for filename in file_list:
    with open(filename) as csvf:
        csvf_read = csv.reader(csvf, delimiter=',')

        for row in csvf_read:
            input_arr.append([int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]), int(row[16]), int(row[17]), int(row[18]), int(row[19]), int(row[20]), int(row[21]), int(row[22]), int(row[23]), int(row[24]), int(row[25]), int(row[26]), int(row[27]), int(row[28]), int(row[29]), int(row[30]), int(row[31]), int(row[32]), int(row[33]), int(row[34]), int(row[35]), int(row[36]), int(row[37]), int(row[38]), int(row[39]), int(row[40]), int(row[41]), int(row[42]), int(row[43]), int(row[44])])
            answers_arr.append(int(row[45]))

# convert the lists to numpy array for performance, and then zip them together
train_data = np.asanyarray(input_arr)
correct_outputs = np.asanyarray(answers_arr)
data_and_labels = list(zip(train_data, correct_outputs))

# Define variables
n_samples = len(train_data)
print("number of samples: " + str(n_samples))

x = train_data.reshape((n_samples, -1))
print("train data shape: " + str(x.shape))

y = correct_outputs
print("answers data shape: " + str(y.shape) + "\n")

# split the set and use 30 percent as test data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

print("Expected Prediction: " + str(y_test))
print("Actual Predictions:  " + str(y_pred))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
