import requests
from bs4 import BeautifulSoup as b
import logging
import json

logger = logging.getLogger(__name__)
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


def cauntr_info(name):
    for dict_cauntr in pars_country():
        if dict_cauntr['country'] == name:
            return dict_cauntr
    return "Країну не знайдено"





if __name__ == '__main__':

    with open('in.txt', 'r', encoding='utf-8') as file:
        name_caunt = file.read()
        file.close()
    with open('caunt.json', 'w') as file_2:
        json.dump(cauntr_info(name_caunt), file_2, indent=4)
        file_2.close()


