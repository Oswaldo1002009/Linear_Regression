import csv
import numpy as np

with open("weatherHistory.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    temp_samples = []
    for row in csv_reader:
        line = ','.join(row)
        line = line.split(",")
        temp_samples.append(line)

def just_hours(temp_samples):
    for i in range(1,len(temp_samples)):
        s = str(temp_samples[i][0])
        temp_samples[i][0] = s[11:19]
    return temp_samples

just_hours(temp_samples)

for i in range(100):
    print(temp_samples[i])
