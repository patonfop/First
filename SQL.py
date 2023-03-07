import sqlite3
from sqlite3 import Error
import requests
from bs4 import BeautifulSoup as b
import logging
import json

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
""" #запит на Створення нової таблиці

execute_query(connection, create_countries_table)


def pars_country ():
    URL = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2'
    r = requests.get(URL)
    if r.status_code == 200:
        soup = b(r.text, 'html.parser')
        all_cauntr = soup.find('table', class_='wikitable').find_all('tr')
        finish_list = []
        lst_leter_cauntr = list((s.find_all("td")[1].find('img', class_='thumbborder').get('alt')[0]) for s in all_cauntr[1:])
        for i in all_cauntr[1:]:
            f_name = i.find_all("td")[3].text[:-1]
            cauntr = i.find_all("td")[1].find('img', class_='thumbborder').get('alt')
            finish_list.append({"country": cauntr,
                           "full_country_name": f_name,
                           "words_in_full_name": len(f_name.split(' ')),
                           "same_letter_count": lst_leter_cauntr.count(f_name[0]),
                           "flag_url": i.find_all("td")[1].find('img', class_='thumbborder').get('src')[2:]})
        return finish_list
    else:
        return 'Помилка в URL або ж сайт недоступний.'


insert_users = """
    INSERT INTO
        countries (name, full_country_name, words_in_full_name, same_letter_count,flag_url)
    VALUES
""" + ",\n".join(pars_country ()) + ";"

print(insert_users)