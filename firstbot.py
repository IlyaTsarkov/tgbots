import telebot
from telebot import types

token = '5211862289:AAHG4VjexC7ZZ_rueMosmbX3lydGcM-5BHY'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Нет')
    button2 = types.KeyboardButton('Далее')
    buttons.add(button1, button2)
    bot.send_message(message.chat.id, text="Меня зовут learn_bot", reply_markup=buttons)


@bot.message_handler(content_types=['text'])
def answer(message):
    try:
        if message.text == 'Нет':
            bot.send_message(message.chat.id, text='...')
        elif message.text == 'Далее':
            buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Что делать?', request_contact=True)
            btn2 = types.KeyboardButton('Это все?', request_location=True)
            buttons.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Выбирай кнопку', reply_markup=buttons)

        elif message.text == 'Что делать?':
            bot.send_message(message.chat.id, text='Не знаю')

        elif message.text == 'Это все?':
            bot.send_message(message.chat.id, text='все')
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)



