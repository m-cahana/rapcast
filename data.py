import json
from collections import Counter
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer

rappers = pd.read_csv('rappers.csv')
rappers.Name = rappers.Name.str.lower()
rapper_list = rappers.Name.tolist()
rappers.columns = ['artist', 'era', 'city', 'sub_city', 'region']


with open('raw_lyrics.json') as f:
    raw = json.load(f)  

for artist, lyrics in raw.items():
    raw[artist] = " ".join(lyrics)

df = pd.DataFrame.from_dict(raw, orient = 'index')
df = df.reset_index()
df.columns = ['artist', 'corpus']

df = df[df['artist'].isin(rapper_list)]
df = df.merge(rappers[['artist', 'region']], how='left', on='artist')
df['region_id'] = df['region'].factorize()[0]

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(df.corpus).toarray()
labels = df.artist