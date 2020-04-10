import csv
import math
import random


file_list = ['G1-Sheet1.csv', 'G2-Sheet1.csv', 'G3-Sheet1.csv', 'G4-Sheet1.csv']
added_row_num = 20
for filename in file_list:
    with open(filename) as csvf:
        csvf_read = csv.reader(csvf, delimiter=',')

        """Stat holders for files"""
        undecided_max = 0
        undecided_total = 0
        rowcount = 0

        """The new lines will be held in this list"""
        new_csv_lines = []

        """Read all lines and get the totals + average"""
        for row in csvf_read:
            rowcount += 1
            new_csv_lines.append(row)
            undecided_total += int(row[2])
            if int(row[2]) > undecided_max:
                undecided_max = int(row[2])

        undecided_avg = math.ceil(undecided_total/rowcount)

        """The new values are obtained through randomness here"""
        for x in range(added_row_num + 1):
            temp_line = []
            current_total = 100
            temp_undecided = 0

            """Two coin flips to make multiple pathways of randomness"""
            coin_flip1 = random.randrange(2)
            coin_flip2 = random.randrange(2)

            """One path uses the max value, while the other uses the average"""
            if coin_flip1 == 0:
                temp_undecided = random.randrange(undecided_avg+1)
                current_total -= temp_undecided
            else:
                temp_undecided = random.randrange(undecided_max+1)
                current_total -= temp_undecided

            """Two paths to use either yes or no first"""
            if coin_flip2 == 0:
                temp_yes = random.randrange(current_total+1)
                current_total -= temp_yes
                temp_no = current_total
                temp_line = [str(temp_yes), str(temp_no), str(temp_undecided)]
                new_csv_lines.append(temp_line)
            else:
                temp_no = random.randrange(current_total + 1)
                current_total -= temp_no
                temp_yes = current_total
                temp_line = [str(temp_yes), str(temp_no), str(temp_undecided)]
                new_csv_lines.append(temp_line)

        new_file_name = filename.split('.')[0] + '_addedVals.csv'
        new_f = open(new_file_name, 'w', newline='')
        with new_f:
            writer = csv.writer(new_f)
            writer.writerows(new_csv_lines)
