"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Sun', 'Moon', 'Phobos',
           'Deimos', 'Io', 'Europa', 'Ganymede', 'Callisto', 'Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea',
           'Titan', 'Hyperion', 'Iapetus', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Miranda']

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def about_planet(update, context):
    print('Вызван /planet')
    user_planet = update.message.text.split()
    if user_planet[1] in planets:
        planet_obj = getattr(ephem, user_planet[1])
        date = datetime.date.today()
        planet = planet_obj(date)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet[1]} сегодня находится в созвездии {const[1]}')
    else:
        update.message.reply_text(f'{user_planet[1]} - такой планеты я не знаю')
'''
    try:
        user_planet[1] in planets:
        planet_obj = getattr(ephem, user_planet[1])
        date = datetime.date.today()
        planet = planet_obj(date)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet[1]} сегодня находится в созвездии {const[1]}')
    except attribute error:
        update.message.reply_text(f'{user_planet[1]} - такой планеты я не знаю')
'''
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", about_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
