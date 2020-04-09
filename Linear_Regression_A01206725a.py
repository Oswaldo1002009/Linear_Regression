# coding=utf-8
import numpy
import math
params = [0, 0] #x0, x1, ...
samples= [59, 52, 44, 51, 42]
y= [56, 63, 55, 50, 66]

#params = [0, 0, 0]
#samples = [[1,1],[2,2],[3,3],[4,4],[5,5],[2,2],[3,3],[4,4]]
#y = [2,4,6,8,10,2,5.5,16]

params = [0.3, 0.5, 0.3]
samples = [[0.5,1.5],[0.8,1.5],[0.9,2.1],[0.2,3],[0.2,8],[2.5,2.7],[0.5,6.1]]
#samples = [[0.17142857142857143, 0.07857142857142858], [0.2914285714285715, 0.07857142857142858], [0.33142857142857146, 0.15357142857142858], [0.051428571428571435, 0.26607142857142857], [0.051428571428571435, 0.8910714285714286], [0.9714285714285713, 0.2285714285714286], [0.17142857142857143, 0.6535714285714286]]
y=[100,250,162,200,70,80,120]

alpha = 0.001

for i in range(len(samples)):
	if isinstance(samples[i], list):
		samples[i]=  [1.0]+samples[i]
	else:
		samples[i]=  [1.0,samples[i]]

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

def new_params(params, samples, y, alpha):
	np = []
	for n in range(len(params)):
		total = 0
		for i in range(len(samples)):
			acum = 0
			for j in range(len(params)):
				acum = acum + params[j]*samples[i][j]#At the end, we get hθ(xi)
			acum = (acum - y[i])#hθ(xi) - yi
			acum = acum * samples[i][n]#[h(x) - y] * xn
			total += acum
		total = total * alpha / (1 * len(samples))
		np.append(params[n] - total)
	return np

def error(params, samples, y):
	return 1

samples = scaling(samples)
#print(samples)

for i in range(1000):
	print(params)
	params = new_params(params, samples, y, alpha)
	print("New params")
	print(params)