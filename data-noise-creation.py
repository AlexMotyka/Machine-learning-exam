import csv
import math
import random


# file_list = ['G1-Sheet1.csv', 'G2-Sheet1.csv', 'G3-Sheet1.csv', 'G4-Sheet1.csv']
file_list = ['q1.csv', 'q2.csv', 'q3.csv', 'q4.csv', 'q5.csv', 'q6.csv', 'q7.csv', 'q8.csv', 'q9.csv', 'q10.csv', 'q11.csv', 'q12.csv', 'q13.csv', 'q14.csv', 'q15.csv']
added_row_num = 2
for filename in file_list:
    with open(filename) as csvf:
        csvf_read = csv.reader(csvf, delimiter='\t')

        """Stat holders for files"""
        undecided_max = 0
        yes_max = 0
        no_max = 0

        undecided_min = 999
        yes_min = 999
        no_min = 999

        undecided_total = 0
        yes_total = 0
        no_total = 0
        rowcount = 0

        """The new lines will be held in this list"""
        new_csv_lines = []
        yes_list = []
        no_list = []
        undecided_list = []
        """Read all lines and get the totals + average"""
        for row in csvf_read:
            rowcount += 1
            new_csv_lines.append([int(row[0]), int(row[1]), int(row[2])])

            yes_total += int(row[0])
            no_total += int(row[1])
            undecided_total += int(row[2])

            yes_list.append(int(row[0]))
            no_list.append(int(row[1]))
            undecided_list.append(int(row[2]))

            if undecided_min > int(row[2]):
                undecided_min = int(row[2])
            if no_min > int(row[1]):
                no_min = int(row[1])
            if yes_min > int(row[0]):
                yes_min = int(row[0])

            if int(row[0]) > yes_max:
                yes_max = int(row[0])
            if int(row[1]) > no_max:
                no_max = int(row[1])
            if int(row[2]) > undecided_max:
                undecided_max = int(row[2])

        yes_mode = max(yes_list, key=yes_list.count)
        no_mode = max(no_list, key=no_list.count)
        undecided_mode = max(undecided_list, key=undecided_list.count)

        undecided_avg = math.ceil(undecided_total/rowcount)
        yes_avg = math.ceil(yes_total/rowcount)
        no_avg = math.ceil(no_total/rowcount)

        print(yes_avg)
        print(no_avg)
        print(undecided_avg)
        """The new values are obtained through randomness here"""
        for x in range(added_row_num):
            rowcount += 1
            current_total = 100
            random_existing_row = new_csv_lines[random.randrange(0,len(new_csv_lines))]
            new_yes_val = math.floor((random_existing_row[0] + yes_mode)/2)
            new_no_val = math.floor((random_existing_row[1] + no_mode)/2)
            new_undecided_val = math.floor((random_existing_row[2] + undecided_mode) / 2)
            temp_line = [new_yes_val, new_no_val, new_undecided_val]

            if new_yes_val + new_no_val + new_undecided_val < 100:
                diff = 100 - (new_no_val + new_yes_val + new_undecided_val)
                rand_index = random.randrange(0,3)
                temp_line[rand_index] += diff
            new_csv_lines.append(temp_line)
            yes_total += new_yes_val
            no_total += new_no_val
            undecided_total += new_undecided_val
            print(temp_line)

        undecided_avg = math.ceil(undecided_total / rowcount)
        yes_avg = math.ceil(yes_total / rowcount)
        no_avg = math.ceil(no_total / rowcount)

        print(yes_avg)
        print(no_avg)
        print(undecided_avg)
        new_file_name = filename.split('.')[0] + '_addedVals.csv'
        new_f = open(new_file_name, 'w', newline='')
        with new_f:
            writer = csv.writer(new_f)
            writer.writerows(new_csv_lines)
