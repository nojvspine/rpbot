from aiogram import Bot, types #все нужные импорты
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import logging
import os

TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN) #токен бота
dp = Dispatcher(bot) #!в aiogram команды бота выполняет диспетчер

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)

async def on_shutdown(dispatcher):
    await bot.delete_webhook()

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

@dp.message_handler(content_types=['text'])
async def get_text_messages(message : types.Message):
    if message.reply_to_message != None:
        try:
            n = message.text.lower().index(' ')
            s = message.text.lower()[:n]
            await bot.send_message(message.chat.id, f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) {rpreplys[s]} [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) {message.text.lower()[n+1:]}", parse_mode='Markdown')
        except(Exception):
            try:
                n = message.text.lower().index('\n')
                s = message.text.lower()[:n]
                await bot.send_message(message.chat.id, f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) {rpreplys[s]} [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})\nС репликой:\"{message.text.lower()[(n+1):]}\"", parse_mode='Markdown')
            except(Exception):
                try:
                    s = message.text.lower()
                    await bot.send_message(message.chat.id, f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) {rpreplys[s]} [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})", parse_mode='Markdown')
                except(Exception):
                    None
    else:
        if message.text.lower() == "команды":
            s = ("\n".join(f'{i}' for i in rps))
            await bot.send_message(message.chat.id, f'Вот список рп команд:{s};\nДругие команды:\nскажи число')
        elif message.text == "/help":
            await bot.send_message(message.chat.id, "Используй *команды* чтобы узнать список команд.")
        elif message.text.lower() == "скажи число":
            n = randint(0, 100)
            await bot.send_message(message.chat.id, "Вот моё число: %d" % n)

if __name__ == '__main__': 
    logging.basicConfig(level=logging.INFO) 
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        )