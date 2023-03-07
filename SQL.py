import sqlite3
from sqlite3 import Error

def create_connection(path):

    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection  #Створили (Підключились) до БД:
connection = create_connection("./country_DB")

def execute_query(connection, query): #виконати задане query
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_countries_table = """
CREATE TABLE IF NOT EXISTS countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  full_country_name TEXT,
  words_in_full_name INTEGER,
  same_letter_count INTEGER,
  flag_url TEXT
);
"""

execute_query(connection, create_countries_table)