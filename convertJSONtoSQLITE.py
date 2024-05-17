import json
import sqlite3

# Read the JSON file
with open('subject/03_combined_data.json', 'r') as f:
    data = json.load(f)

# Connect to the SQLite database
conn = sqlite3.connect('PDP/db.sqlite3')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute("""
    CREATE TABLE IF NOT EXISTS home_collaborators (
        id INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Apelido TEXT NOT NULL,
        Departamento TEXT NOT NULL,
        NumColab INTEGER NOT NULL,
        NumAvali INTEGER NOT NULL,
        Func TEXT NOT NULL,
        Data TEXT NOT NULL,
        Grupo TEXT NOT NULL,
        DirUni INTEGER NOT NULL
    )
""")

# Iterate over the data and insert each row into the database
for row in data:
    if row['DirUni'] is None:
        continue  # Skip this row if DirUni is None
    c.execute("""
        INSERT INTO home_collaborators (Nome, Apelido, Departamento, NumColab, NumAvali, Func, Data, Grupo, DirUni)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (row['Nome'], row['Apelido'], row['Departamento'], row['NumColab'], row['NumAvali'], row['Func'], row['Data'], row['Grupo'], row['DirUni']))
# Commit the changes and close the connection
conn.commit()
conn.close()