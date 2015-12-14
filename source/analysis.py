import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import random
from shapely.geometry import LineString
from random import randint
import statistics

with open('Market List/Fiery Soul of the Slayer.txt') as data_file:
	data = json.load(data_file);
#data['prices'][DATE][PRICE]

POPULATION_SIZE = 50

def generateRandomPopulation():
	population = []
	lower = 20
	upper = 200
	for i in range(POPULATION_SIZE*2):
		population.append(randint(lower,upper))
	return population

def generateNewLength():
	population = []
	lower = 20
	upper = 200
	for i in xrange(0,2):
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

def getTotalAVG():
	totalAVG = 0
	listOfPoints = []
	for point in data["prices"]:
		listOfPoints.append(point[1])
	for x in range(0,len(data["prices"])):
		totalAVG = listOfPoints[x] + totalAVG

	return totalAVG/len(data["prices"])
'''
a = getMovingAVG(31)
b = getMovingAVG(36)
plt.plot(*zip(*a))
plt.plot(*zip(*b))
plt.show()
'''

class Population:

	def __init__(self):
		self.standardDeviation = []
		self.firstBUY = True
		self.firstSpend = 0
		self.listOfMovingAVG = []
		self.BUY = True
		self.listOfMovingLength = generateRandomPopulation()
		for x in xrange(0,len(self.listOfMovingLength),2):
			newTuple = (getMovingAVG(self.listOfMovingLength[x]),getMovingAVG(self.listOfMovingLength[x+1]))
			self.listOfMovingAVG.append((newTuple, self.listOfMovingLength[x], self.listOfMovingLength[x+1]))
		

	def evaluate(self):
		self.firstBUY = True
		self.BUY = None
		self.firstSpend = 0
		self.selectionResults = []
		for pair in self.listOfMovingAVG:
			currentStock = 0
			#print "pair: ", type(pair[0][0])

			l1 = LineString(pair[0][0])
			l2 = LineString(pair[0][1])
			intersection = l1.intersection(l2)
			try:
				intersect_points = [list(p.coords)[0] for p in intersection]
			except:
				intersect_points = list(intersection.coords)

			while(len(intersect_points) == 1):
				newLength = generateNewLength()
				pair = ((getMovingAVG(newLength[0]), getMovingAVG(newLength[1])), newLength[0], newLength[1])
				l1 = LineString(pair[0][0])
				l2 = LineString(pair[0][1])
				intersection = l1.intersection(l2)
				try:
					intersect_points = [list(p.coords)[0] for p in intersection]
				except:
					intersect_points = list(intersection.coords)


			listOfXinl1 = [i[0] for i in list(l1.coords)]
			listOfXinl2 = [j[0] for j in list(l2.coords)]
			tempProfit = 0

			for item in intersect_points:
				self.standardDeviation.append(item[1])
				if pair[1] > pair[2]: # first is short term, second is long term
					if pair[0][0][listOfXinl1.index((float(int(item[0]) + 1)))][1] > pair[0][1][listOfXinl2.index((float(int(item[0]) + 1)))][1]:
						tempProfit = tempProfit - item[1] #buy
						currentStock = currentStock + 1
						if self.firstBUY is True:
							self.firstSpend = item[1]
							self.firstBUY = False
						self.BUY = True
					else:
						tempProfit = tempProfit + (item[1] * currentStock) #sell
						currentStock = 0
						self.BUY = False
				else: # x is long term, y is short term
					if pair[0][1][listOfXinl2.index((float(int(item[0]) + 1)))][1] > pair[0][0][listOfXinl1.index((float(int(item[0]) + 1)))][1]:
						tempProfit = tempProfit + (item[1] * currentStock) #selectionResults
						currentStock = 0
						self.BUY = False
					else:
						tempProfit = tempProfit - item[1] #buy
						currentStock = currentStock + 1
						if self.firstBUY is True:
							self.firstSpend = item[1]
							self.firstBUY = False
						self.BUY = True


			evaluatePairFitness = (pair, tempProfit)

			self.selectionResults.append(evaluatePairFitness)

		
		
	def select(self):
		self.selectionResults = sorted(self.selectionResults, key = lambda x:x[1], reverse = True)

	def crossover(self):
		CROSSOVER_RATE = 1
		newPop = []
		newPop.append(self.selectionResults[0][0])
		newPop.append(self.selectionResults[1][0])
		for i in xrange(2, len(self.selectionResults),2):
			isCrossover = random.uniform(0,1)
			if isCrossover < CROSSOVER_RATE:
				'''
				crossOver1 = (self.selectionResults[i][0][0][0], self.selectionResults[i+1][0][0][1])
				crossOverTuple1 = (crossOver1, self.selectionResults[i][0][1], self.selectionResults[i+1][0][2])
				crossOver2 = (self.selectionResults[i+1][0][0][0], self.selectionResults[i][0][0][1])
				crossOverTuple2 = (crossOver2, self.selectionResults[i+1][0][1], self.selectionResults[i][0][2])
				'''
				crossOver1 = (self.selectionResults[i][0][0][0], self.selectionResults[0][0][0][1])
				crossOverTuple1 = (crossOver1, self.selectionResults[i][0][1], self.selectionResults[i+1][0][2])
				crossOver2 = (self.selectionResults[i+1][0][0][0], self.selectionResults[1][0][0][1])
				crossOverTuple2 = (crossOver2, self.selectionResults[i+1][0][1], self.selectionResults[i][0][2])
				newPop.append(crossOverTuple1)
				newPop.append(crossOverTuple2)

			else:
				newPop.append(self.selectionResults[i][0])
				newPop.append(self.selectionResults[i+1][0])

		self.listOfMovingAVG = newPop

		
	def mutate(self):
		MUTATION_RATE = 0.3
		newPop = []
		newPop.append(self.selectionResults[0][0])
		newPop.append(self.selectionResults[1][0])
		for i in xrange(2, len(self.selectionResults)):
			isMutate = random.uniform(0,1)
			if isMutate < MUTATION_RATE:
				newLength = generateNewLength()
				newMutation = (self.selectionResults[i][0][0][0], getMovingAVG(newLength[0]))
				newGene = (newMutation, self.selectionResults[i][0][1], newLength[0])
				newPop.append(newGene)
			else:
				newPop.append(self.selectionResults[i][0])

		self.listOfMovingAVG = newPop




def start_algorithm():
	newPopulation = Population();
	maxProfit = 0
	numGenerations = 0
	while(numGenerations < 2000):
		newPopulation.evaluate()
		if newPopulation.selectionResults[0][1] > maxProfit:
			maxProfit = newPopulation.selectionResults[0][1]
			print "Generation: ",numGenerations
			print "Standard Deviation: ", statistics.pstdev(newPopulation.standardDeviation)
			print "New Max: " ,maxProfit, "Length: ", newPopulation.selectionResults[0][0][1], newPopulation.selectionResults[0][0][2], " Max Return: ", ((maxProfit + newPopulation.firstSpend) /newPopulation.firstSpend) * 100, " Buy: ", newPopulation.BUY
		print numGenerations
		newPopulation.select()
		newPopulation.crossover()
		newPopulation.mutate()
		numGenerations = numGenerations + 1

if __name__ == "__main__":
	start_algorithm()
