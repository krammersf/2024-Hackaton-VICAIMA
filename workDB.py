
import subprocess

# Execute o script convertingDB.py
subprocess.run(["python3", "ConvertingDB.py"])
subprocess.run(["python3", "ConvertingAbs.py"])

import json

# Abra o arquivo json e carregue os dados numa variável
with open('subject/02_BD_colaboradores.json', 'r') as f:
    data1 = json.load(f)

# Renomeie a chave em cada dicionário
for item in data1:
    item['NumColab'] = item.pop('N\u00ba colaborador')
    item['NumAvali'] = item.pop("N\u00ba avaliador \n(= n\u00ba colaborador)")
    item['Func'] = item.pop("Fun\u00e7\u00e3o")
    item['Data'] = item.pop("Data de Admiss\u00e3o")
    item['Grupo'] = item.pop("Grupo Funcional:")
    item['DirUni'] = item.pop("Diretor Unidade\n(= n\u00ba colaborador)")

# Trim espacos em branco
for item in data1:
    item['Nome'] = item['Nome'].strip()

# Preencha com zeros a esquerda
for item in data1:
    item['NumColab'] = str(item['NumColab']).zfill(2)
    item['NumAvali'] = str(item['NumAvali']).zfill(2)

# Adicione o campo 'Pin'
for item in data1:
    item['Pin'] = str(item['NumColab']).zfill(4)

# Abra o outro arquivo json e carregue os dados numa outra variável
with open('subject/01_BD_Absentismo.json', 'r') as f:
    data2 = json.load(f)

for item in data2:
    item['NumColab'] = item.pop("N\u00famero")
    item['FaltaJust'] = item.pop("Faltas Justificadas (Horas)")

# Preencha com zeros a esquerda
for item in data2:
    item['NumColab'] = str(item['NumColab']).zfill(2)

# Junte as bases de dados
for item1 in data1:
    for item2 in data2:
        if item1['NumColab'] == item2['NumColab']:
            item1['Ano'] = item2.get('Ano', 0)
            item1['FaltaJust'] = item2.get('FaltaJust', 0)
            item1['FaltaInjust'] = item2.get("Faltas Injustificadas (Horas)", 0)

with open('subject/03_combined_data.json', 'w') as f:
    json.dump(data1, f)

# Nomes das variáveis
var_names = [
    'NumColab',
    'Nome',
    'Apelido',
    'NumAvali',
    'Departamento',
    'Func',
    'Data',
    'Grupo',
    'DirUni',
    'Pin',
    'Ano',
    'FaltaJust',
    'FaltaInjust'
]

# Imprimir os nomes das variáveis
print(' | '.join(var_names))

# Loop para imprimir os dados
for item in data1:
    info = [
        str(item['NumColab']),
        str(item['Nome']),
        str(item['Apelido']),
        str(item['NumAvali']),
        str(item['Departamento']),
        str(item['Func']),
        str(item['Data']),
        str(item['Grupo']),
        str(item['DirUni']),
        str(item['Pin']),
        str(item['Ano']) if 'Ano' in item else 'N/A',
        str(item['FaltaJust']) if 'FaltaJust' in item else 'N/A',
        str(item['FaltaInjust']) if 'FaltaInjust' in item else 'N/A'
    ]
    print(' | '.join(info))