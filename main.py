import telebot
import random
from telebot import types

token = '6115476956:AAEdmUCKC8nW2eFIej0U73wKRnvDrncZC14'
bot = telebot.TeleBot(token)

def generate_keyboard(ListNameBtn : list, NumberColomns=2):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=NumberColomns)
    btn_name = [types.KeyboardButton(text=x) for x in ListNameBtn]
    keyboard.add(*btn_name)
    return keyboard

@bot.message_handler(func=lambda m : m.text == 'Tect')
def test(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Привет')
    keyboard.add(btn1)

    bot.send_message(message.chat.id, 'hi', reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Введите число от 1 до 2:')
    if type(msg) != int:
        bot.send_message(message.chat.id, 'Это не число:')
    else:
        bot.register_next_step_handler(msg, game)

def game(message):
    num = int(message.text)
    com_num = random.randint(1, 2)  
    if num == com_num:
        bot.send_message(message.chat.id, f'Ваше число {num}\
            \nМоё число:{com_num}\n Вы победили!')
    else:
        bot.send_message(message.chat.id, f'Ваше число {num}\
            \nМоё число:{com_num}\n Вы проиграли!')        

bot.polling()   