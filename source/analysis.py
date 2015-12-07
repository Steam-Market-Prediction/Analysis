import json
from pprint import pprint

with open('Market List/Demon Eater.txt') as data_file:
	data = json.load(data_file);

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


print generate_population(3)