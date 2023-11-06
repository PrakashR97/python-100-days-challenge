import random

import pandas
from pandas import *

data_file = pandas.read_csv("data/french_words.csv")
to_learn = data_file.to_dict(orient="records")
print(to_learn)
learn_list = random.choice(to_learn)

to_learn.remove(learn_list)
df = DataFrame(to_learn)
csv_data = df.to_csv("learn_words.csv", index=False)

data = pandas.read_csv("learn_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)
