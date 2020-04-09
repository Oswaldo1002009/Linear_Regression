import csv
import numpy as np
from fastnumbers import isfloat #pip install fastnumbers

#Find all different non-numeric values of the column
def binary_rows(binary, temp_samples, pos):
    local_classes = []
    for i in range(1,len(temp_samples)):
        if not(temp_samples[i][pos] in local_classes):
            local_classes.append(temp_samples[i][pos])
    binary.append(local_classes)
    return binary

def find_bin_classes(sample, temp_sample, binary, column):
    for i in range(len(binary[column])):
        if temp_sample == binary[column][i]:
            sample.append(1)
        else:
            sample.append(0)
    return sample

#otraPrueba
#weatherHistory
#Create samples (all are strings)
with open("otraPrueba.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    temp_samples = []
    lines = 0
    for row in csv_reader:
        line = ','.join(row)
        line = line.split(",")
        temp_samples.append(line)

#Sear for non-numeric columns
binary = []
for i in range(len(temp_samples[1])):
    if isfloat(temp_samples[1][i]):
        binary.append([])
    else:
        binary = binary_rows(binary, temp_samples, i)

#Build the definitive list of samples and y's
samples = []
y = []
for i in range(1,len(temp_samples)):
    sample = []
    for j in range(len(temp_samples[i])-1):
        if isfloat(temp_samples[i][j]):
            sample.append(float(temp_samples[i][j]))
        else:
            sample = find_bin_classes(sample, temp_samples[i][j], binary, j)
    y.append(float(temp_samples[i][-1]))#We assume y is numeric, otherwise the program will crash
    samples.append(sample)
    #print(sample)
#print(binary)


print(samples)
print(y)