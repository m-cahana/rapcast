import json
from collections import Counter
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

rappers = pd.read_csv('./input/rappers.csv')
rappers.Name = rappers.Name.str.lower()
rapper_list = rappers.Name.tolist()
rappers.columns = ['artist', 'era', 'city', 'sub_city', 'region']
rappers.region = rappers.region.replace('Northeast ', 'Northeast')
rappers.region = rappers.region.replace('New Jersey', 'Northeast')
rappers.region = rappers.region.replace('Southeast ', 'Southeast')
rappers.region = rappers.region.replace('Souteast', 'Southeast')
rappers.region = rappers.region.replace('Souteast ', 'Southeast')

rappers.city = rappers.city.replace('Mephis', 'Memphis')
rappers.city = rappers.city.replace('Newark/East Orange', 'Newark')
rappers.city = rappers.city.replace('Long Beach', 'Los Angeles')
rappers.city = rappers.city.replace('Beverly Hills', 'Los Angeles')
rappers.city = rappers.city.replace('New York ', 'New York')
rappers.city = rappers.city.replace('East Orange', 'Orange')
rappers.city = rappers.city.replace('South Orange', 'Orange')
rappers.city = rappers.city.replace('Miami ', 'Miami')
rappers = rappers.set_value(27, 'city', 'Oakland ')
rappers = rappers.set_value(27, 'sub-city', np.NaN)
rappers = rappers.set_value(27, 'region', 'West')


with open('./input/raw_lyrics.json') as f:
    raw = json.load(f)

for artist, lyrics in raw.items():
    raw[artist] = " ".join(lyrics)

df = pd.DataFrame.from_dict(raw, orient = 'index')
df = df.reset_index()
df.columns = ['artist', 'corpus']

df = df[df['artist'].isin(rapper_list)]
df = df.merge(rappers[['artist', 'city']], how='left', on='artist')
df['city_id'] = df['city'].factorize()[0]

region_id_df = df[['city', 'city_id']].drop_duplicates().sort_values('city_id')
region_to_id = dict(region_id_df.values)

id_to_region = dict(region_id_df[['city_id', 'city']].values)

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(df.corpus).toarray()
labels = df.city_id

N = 2
for region, region_id in sorted(region_to_id.items()):
  features_chi2 = chi2(features, labels == region_id)
  indices = np.argsort(features_chi2[0])
  feature_names = np.array(tfidf.get_feature_names())[indices]
  unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
  bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
  print("# '{}':".format(region))
  print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-N:])))
  print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-N:])))


X_train, X_test, y_train, y_test = train_test_split(df['corpus'], df['city'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, y_train)
