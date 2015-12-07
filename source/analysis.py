import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

with open('Market List/Demon Eater.txt') as data_file:
	data = json.load(data_file);
#data['prices'][DATE][PRICE]

def getMovingAVG(movingAVGLength):
	movingAVG = []
	listOfPoints = []
	for point in data["prices"]:
		listOfPoints.append(point[1])
	for x in range(movingAVGLength,len(data["prices"])):
		avg = 0.0
		for y in range(x-movingAVGLength, x):
			avg = listOfPoints[y] + avg
		point = [x,float(avg/movingAVGLength)]
		movingAVG.append(point)
	return movingAVG


a = getMovingAVG(3)
plt.plot(*zip(*a))
plt.show()