import pandas as pd
import numpy as np
import re
from nltk import word_tokenize
from nltk.corpus import wordnet
import pickle

def feature_extraction_approach_2(name):
	consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
	vowels = ['a','e','i','o','u']
	bobua_consonants = ['b','l','m','n']
	bobua_vowels = ['u','o']
	kiki_consonants = ['k','p','t']
	kiki_vowels = ['i','e']
	number_of_consonants = 0
	number_of_vowels = 0
	number_of_bobua_consonants = 0
	number_of_bobua_vowels = 0
	number_of_kiki_consonants = 0
	number_of_kiki_vowels = 0
	last_character = 0
	len_of_name = 0
	featuress = []
	name_array = list(name)
	for name in name_array:
		if name in consonants:
			number_of_consonants = number_of_consonants + 1
			if name in bobua_consonants:
				number_of_bobua_consonants = number_of_bobua_consonants + 1
			elif name in kiki_consonants:
				number_of_kiki_consonants = number_of_kiki_consonants + 1
		elif name in vowels:	
			number_of_vowels = number_of_vowels + 1
			if name in bobua_vowels:
				number_of_bobua_vowels = number_of_bobua_vowels + 1
			elif name in kiki_vowels:
				number_of_kiki_vowels = number_of_kiki_vowels + 1
	if name[-1] in vowels:
		last_character = 1
	len_of_name = len(name_array)	
	features = [number_of_consonants,number_of_vowels,number_of_bobua_consonants,number_of_bobua_vowels,number_of_kiki_consonants,number_of_kiki_vowels,last_character,len_of_name] 	
	return features

def model(data):
	dataframe_to_parse = data

	dataframe_to_parse['noc'] = 0
	dataframe_to_parse['nov'] = 0
	dataframe_to_parse['nobc'] = 0
	dataframe_to_parse['nobv'] = 0
	dataframe_to_parse['nokc'] = 0
	dataframe_to_parse['nokv'] = 0
	dataframe_to_parse['last'] = 0
	dataframe_to_parse['len'] = 0

#data['one-gram'] = [one_gram[ii] for ii in range(len(one_gram))]
#data['bi-gram'] = [bi_gram[ii] for ii in range(len(bi_gram))]
#data['tri-gram'] = [tri_gram[ii] for ii in range(len(tri_gram))]
	noc = []
	nov = []
	nobc = []
	nobv = []
	nokc = []
	nokv = []
	last = []
	leng = []

	#print "Starting feature Extractiont"
	name_list = []
	for name in data.Firstname:
		name_list.append(name)
	for ii in range(len(name_list)):
		feature = feature_extraction_approach_2(name_list[ii])
		noc.append(feature[0])
		nov.append(feature[1])
		nobc.append(feature[2])
		nobv.append(feature[3]) 
		nokc.append(feature[4])
		nokv.append(feature[5])
		last.append(feature[6])
		leng.append(feature[7])

	#print "In between feature Extraction"
	data['noc'] = [noc[ii] for ii in range(len(noc))]
	data['nov'] = [nov[ii] for ii in range(len(nov))]
	data['nobc'] = [nobc[ii] for ii in range(len(nobc))]
	data['nobv'] = [nobv[ii] for ii in range(len(nobv))]
	data['nokc'] = [nokc[ii] for ii in range(len(nokc))]
	data['nokv'] = [nokv[ii] for ii in range(len(nokv))]
	data['last'] = [last[ii] for ii in range(len(last))]
	data['len'] = [leng[ii] for ii in range(len(leng))]

	dataframe_to_parse = dataframe_to_parse.drop(['OrderId','Firstname'],axis = 1)

	#print "Running model on data"
	dataframe_to_parse = dataframe_to_parse.values
	loaded_model = pickle.load(open('dataModel.sav','rb'))

	result = loaded_model.predict(dataframe_to_parse)

	data['Gender'] = 0

	data['Gender'] = [result[ii] for ii in range(len(result))]

	data = data.drop(['noc','nov','nobc','nobv','nokc','nokv','last','len'],axis = 1)

	return data