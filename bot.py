from telebot import *
from random import randint

bot = TeleBot('2071410162:AAEBi0TeppPrzRA8vanFyCCv_V1J7VrK6hE');

def loadnicks(filename):
    with open(filename, 'r') as s:
        nicks = eval(s.read())
        return nicks

def savenicks(filename, nicks):
    with open(filename, 'w') as s:
        nicks = str(nicks)
        s.write(nicks)

def nicksearch(message):
    n = loadnicks('nicks.txt')
    if message.chat.id in n.keys():
        if message.from_user.first_name in n[message.chat.id].keys():
            savenicks('nicks.txt', n)
        else:
            n[message.chat.id][message.from_user.first_name] = message.from_user.first_name
            savenicks('nicks.txt', n)
        if message.reply_to_message != None:
            if message.reply_to_message.from_user.first_name in n[message.chat.id].keys():
                savenicks('nicks.txt', n)
            else:
                n[message.chat.id][message.reply_to_message.from_user.first_name] = message.reply_to_message.from_user.first_name
                savenicks('nicks.txt', n)
    else:
        n[message.chat.id] = {}
        if message.from_user.first_name in n[message.chat.id].keys():
            savenicks('nicks.txt', n)
        else:
            n[message.chat.id][message.from_user.first_name] = message.from_user.first_name
            savenicks('nicks.txt', n)
        if message.reply_to_message != None:
            if message.reply_to_message.from_user.first_name in n[message.chat.id].keys():
                savenicks('nicks.txt', n)
            else:
                n[message.chat.id][message.reply_to_message.from_user.first_name] = message.reply_to_message.from_user.first_name
                savenicks('nicks.txt', n)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    nicksearch(message)
    if message.reply_to_message!=None:
        with open('nicks.txt', 'r') as s:
            nicks = eval(s.read())
            if message.text.lower()[:6] == "обнять":
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) обнял [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
            elif message.text.lower()[:4] == "кусь":
            
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) кусьнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[5:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "кусьнуть":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) кусьнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:10] == "поцеловать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) поцеловал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[11:]),parse_mode="Markdown")
            elif message.text.lower()[:3] == "цом":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) поцеловал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[4:]),parse_mode="Markdown")
            elif message.text.lower()[:4] == "цмок":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) поцеловал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[5:]),parse_mode="Markdown")
            elif message.text.lower()[:4] == "лизь": 
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) лизнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[5:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "лизнуть":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) лизнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "укусить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) укусил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:9] == "покормить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) покормил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[10:]),parse_mode="Markdown")
            elif message.text.lower()[:9] == "прижаться":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) прижался к [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[10:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "прижать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) прижал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "напоить": 
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) напоил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:6] == "споить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) напоил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
            elif message.text.lower()[:13] == "уложить спать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) уложил спать [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[14:]),parse_mode="Markdown")
            elif message.text.lower()[:5] == "сжечь":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) сжёг [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[6:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "ударить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) ударил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "связать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) связал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "прыгнуть":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) прыгнул на [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:5] == "взять":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) взял [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[6:]),parse_mode="Markdown")
            elif message.text.lower()[:6] == "съесть":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) съел [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
            elif message.text.lower()[:6] == "кинуть":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) кинул с прогиба [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "запереть":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) запер в шкафу [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "шлёпнуть":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) шлёпнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "отсосать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) отсосал у [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "трахнуть":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) оттрахал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "выебать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) выебал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "отлизать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) отлизал у [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "повесить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) повесил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "бупнуть": 
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:4] == "boop":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[5:]),parse_mode="Markdown")
            elif  message.text.lower()[:1] == "👇":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[2:]),parse_mode="Markdown")
            elif message.text.lower()[:1] == "👈":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[2:]),parse_mode="Markdown")
            elif message.text.lower()[:1] == "👉":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[2:]),parse_mode="Markdown")
            elif message.text.lower()[:1] == "👆":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) бупнул [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[2:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "заняшить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) заняшил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "положить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) положил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "впитать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) слился с [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "вылизать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) вылизал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:10] == "расплавить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) расплавил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[11:]),parse_mode="Markdown")
            elif message.text.lower()[:5] == "сесть":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) сел на [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[6:]),parse_mode="Markdown")
            elif message.text.lower()[:6] == "уебать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) уебал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "въебать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) въебал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:7] == "выебать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) выебал [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[8:]),parse_mode="Markdown")
            elif message.text.lower()[:11] == "пристрелить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) пристрелил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[12:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "накурить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) накурил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:8] == "засосать":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) засосался с [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[9:]),parse_mode="Markdown")
            elif message.text.lower()[:9] == "погладить":
                
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) погладил [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[10:]),parse_mode="Markdown")     
    else:
        with open('nicks.txt', 'r') as s:
            nicks = eval(s.read())
            if message.text.lower() == "команды":
                bot.send_message(message.chat.id, "Вот список моих команд:\nобнять;\nкусь (alt кусьнуть);\nпоцеловать (alt цом, цмок);\nлизнуть (alt лизь);\nукусить;\nпокормить;\nприжать;\nнапоить (alt споить);\nуложить спать;\nсжечь;\nударить;\nсвязать;\nпрыгнуть;\nвзять;\nсъесть;\nкинуть;\nзапереть;\nшлёпнуть;\nотсосать;\nтрахнуть;\nвыебать;\nотлизать;\nповесить;\nбупнуть (atl boop, смайлы пальцев);\nзаняшить;\nприжаться;\nположить;\nвпитать;\nвылизать;\nрасплавить;\nсесть;\nуебать;\nвъебать;\nвыебать;\nпристрелить;\nнакурить;\nзасосать;\nпогладить;\nскажи число;\nрп ник <ваш ник>;\nники рп.")
            elif message.text == "/help":
                bot.send_message(message.chat.id, "Используй *команды* чтобы узнать список команд.")
            elif message.text.lower() == "скажи число":
                n = randint(0, 100)
                bot.send_message(message.chat.id, "Вот моё число: %d" % n)
            elif message.text[:6] == "рп ник" or message.text[:6] == "Рп ник":
                if message.text[6:]==' ' or message.text[6:]=='':
                    bot.send_message(message.chat.id, "Вы не ввели ник!")
                else:
                    n={message.from_user.first_name: message.text[7:]}
                    nicks[message.chat.id].update(n)
                    savenicks('nicks.txt', nicks)
                    bot.send_message(message.chat.id, "%s теперь имеет ник %s" % (message.from_user.first_name, nicks[message.chat.id][message.from_user.first_name]))
            elif message.text.lower() == "ники рп":
                bot.send_message(message.chat.id, "Вот ники участников чата: "+("\n".join(f'{i}: {nicks[message.chat.id][i]}' for i in nicks[message.chat.id].keys())))


bot.polling(none_stop=True, interval=0)
