import telebot

# from aiogram.types import ReplyKeyboardRemove, \
#     ReplyKeyboardMarkup, KeyboardButton, \
#     InlineKeyboardMarkup, InlineKeyboardButton
#
#
# greeting = KeyboardButton('Привет! 👄')
#
# greet_kb = ReplyKeyboardMarkup()
# greet_kb.add(greeting)

# ----------------------------------------------------------------------------------------------

bot = telebot.TeleBot('1202108943:AAGo-efNpzsvNVYhleX94daF9bMkFUAZt2A')

list_frendly_messages = ['привет', 'хай', 'здарова', 'здаров', 'hi', 'hello']



@bot.message_handler(commands=['start'])
def greeting(message):
    bot.send_message(message.chat.id, 'Я к вашим услугам-хозяин ...')

    # bot.send_message(message.chat.id, 'Я к вашим услугам-хозяин ...')


@bot.message_handler(content_types=['text'])
def message_text(message):
    message.text = message.text.lower()

    if message.text == '\help':
        bot.send_message(message.chat.id,
                         f'Напиши любой варинат из {list_frendly_messages} для того что бы начать общаться со мной.')

    elif message.text not in list_frendly_messages:
        bot.send_message(message.chat.id, f'Напиши "\help", я люблю когда со мной обращаются именно так. '
                                          f'А как именно - узнай ^_^.')

    else:
        bot.send_message(message.chat.id, "Привет мой господин!")





bot.polling(none_stop=True, interval=1)
