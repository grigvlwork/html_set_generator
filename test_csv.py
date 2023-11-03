import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('dataset.csv', encoding='utf-8', sep='@')
train, test = train_test_split(df, test_size=0.001, random_state=0)
train.to_json('dataset_train.json', force_ascii=False)
test.to_json('dataset_test.json', force_ascii=False)

