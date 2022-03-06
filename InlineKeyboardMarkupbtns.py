import telebot
from telebot import types

token = '5211862289:AAHG4VjexC7ZZ_rueMosmbX3lydGcM-5BHY'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['buttons'])
def other_buttons(message):
    buttons = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Github', url='https://github.com/')
    switch_button = types.InlineKeyboardButton(text='OtherChat', switch_inline_query='ForLearn')
    switch_button_here = types.InlineKeyboardButton(text='OtherBot_2', switch_inline_query_current_chat='')
    buttons.add(url_button, switch_button, switch_button_here)
    bot.send_message(message.chat.id, text='Типы кнопок', reply_markup=buttons)


bot.polling()

