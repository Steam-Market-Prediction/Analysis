import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString
from random import randint

with open('Market List/Demon Eater.txt') as data_file:
	data = json.load(data_file);
#data['prices'][DATE][PRICE]

POPULATION_SIZE = 10

def generateRandomPopulation():
	population = []
	lower = len(data['prices']) / 4
	upper = len(data['prices']) * 3 / 4
	for i in range(POPULATION_SIZE):
		population.append(randint(lower,upper))
	return population

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


print intersect_points

a = getMovingAVG(3)
b = getMovingAVG(15)
plt.plot(*zip(*a))
plt.plot(*zip(*b))
plt.show()


bestFitness1 = None
bestFitness2 = None
bestfitnessIntersection = 0
for x in range(0, len(listOfMovingAVG)-2):
	for y in range(x+1, len(listOfMovingAVG)-1):
		l1 = LineString(listOfMovingAVG[x])
		l2 = LineString(listOfMovingAVG[y])

		intersection = l1.intersection(l2)
		intersect_points = [list(p.coords)[0] for p in intersection]
		if len(intersect_points) > bestfitnessIntersection:
			bestFitness1 = x
			bestFitness2 = y
listOfMovingAVG.insert(0, mylist.pop(mylist.index(bestFitness1)))
listOfMovingAVG.insert(1, mylist.pop(mylist.index(bestFitness2)))

population = generateRandomPopulation()
population_MAs = []
for element in population:
	population_MAs.append(getMovingAVG(element))
print population_MAs

