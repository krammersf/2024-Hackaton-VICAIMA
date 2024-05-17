import pandas as pd

data = pd.read_csv('subject/01_BD_Absentismo.csv', encoding='ISO-8859-1', sep=';')
data.to_json('subject/01_BD_Absentismo.json', orient='records')