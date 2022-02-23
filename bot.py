from telebot import *
from random import randint

bot = TeleBot('');

rps = ['обнять', 'кусь', 'кусьнуть', 'поцеловать', 'цом', 'цмок', 'лизь', 'лизнуть', 'укусить', 
    'покормить', 'прижаться', 'прижать', 'напоить', 'споить', 'уложить', 'сжечь', 'ударить',
    'связать', 'прыгнуть', 'взять', 'съесть', 'кинуть', 'запереть', 'шлёпнуть', 'отсосать', 
    'трахнуть', 'выебать', 'отлизать', 'повесить', 'бупнуть', 'boop', '👇', '👈', '👉', '👆',
    'заняшить', 'положить', 'впитать', 'вылизать', 'расплавить', 'сесть', 'уебать', 'въебать',
    'выебать', 'пристрелить', 'накурить', 'засосать', 'погладить']
rpreplys = {'обнять':'обнял', 'кусь':'кусьнул', 'кусьнуть':'кусьнул', 'поцеловать':'поцеловал', 
    'цом':'поцеловал', 'цмок':'поцеловал', 'лизь':'лизнул', 'лизнуть':'лизнул', 'укусить':'укусил', 
    'покормить':'покормил', 'прижаться':'прижался к', 'прижать':'прижал', 'напоить':'напоил', 
    'споить':'споил', 'уложить':'уложил спать', 'сжечь':'сжёг', 'ударить':'ударил', 'связать':'связал', 
    'прыгнуть':'прыгнул на', 'взять':'взял', 'съесть':'съел', 'кинуть':'кинул', 'запереть':'запер в шкафу', 
    'шлёпнуть':'шлёпнул', 'отсосать':'отсосал у', 'трахнуть':'трахнул', 'выебать':'выебал', 'отлизать':'отлизал у', 
    'повесить':'повесил', 'бупнуть':'бупнул', 'boop':'бупнул', '👇':'бупнул', '👈':'бупнул', '👉':'бупнул', 
    '👆':'бупнул', 'заняшить':'заняшил', 'положить':'положил', 'впитать':'слился с', 'вылизать':'вылизал', 
    'расплавить':'расплавил', 'сесть':'сел на', 'уебать':'уебал', 'въебать':'въебал', 'выебать':'выебал', 
    'пристрелить':'пристрелил', 'накурить':'накурил', 'засосать':'засосал', 'погладить':'погладил'}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.reply_to_message!=None:
        try:
            n = message.text.lower().index(' ')
            s = message.text.lower()[:n]
            if s in rps:
                if message.text.lower()[n+1:] == message.reply_to_message.from_user.username:
                    bot.send_message(message.chat.id, f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) {rpreplys[s]} {message.text.lower()[n+1:]} {message.text.lower()[:(n+1)]}", parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) {rpreplys[s]} [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) {message.text.lower()[:(n+1)]}", parse_mode='Markdown')
        except(Exception):
            try:
                n = message.text.lower().index('\n')
                bot.send_message(message.chat.id, f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) {rpreplys[s]} [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})\nС репликой:\"{message.text.lower()[:(n+1)]}\"", parse_mode='Markdown')
            except:
                bot.send_message(message.chat.id, f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) обнял [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})", parse_mode='Markdown')
    else:
        if message.text.lower() == "команды":
            s = ("\n".join(f'{i}' for i in rps))
            bot.send_message(message.chat.id, f'Вот список рп команд:{s};\nДругие команды:\nскажи число')
        elif message.text == "/help":
            bot.send_message(message.chat.id, "Используй *команды* чтобы узнать список команд.")
        elif message.text.lower() == "скажи число":
            n = randint(0, 100)
            bot.send_message(message.chat.id, "Вот моё число: %d" % n)

bot.polling(none_stop=True, interval=0)
