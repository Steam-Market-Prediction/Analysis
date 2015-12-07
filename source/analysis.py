import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

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
		movingAVG.append((x,float(avg/movingAVGLength)))
	return movingAVG

l1 = LineString(getMovingAVG(3))
l2 = LineString(getMovingAVG(15))

intersection = l1.intersection(l2)
intersect_points = [list(p.coords)[0] for p in intersection]
print intersect_points

a = getMovingAVG(3)
b = getMovingAVG(15)
plt.plot(*zip(*a))
plt.plot(*zip(*b))
plt.show()
