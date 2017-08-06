import pandas as pd
import numpy as np
import re
from nltk import word_tokenize
from nltk.corpus import wordnet

def main(data):

	print "Data is getting Cleaned"

	columns = ['OrderId','Firstname']

	data.columns = columns

	name_list=  []
	name_value= []

	data = data.dropna(subset = ['Firstname'])

	for name in data.Firstname:
		name_list.append(name)

	for name in name_list:
		if not re.search(r'[a-zA-Z]',name):
				name_value.append(name)

	for name in name_value:
		data = data[data.Firstname != name]

	name_list = []
	name_value = []

	for name in data.Firstname:
		name_list.append(name)

	print "Midway point 1"

	for name in name_list:
		if re.search(r'[0-9]',name):
			name_value.append(name)

	for name in name_value:
		data = data[data.Firstname != name]

	name_list = []
	name_value =[]

	for name in data.Firstname:
		name_list.append(name)

	for name in name_list:
		if re.search(r'[,.!@#$%^&*]',name):
			name_value.append(name)

	for name in name_value:
		data = data[data.Firstname != name]

	print "midway point 2"
	name_list = []
	name_value = []

	for name in data.Firstname:
		name_list.append(name)

	for name in name_list:
		value = word_tokenize(name)
		name_value.append(value[0])

	data.Firstname = [name_value[ii] for ii in range(len(name_value))]

	data.Firstname = map(lambda x:x.lower(),data.Firstname)

	print "midway point 3"
	name_list = []
	name_value =[]

	for name in data.Firstname:
		name_list.append(name)

	for name in name_list:
		if len(name) <=2:
			name_value.append(name)

	for name in name_value:
		data = data[data.Firstname != name]

	print "midway point 4"
	return data				