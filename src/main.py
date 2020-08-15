import random

import telebot
from youtubesearchpython.videos__search import SearchVideos as searchYoutube

bot = telebot.TeleBot('token')

from telebot import types

tracks = ['Rock Creek Park - Blackbyrds',
          'The Mexican - Babe Ruth',
          'Rocket In The Pocket - Cerrone',
          'Melting Pot - Booker T & The MGs',
          'Expansions - Lonnie Liston Smith',
          'Theme From SWAT - Rythym Heritage',
          'Shaft In Africa - Johnny Pate',
          'Apache - Incredible Bongo Band',
          'Sex Machine - James Brown',
          'Give It Up Turn It Loose - James Brown',
          'Yellow Sunshine - Yellow Sunshine Band',
          'Listen To Me - Baby Huey',
          'UFO - ESG',
          'Drummers Beat - Herman Kelly & Life',
          'Scorpio - Dennis Coffey',
          'Ride Sally Ride - Dennis Coffey',
          'Cloud Nine - The Temptations',
          'Its Just begun - Jimmy Castor Bunch',
          'Soul Makossa - Manu Dibango',
          'Films - Gary Newman',
          'Woman - Barabas',
          'In The Bottle - Gil Scott Heron',
          'Big Beat - Billy Squire',
          'Funky Penguin - Rufus Thomas',
          'Bongo Rock - Incredible Bongo Band',
          'Castles in the Sky - The Futures',
          'Fire - Osibisa',
          'Life on Mars - Dexter Wansel',
          'Bra - Cymande',
          'Hum Along and Dance - The Jacksons',
          'Life of the Party - The Jacksons',
          'Mirrors of My Mind - The Jacksons',
          'What You Dont Know - The Jacksons',
          'Galaxy - War',
          'Rain 2000 - Titanic',
          'Crystal World - Crystal Glass',
          'Gotta Get a Knutt - The New Birth',
          'I Can Understand It - The New Birth',
          'Super Sporm - Captain Sky',
          'Power - Earth, Wind & Fire',
          'New Bell - Manu Dibango']


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":

        keyboard = types.InlineKeyboardMarkup()

        key_get = types.InlineKeyboardButton(text='GET SONG', callback_data='tracks')

        keyboard.add(key_get)

        bot.send_message(message.from_user.id, text='Push the button to get \n random UpRock Song',
                         reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "press /start")

    else:

        bot.send_message(message.from_user.id, "press /help.")


def linker():
    song = random.choice(tracks)
    search = searchYoutube(song, offset=1, mode="list", max_results=1)
    return search.result()[0][2]


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "tracks":
        msg = linker()

        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
