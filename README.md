# Rapcast
Predicts where a rapper grew up and started their career based on their lyric corpus

### Playing with the dataset:
```
import json
from collections import Counter

with open('./input/bag_of_words.json') as f:
  bag = json.load(f)

for artist, bag_of_words in bag.items():
  bag[artist] = Counter(bag_of_words)
```
To see most common words for a particular artist:
`bag[<ARTIST>].most_common(<INT>)`

To see how many times an artist says a given word:
`bag[<ARTIST>][<WORD>]`

### View the project website:
https://m-cahana.github.io/rapcast/

