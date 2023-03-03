import requests
from bs4 import BeautifulSoup as b

def country ():
    URL = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2'
    r = requests.get(URL)
    if r.status_code == 200:
        soup = b(r.text, 'html.parser')
        cauntr_list = []
        img_list = []
        full_name = []
        all_cauntr = soup.find('table', class_='wikitable').find_all('tr')
        for i in all_cauntr[1:]:
            cauntr_list.append(i.find_all("td")[1].find('img', class_='thumbborder').get('alt'))
            img_list.append(i.find_all("td")[1].find('img', class_='thumbborder').get('src'))
            full_name.append(i.find_all("td")[3].text)



        print(full_name)
        print(cauntr_list)
        print(img_list)



        """all_cauntr = soup.find('table', class_='wikitable').find_all('img', class_='thumbborder')
        cauntr_list = []
        img_list = []
        for i in all_cauntr:
            cauntr_list.append(i.get('alt'))
            img_list.append(i.get('src'))"""

        #print(cauntr_list)

"""        
        img = soup.find('img', class_='weatherImg').get('title')
        return {temp_min.text, temp_max.text, img}
    else:
        return {'Місто не знайдено, повторіть спробу.'}
"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    country()


