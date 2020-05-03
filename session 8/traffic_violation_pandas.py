# Question 2

import pandas as pd


male = 0
female = 0
# reading csv file   
data = pd.read_csv('Traffic_Violations.csv')
for value in data.Gender :
    if (value == "M") :
        male += 1
    else :
        female += 1
print("\nCount of male and female who violated traffic rules in MACOSX\n")
print("Male : {}\nFemale : {}\n".format(male,female))

