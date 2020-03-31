import telebot
import my_parser_pl
import weater_api
from telebot import types
import time

TOKEN = '973239782:AAGDKrlsdzq_GNgSOZhWyIsITJNz5aBermA'

bot = telebot.TeleBot(TOKEN)

in_keyboard2 = types.InlineKeyboardMarkup()
in_keyboard3 = types.InlineKeyboardMarkup()

bms2 = types.InlineKeyboardButton(text = 'Dobrze', callback_data ='f2')
bms3 = types.InlineKeyboardButton(text = 'Źle', callback_data ='f3')
bms4 = types.InlineKeyboardButton(text = 'Warszawa', callback_data ='f4')
bms5 = types.InlineKeyboardButton(text = 'Lublin', callback_data ='f5')
bms6 = types.InlineKeyboardButton(text = 'Mińsk', callback_data ='f6')

in_keyboard2.add(bms2,bms3)
in_keyboard3.add(bms4,bms5,bms6)

@bot.message_handler(commands = ['start', 'help'])

def comady(message):
    if message.text == '/start':
        bot.send_sticker(message.chat.id,'CAACAgQAAxkBAAIQnV6A2lUSAXYuTAe1wJItlzwrB2H1AALoAANLae4QfKiCoCy-Tw4YBA')
        bot.send_message(chat_id = message.chat.id , text =
'''Hej! Jesetem testowym botem
Wpisz:
"pogoda" jeżeli chcesz dowiedzieć się jaka dzisiaj jest temperatura.
"waluta" jeżeli chcesz dowiedzieć się jakie są kyrsy walut. 
''')
        time.sleep(8)
        bot.send_message(message.chat.id, 'Jak się masz ?', reply_markup = in_keyboard2)

@bot.callback_query_handler(func = lambda call : True)
def longname(call):
    if call.data == "f2":
        bot.send_sticker(call.message.chat.id,'CAACAgQAAxkBAAIQ416A7Lk9umTrXILiZnFvZHKIlsLXAALmAANLae4QiPmPNEb61zUYBA')
        bot.send_message(chat_id = call.message.chat.id, text = 'Cool !')
    if call.data == "f3":
        bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAICzF6B4xL2K5f9TpAs2lAeSuaw2ZHfAAKdAANLae4Q0KpUnFTk_NQYBA')
        bot.send_message(chat_id = call.message.chat.id , text = 'Nie zasmucaj się. Wszystko będzie dobrze')
    if call.data == "f4":
        bot.send_message(chat_id = call.message.chat.id , text = 'Warszawa {0}°C'.format(weater_api.my_weater('Warsaw')))
    if call.data == "f5":
        bot.send_message(chat_id = call.message.chat.id, text = 'Lublin {0}°C'.format(weater_api.my_weater('Lublin')))
    if call.data == "f6":
        bot.send_message(chat_id = call.message.chat.id , text = 'Mińsk {0}°C'.format(weater_api.my_weater('Minsk')))

@bot.message_handler(content_types = ['text'])
def send_text(message):
    if message.text.lower() == 'waluta':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICwV6B4l25WPcmuNGI29dSCQaY23l-AALRAQACfDeOCvx9dmiAxUccGAQ')
        kurs = '''Dolar\tkupna - {dan[0]} zł, sprzedaż - {dan[1]} zł\nEuro\tkupna - {dan[2]} zł, sprzedaż - {dan[3]} zł'''.format(dan = my_parser_pl.waluta())
        bot.send_message(message.chat.id, kurs )
    elif message.text.lower() == 'pogoda':
        bot.send_message(message.chat.id, 'Które miasto ?', reply_markup = in_keyboard3)
    else:
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAIQpV6A2pn7u3iE0QZoEcXETZH6ZL77AAKbAANLae4QaHX_DJ1kkisYBA')
        bot.send_message(message.chat.id, 'Nie znam jak odpowiedzieć')

if __name__ == '__main__':
    bot.polling()

