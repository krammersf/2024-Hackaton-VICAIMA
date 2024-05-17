import sqlite3
import json

# Open the JSON file
with open('subject/03_combined_data.json', 'r') as f:
    # Load the JSON data from the file
    data = json.load(f)

# Connect to the SQLite database
with sqlite3.connect('PDP/db.sqlite3') as connection:
    # Create a cursor object
    cursor = connection.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS my_table")

    # Get the column names from the first dictionary in the list
    column_names = data[0].keys()

    # Sanitize the column names
    sanitized_column_names = ["".join(c if c.isalnum() else "_" for c in name) for name in column_names]

    # Create a table with the column names
    cursor.execute(f"""
        CREATE TABLE my_table (
            {', '.join(f'{name} TEXT' for name in sanitized_column_names)}
        )
    """)

    # Insert the rows from the JSON file into the table
    for item in data:
        # Only insert the values that correspond to the columns in the table
        values_to_insert = [item.get(name) for name in column_names]
        cursor.execute(f"""
            INSERT INTO my_table ({', '.join(sanitized_column_names)})
            VALUES ({', '.join('?' for _ in sanitized_column_names)})
        """, values_to_insert)

    # Commit the changes
    connection.commit()