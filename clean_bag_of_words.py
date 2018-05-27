import json
from collections import Counter
import pandas as pd 

rappers = pd.read_csv('rappers.csv')
rapper_list = rappers.Name.str.lower().tolist()

with open('bag_of_words.json') as f:
    bag = json.load(f)  

for artist, bag_of_words in bag.items():
    bag[artist] = Counter(bag_of_words)

with open('master_bag.json') as f:
    master_bag = json.load(f)  

def greater_than_5(master_bag):
	res = []
	for word, count in master_bag.items():
		if count > 5:
			res.append(word)
	return res

valid_words = greater_than_5(master_bag)

clean_bag = {}
for artist, bag_of_words in bag.items():
    if artist in rapper_list:
        print(artist)
        if artist not in clean_bag:
            clean_bag[artist] = {}
        for word, count in bag_of_words.items():
            if word in valid_words:
                clean_bag[artist][word] = count

for artist, bag_of_words in clean_bag.iteritems():
    clean_bag[artist] = Counter(bag_of_words)

clean_bag_classes = {}
for artist, bag_of_words in clean_bag.iteritems():
    clean_bag[artist] = Counter(bag_of_words)

