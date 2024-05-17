

# correr no terminal: e vai abrir janela:
# mongodb-compass

from pymongo import MongoClient
import json

# Carregue os dados do arquivo JSON
with open('subject/03_combined_data.json', 'r') as f:
    data = json.load(f)

# Crie uma conexão com o MongoDB
client = MongoClient('mongodb+srv://admin:Vicaima2024@vicaima.pg9i3t6.mongodb.net/?retryWrites=true&w=majority&appName=vicaima')

# Acesse o banco de dados 'mydatabase' e a coleção 'mycollection'
db = client['naturdorDB']

# Insira os dados na coleção
db.Users.insert_many(data)