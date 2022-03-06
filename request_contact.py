import telebot
from telebot import types

token = '5211862289:AAHG4VjexC7ZZ_rueMosmbX3lydGcM-5BHY'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    start_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button.add(types.KeyboardButton(text='начать'))
    bot.send_message(message.chat.id, text='Напиши начать', reply_markup=start_button)


@bot.message_handler(content_types=["text"])
def next_message(message):
    if message.text.lower() == 'начать':
        buttons = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('Можно выбрать это', callback_data='but1')
        button2 = types.InlineKeyboardButton('Или это', callback_data='but2')
        buttons.add(button1, button2)
        bot.send_message(message.chat.id, text='Вот: ', reply_markup=buttons)
    else:
        bot.send_message(message.chat.id, text='Я что просил?')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'start':
        buttons = types.InlineKeyboardMarkup(row_width=2)
        buttons.add(types.InlineKeyboardButton('Можно выбрать это', callback_data='but1'),
                    types.InlineKeyboardButton('Или это', callback_data='but2'))
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=buttons)
    elif call.data == 'but1':
        new_menu = types.InlineKeyboardMarkup()
        new_menu.add(types.InlineKeyboardButton('Ничего нового', callback_data='but4'),
                     types.InlineKeyboardButton('назад', callback_data='start'))
        bot.edit_message_text('Новое меню, кнопка 1', call.message.chat.id, call.message.message_id,
                              reply_markup=new_menu)
    elif call.data == 'but2':
        new_menu_2 = types.InlineKeyboardMarkup()
        new_menu_2.add(types.InlineKeyboardButton('И тут', callback_data='but5'),
                       types.InlineKeyboardButton('назад', callback_data='start'))
        bot.edit_message_text('Новое меню, кнопка 2', call.message.chat.id, call.message.message_id,
                              reply_markup=new_menu_2)


bot.polling()

