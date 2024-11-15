import random
import telebot
import settings
from telebot import types

TOKEN = settings.api
bot = telebot.TeleBot(TOKEN)
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
start_keyboard.row(types.KeyboardButton('Случайные ноготочки'))

width = ["короткие","длинные", "средние"]
led = ["матовые","глянцевые"]
forms = ["квадратной формы", "острой формы", "формы балерина", "формы стилет"]
colors = ["черные","нюд", "бордовые", "молочные" ]
additions = ["без дизайна", "с стемпингом", "с наклейками", "со стразами", "с втиркой", "с градиентом", "с фигурками","с обьемными линиями", "с фольгой", "с глитером", "со слайдерами", " с рисунком", "с пирсингом", "с мрамором", "с графити", "с разводами"]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Бот для случайного выбора ноготочков🫠", reply_markup = start_keyboard)
    
@bot.message_handler(func=lambda m: True)
def randomnogotochki(message):
    if message.text == "Случайные ноготочки":
	    w= random.choice(width)
	    l = random.choice(led)
	    c= random.choice(colors)
	    f= random.choice(forms)
	    a = random.choice(additions)
	    m = f"Ваши ногти это {w} {l} {c} {f} {a}"
	    bot.send_message(message.chat.id, text=m)
    else:
        bot.send_message(message.chat.id, text="Неверная комманда(")
    

def main() -> None:
    bot.infinity_polling()
    
main()
