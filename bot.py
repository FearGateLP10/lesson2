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

    planet_name = update.message.text.split()[1]
    date = datetime.datetime.now()

    # if planet_name == 'Mars':
    #     ephem_planet = ephem.Mars(date.strftime('%Y/%m/%d'))
    # elif planet_name == 'Venus':
    #     ephem_planet = ephem.Venus(date.strftime('%Y/%m/%d'))

    # ephem_planet = ephem.planet_name(datetime.datetime.now().strftime('%Y/%m/%d'))

    ephem_planet = getattr(ephem, planet_name)(datetime.datetime.now().strftime('%Y/%m/%d'))
    # (datetime.datetime.today())

    ephem.constellation(ephem_planet)
    # update.message.reply_text(text)
    update.message.reply_text(planet_name)
    update.message.reply_text(ephem.constellation(ephem_planet))


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