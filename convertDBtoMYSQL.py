
# sudo service mysql start
# sudo service mysql status
# mysql -u root -p
# USE my_database;
# SELECT * FROM your_table;
# SELECT Nome, Apelido FROM your_table;

import json
import pymysql
from datetime import datetime

# Load JSON data
with open('subject/03_combined_data.json') as f:
    data = json.load(f)

# Establish connection with MySQL
connection = pymysql.connect(host='localhost',
                             user='42',
                             password='2305',
                             db='my_database')

try:
    with connection.cursor() as cursor:
        # Delete the table if it exists
        cursor.execute("DROP TABLE IF EXISTS `your_table`")

        # Create the table
        cursor.execute("""
        CREATE TABLE `your_table` (
        `NumColab` varchar(255),
        `Nome` varchar(255),
        `Apelido` varchar(255),
        `Departamento` varchar(255),
        `NumAvali` varchar(255),
        `Func` varchar(255),
        `Data` date,
        `Grupo` varchar(255),
        `DirUni` int,
        `Pin` int,
        `Ano` int,
        `FaltaJust` int,
        `FaltaInjust` int
        );
        """)

        for item in data:
            # Convert the date to 'YYYY-MM-DD' format
            item['Data'] = datetime.strptime(item['Data'], '%d/%m/%Y').strftime('%Y-%m-%d')

            # Check if 'Pin' is present
            if 'Pin' in item:
                try:
                    # Try to convert 'Pin' to a string
                    pin_str = str(item['Pin'])
                    # Check if 'Pin' has exactly 4 digits
                    if len(pin_str) == 4 and pin_str.isdigit():
                        # 'Pin' is correct, keep it as a string
                        item['Pin'] = pin_str
                    else:
                        # If 'Pin' does not have exactly 4 digits, set it to None
                        item['Pin'] = None
                except ValueError:
                    # If 'Pin' cannot be converted to a string, set it to None
                    item['Pin'] = None
            else:
                # If 'Pin' is not present, set it to None
                item['Pin'] = None

            # Check the value of 'FaltaInjust'
            falta_injust = item.get('FaltaInjust')
            print(f"FaltaInjust: {falta_injust}")

            # If 'FaltaInjust' is 'N/A', replace it with None
            if falta_injust == 'N/A':
                falta_injust = None

            # Insert the data into the table
            sql = "INSERT INTO `your_table` (`NumColab`, `Nome`, `Apelido`, `Departamento`, `NumAvali`, `Func`, `Data`, `Grupo`, `DirUni`, `Ano`, `FaltaJust`, `FaltaInjust`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (item['NumColab'], item['Nome'], item['Apelido'], item['Departamento'], item['NumAvali'], item['Func'], item['Data'], item['Grupo'], item['DirUni'], item.get('Ano'), item.get('FaltaJust'), falta_injust))

        # Commit the transactions
        connection.commit()

finally:
    # Close the connection
    connection.close()