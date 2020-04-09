# coding=utf-8
import csv
import numpy as np
from fastnumbers import isfloat #pip install fastnumbers
import math

def x0(samples):
    for i in range(len(samples)):
        if isinstance(samples[i], list):
            samples[i] = [1.0] + samples[i]
        else:
            samples[i] = [1.0, samples[i]]
    return samples

def scaling(samples):
    means = []
    for i in range(len(samples[0])):#Means
        acum = 0
        for j in range(len(samples)):
            acum += samples[j][i]
        acum = acum / len(samples)
        means.append(acum)
    sd = []
    for i in range(len(samples[0])):#standard deviation
        acum = 0
        for j in range(len(samples)):
            acum = acum + (samples[j][i] - means[i])**2
        acum = math.sqrt(acum / len(samples))
        sd.append(acum)
    for i in range(1, len(samples[0])): #New values
        for j in range(len(samples)):
            samples[j][i] = (samples[j][i] - means[i]) / sd[i]
    return samples

def hyp(params, samples):
    hy = []
    for i in range(len(samples)):
        acum = 0
        for j in range(len(params)):
            acum = acum + params[j] * samples[i][j]  # At the end, we get hθ(xi)
        hy.append(acum)
    return hy

def gradient_descent(hyp_x, y, params, samples, alpha):
    new_params = []
    for i in range(len(params)):
        total = 0
        for j in range(len(hyp_x)):
            summatory = (hyp_x[j]-y[j])*samples[j][i]#[hθ(xi)-yi]*xi
            total += summatory
        param = params[i] - total * alpha / len(samples)#θnew = θold - α*(1/m)*total
        new_params.append(param)
    return new_params

def cost_function(errors, hyp_x, y):
    error = 0
    for i in range(len(hyp_x)):
        error += (hyp_x[i] - y[i])**2
    error = error / len(hyp_x)
    errors.append(error)
    return error

###########################################################################
#############################Start the program#############################
###########################################################################

#Find all different non-numeric values of the column
def binary_rows(binary, temp_samples, pos):
    local_classes = []
    for i in range(1,len(temp_samples)):
        if not(temp_samples[i][pos] in local_classes):
            local_classes.append(temp_samples[i][pos])
    binary.append(local_classes)
    return binary

#Classify all non-numeric values with 1's or 0's
def find_bin_classes(sample, temp_sample, binary, column):
    for i in range(len(binary[column])):
        if temp_sample == binary[column][i]:
            sample.append(1)
        else:
            sample.append(0)
    return sample

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
    y.append(float(temp_samples[i][-1]))#We assume y is float, otherwise the program will crash
    samples.append(sample)

params = list(np.zeros(len(samples[0])+1))#+1 is due b in mx + b

alpha = 0.001

__errors__ = []

samples = x0(samples)
samples = scaling(samples)

for i in range(1000):
    hyp_x = hyp(params, samples)
    params = gradient_descent(hyp_x, y, params, samples, alpha)
    print("New params:")
    print(params)
    print("Error: " + str(cost_function(__errors__, hyp_x, y)))

#print("Samples:")
#print(samples)

