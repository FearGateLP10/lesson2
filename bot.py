from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime
import logging
import ephem
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def get_planet(bot, update):
    text = 'Вызван /ephem'
    logging.info(text)

    try:
        planet_name = update.message.text.split()[1]
        date = datetime.datetime.now()

        ephem_planet = getattr(ephem, planet_name)(datetime.datetime.now().strftime('%Y/%m/%d'))    # (datetime.datetime.today())

        update.message.reply_text(planet_name)
        update.message.reply_text(ephem.constellation(ephem_planet))

    except AttributeError:
        text_except = ('Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Phobos', 'Deimos', 'Jupiter', 'Io', 'Europa', 
            'Ganymede', 'Callisto', 'Saturn', 'Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan', 'Hyperion', 
            'Iapetus', 'Uranus', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Miranda', 'Neptune', 'Pluto'
            )
        update.message.reply_text('Введите название планеты из списка: {}'.format(text_except))


def talk_to_me(bot, update):
    user_text = 'Привет, {}! Ты написал {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: {}, Chat id: {}, message: {}'.format(update.message.chat.username, 
                                                            update.message.chat.id, update.message.text))
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Bot запущен')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("ephem", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()