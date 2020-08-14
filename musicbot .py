import random
import telebot
import youtube_search
bot = telebot.TeleBot('1075825015:AAGV3W5UVL6s6sSpjg4ruUG-wHPGyJOoRpc')

# Импортируем типы из модуля, чтобы создавать кнопки
from youtube_search import YoutubeSearch
from telebot import types
# Список Треков
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
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Hey There! \n I am a Rocker Bot \n Get ready for training")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик

        key_yes = types.InlineKeyboardButton(text='YES', callback_data='tracks')

        keyboard.add(key_yes)

        key_no = types.InlineKeyboardButton(text='NO', callback_data='no')

        keyboard.add(key_no)

        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Do you wanna dance?', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "press /start")

    else:

        bot.send_message(message.from_user.id, "You are dumb press /help.")
def linker():
    song = (random.choice(tracks))
    results = YoutubeSearch((song), max_results=1).to_json()
    final = ('http://www.youtube.com'+ results[results.index('link')+8:])
    return (final)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "tracks":
        msg = linker()
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data != "tracks":
        msgg = ('YOU SUCK')
        bot.send_message(call.message.chat.id, msgg)

bot.polling(none_stop=True, interval=0)
