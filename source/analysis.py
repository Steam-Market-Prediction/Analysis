import json
from pprint import pprint

with open('Market List/Demon Eater.txt') as data_file:
	data = json.load(data_file);

#usage: data['prices'][DATE][PRICE]