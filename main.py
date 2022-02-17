import telebot

bot = telebot.TeleBot("5278392867:AAFePM81opTNIZITZxJDfWXUy1Leyear-Mw")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет,как дела?")

@bot.message_handler(commands=['dice'])
def send_dice(message):
     bot.send_dice(message.from_user.id)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я очень вежливый бот: могу поздороваться в ответ, попрощаться, твоя любовь ко мне всегда будет взаимна. \n /start - начать общение \n /dice - кинуть кость')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,"Ну привет!")
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До скорого')
    elif message.text.lower() == 'я люблю тебя':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMaYgwoGCdJ_vPjcWzOa19zAvm6vm0AAjUKAAIySyhLcag9ApnhVP0jBA')

bot.infinity_polling()
