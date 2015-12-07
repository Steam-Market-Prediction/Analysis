import json
from pprint import pprint

with open('Market List/Demon Eater.txt') as data_file:
	data = json.load(data_file);

def getMovingAVG(movingAVGLength):
	movingAVG = []
	listOfPoints = []
	for point in data["prices"]:
		listOfPoints.append(point[1])
	for x in range(movingAVGLength,len(data["prices"])):
		avg = 0.0
		for y in range(x-movingAVGLength, x):
			avg = listOfPoints[y] + avg
		movingAVG.append(float(avg/movingAVGLength))
	print movingAVG

#usage: data['prices'][DATE][PRICE]

def generate_population(MA_length):
	array = []
	population = []
	current = 2**MA_length - 1
	while current > 0:
		array = [int(x) for x in str(bin(current))[2:].zfill(MA_length)]
		population.append(array);
		current -= 1
	return population

getMovingAVG(500)
print generate_population(3)
