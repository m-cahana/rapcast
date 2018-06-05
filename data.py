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
import matplotlib.pyplot as plt

rappers = pd.read_csv('./input/rappers.csv')
rappers.Name = rappers.Name.str.lower()
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
rappers.era = rappers.era.replace('1990s ', '1990s')
rappers.sub_city.fillna(rappers.city, inplace=True)
rappers.sub_city.replace('Harlem ', 'Harlem')
rappers.sub_city.replace('Joliest', 'Joliet')
rappers.sub_city.replace('Harlem/New York City', 'Harlem')
rappers.sub_city.replace('Queens/Brooklyn', 'Queens')

era = input('era: ')
if (era=='1980s' or era=='1990s' or era=='2000s' or era=='2010s'):
    rappers = rappers[rappers.era==era]
rapper_list = rappers.artist.tolist()

with open('./input/raw_lyrics.json') as f:
    raw = json.load(f)

for artist, lyrics in raw.items():
    raw[artist] = " ".join(lyrics)

df = pd.DataFrame.from_dict(raw, orient = 'index')
df = df.reset_index()
df.columns = ['artist', 'corpus']

location = input('location: ')
while (location!='region' and location!='city' and location!='sub_city'):
    location = input('try again! Pick from region, city or sub_city: ')


df = df[df['artist'].isin(rapper_list)]
df = df.merge(rappers[['artist', location]], how='left', on='artist')
df['region_id'] = df[location].factorize()[0]

region_id_df = df[[location, 'region_id']].drop_duplicates().sort_values('region_id')
region_to_id = dict(region_id_df.values)

id_to_region = dict(region_id_df[['region_id', location]].values)

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(df.corpus).toarray()
labels = df.region_id

N = 2
text_file = open("./output/" + str(era) + str(location) + "_grams.txt", "w")
for region, region_id in sorted(region_to_id.items()):
  features_chi2 = chi2(features, labels == region_id)
  indices = np.argsort(features_chi2[0])
  feature_names = np.array(tfidf.get_feature_names())[indices]
  unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
  bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
  text_file.write("# '{}':".format(region))
  text_file.write('\n')
  text_file.write("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-N:])))
  text_file.write('\n')
  text_file.write("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-N:])))
  text_file.write('\n')
text_file.close()

X_train, X_test, y_train, y_test = train_test_split(df['corpus'], df[location], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, y_train)

X_train, X_test, y_train, y_test = train_test_split(df['corpus'], df[location], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, y_train)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(random_state=0),
]
CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []
for model in models:
  model_name = model.__class__.__name__
  accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)
  for fold_idx, accuracy in enumerate(accuracies):
    entries.append((model_name, fold_idx, accuracy))
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])
import seaborn as sns
sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df,
              size=8, jitter=True, edgecolor="gray", linewidth=2)
plt.savefig('./figures/' + str(era) + str(location) + '_box.pdf')

model = LinearSVC()
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index, test_size=0.33, random_state=0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(conf_mat, annot=True, fmt='d',
            xticklabels=region_id_df.values, yticklabels=region_id_df.values)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.savefig('./figures/'+ str(era) + str(location) + '_matrix.pdf')
