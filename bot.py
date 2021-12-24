from telebot import *

bot = TeleBot('');

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
    for key in n.keys():
        if message.chat.id != key:
            n[message.chat.id] = {}
        else:
            for key in n[message.chat.id].keys():
                if message.from_user.first_name != key:
                    n[message.chat.id][message.from_user.first_name] = message.from_user.first_name
                else:
                    break
            break
    savenicks('nicks.txt', n)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.reply_to_message!=None:
        nicksearch(message)
        with open('nicks.txt', 'r') as s:
            nicks = eval(s.read())
            if message.text.lower()[:6] == "обнять":
                bot.send_message(message.chat.id, "[%s](tg://user?id=%s) обнял [%s](tg://user?id=%s) %s" % (nicks[message.chat.id][message.from_user.first_name], message.from_user.id, nicks[message.chat.id][message.reply_to_message.from_user.first_name], message.reply_to_message.from_user.id, message.text.lower()[7:]),parse_mode="Markdown")

bot.polling(none_stop=True, interval=0)
