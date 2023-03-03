#import telebot
import requests
from bs4 import BeautifulSoup as b  # from https://pypi.org/



def pohoda (city):
    URL = 'https://ua.sinoptik.ua/погода-'
    r = requests.get(URL + str(city))
    if r.status_code == 200:
        soup = b(r.text, 'html.parser')
        temp_min = soup.find('div', class_='min')
        temp_max = soup.find('div', class_='max')
        img = soup.find('img', class_='weatherImg').get('src')
        return {temp_min.text, temp_max.text, img}
    else:
        return {'Місто не знайдено, повторіть спробу.'}



bot_API = '5042073234:AAFFJ4R-iVGcOm-iK9YAzilO_ee7Ud9m7HA'
bot = telebot.TeleBot(bot_API)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, "Вітаю, введіть ваше місто:")
@bot.message_handler(content_types=['text'])
def send_temp(message):
    for i in pohoda(message.text):
        bot.send_message(message.chat.id, i) #"Сьогодні в місті " + message.text + ' ' + i)
bot.polling()

