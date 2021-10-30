import telebot
from time import time
import nicks
from telebot.types import ChatMemberMember, User;
from telebot import types;
import random
bot = telebot.TeleBot('2071410162:AAEBi0TeppPrzRA8vanFyCCv_V1J7VrK6hE');

def chatnick(message):
    for key in nicks.nicks.keys():
        if message.chat.id == key:
            nicks.nicks=nicks.nicks
            break
    else:
        nicks.nicks[message.chat.id]={}

def nick(message):
    chatnick(message)
    for key in nicks.nicks[message.chat.id].keys():
        if message.from_user.first_name == key:
            nicks.nicks[message.chat.id][message.from_user.first_name]=nicks.nicks[message.chat.id][message.from_user.first_name]
            break
    else:
        nicks.nicks[message.chat.id][message.from_user.first_name]=message.from_user.first_name
    for key in nicks.nicks[message.chat.id].keys():
        if message.reply_to_message.from_user.first_name == key:
            nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name]=nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name]
            break
    else:
        nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name]=message.reply_to_message.from_user.first_name

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.reply_to_message!=None:
        if message.text.lower()[:6] == "обнять":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) обнял [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
        elif message.text.lower()[:4] == "кусь":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) кусьнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[5:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "кусьнуть":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) кусьнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:10] == "поцеловать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) поцеловал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[11:]),parse_mode="Markdown")
        elif message.text.lower()[:3] == "цом":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) поцеловал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[4:]),parse_mode="Markdown")
        elif message.text.lower()[:4] == "цмок":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) поцеловал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[5:]),parse_mode="Markdown")
        elif message.text.lower()[:4] == "лизь": 
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) лизнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[5:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "лизнуть":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) лизнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "укусить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) укусил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:9] == "покормить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) покормил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[10:]),parse_mode="Markdown")
        elif message.text.lower()[:9] == "прижаться":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) прижался к [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[10:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "прижать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) прижал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "напоить": 
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) напоил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:6] == "споить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) напоил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
        elif message.text.lower()[:13] == "уложить спать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) уложил спать [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[14:]),parse_mode="Markdown")
        elif message.text.lower()[:5] == "сжечь":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) сжёг [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[6:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "ударить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) ударил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "связать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) связал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "прыгнуть":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) прыгнул на [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:5] == "взять":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) взял [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[6:]),parse_mode="Markdown")
        elif message.text.lower()[:6] == "съесть":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) съел [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
        elif message.text.lower()[:6] == "кинуть":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) кинул с прогиба [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "запереть":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) запер в шкафу [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "шлёпнуть":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) шлёпнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "отсосать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) отсосал у [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "трахнуть":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) оттрахал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "выебать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) выебал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "отлизать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) отлизал у [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "повесить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) повесил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "бупнуть": 
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:4] == "boop":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[5:]),parse_mode="Markdown")
        elif  message.text.lower()[:1] == "👇":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[2:]),parse_mode="Markdown")
        elif message.text.lower()[:1] == "👈":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[2:]),parse_mode="Markdown")
        elif message.text.lower()[:1] == "👉":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[2:]),parse_mode="Markdown")
        elif message.text.lower()[:1] == "👆":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[2:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "заняшить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) заняшил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "положить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) положил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "впитать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) слился с [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "вылизать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) вылизал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:10] == "расплавить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) расплавил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[11:]),parse_mode="Markdown")
        elif message.text.lower()[:5] == "сесть":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) сел на [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[6:]),parse_mode="Markdown")
        elif message.text.lower()[:6] == "уебать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) уебал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "въебать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) въебал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:7] == "выебать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) выебал [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
        elif message.text.lower()[:11] == "пристрелить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) пристрелил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[12:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "накурить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) накурил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:8] == "засосать":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) засосался с [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
        elif message.text.lower()[:9] == "погладить":
            nick(message)
            bot.send_message(message.chat.id, "[%s](tg://user?id=%s) погладил [%s](tg://user?id=%s) %s" % (nicks.nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks.nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[10:]),parse_mode="Markdown")
    else:
        if message.text.lower() == "команды":
            bot.send_message(message.chat.id, "Вот список моих команд:\nобнять;\nкусь (alt кусьнуть);\nпоцеловать (alt цом, цмок);\nлизнуть (alt лизь);\nукусить;\nпокормить;\nприжать;\nнапоить (alt споить);\nуложить спать;\nсжечь;\nударить;\nсвязать;\nпрыгнуть;\nвзять;\nсъесть;\nкинуть;\nзапереть;\nшлёпнуть;\nотсосать;\nтрахнуть;\nвыебать;\nотлизать;\nповесить;\nбупнуть (atl boop, смайлы пальцев);\nзаняшить;\nприжаться;\nположить;\nвпитать;\nвылизать;\nрасплавить;\nсесть;\nуебать;\nвъебать;\nвыебать;\nпристрелить;\nнакурить;\nзасосать;\nпогладить;\nскажи число;\nрп ник <ваш ник>;\nники рп.")
        elif message.text == "/help":
            bot.send_message(message.chat.id, "Используй *команды* чтобы узнать список команд.")
        elif message.text.lower() == "скажи число":
            n = random.randint(0, 100)
            bot.send_message(message.chat.id, "Вот моё число: ",n)
        elif message.text[:6] == "рп ник" or message.text[:6] == "Рп ник":
            chatnick(message)
            if message.text[6:]==' ' or message.text[6:]=='':
                bot.send_message(message.chat.id, "Вы не ввели ник!")
            else:
                n={message.from_user.first_name: message.text[7:]}
                nicks.nicks[message.chat.id].update(n)
                bot.send_message(message.chat.id, "%s теперь имеет ник %s" % (message.from_user.first_name, nicks.nicks[message.chat.id][message.from_user.first_name]))
        elif message.text.lower() == "ники рп":
            chatnick(message)
            bot.send_message(message.chat.id, "Вот ники участников чата:\n"+("\n".join([f'{i}: {nicks.nicks[message.chat.id][i]}' for i in nicks.nicks[message.chat.id].keys()])))

bot.polling(none_stop=True, interval=0)
