import pandas as pd

data = pd.read_csv('subject/02_BD_colaboradores.csv', encoding='ISO-8859-1', sep=';')
data.to_json('subject/02_BD_colaboradores.json', orient='records')