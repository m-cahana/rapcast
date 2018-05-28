import json
import pandas as pd 
from collections import Counter

data = [0] * 4

with open('./data/lyrics_1980s.json') as f:
    data[0] = json.load(f) 
with open('./data/lyrics_1990s.json') as f:
    data[1] = json.load(f) 
with open('./data/lyrics_2000s.json') as f:
    data[2] = json.load(f) 
with open('./data/lyrics_2010s.json') as f:
    data[3] = json.load(f) 

for i in range(len(data)):
    if i==0:
        artists = data[i]
    else:
        for artist,verses in data[i].items():
            if artist in artists:
                for verse in verses:
                    artists[artist].append(verse)
            else:
                artists[artist] = verses

with open('./input/raw_lyrics.json', 'w') as outfile:
        json.dump(artists, outfile) 

for artist, verses in artists.items():
    artists[artist] = " ".join(verses)
    artists[artist] = Counter(artists[artist].split())

with open('./input/bag_of_words.json', 'w') as outfile:
        json.dump(artists, outfile) 
