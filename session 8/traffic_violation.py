# Question 1

import csv

male = 0
female = 0
with open('Traffic_Violations.csv') as csv_file :
    rows = csv.DictReader(csv_file)
    for cur_row in rows:
        if(cur_row["Gender"] == "M") :
            male += 1
        else :
            female += 1
print("\nCount of male and female who violated traffic rules in MACOSX\n")
print("Male : {}\nFemale : {}\n".format(male,female))
