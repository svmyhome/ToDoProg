import telebot
token = '1448944959:AAFaQKKp7pXRlYmRZcuXVCgtjWXYRlY8Hs8'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    print(f'Receivers: {message.text}')
    if 'Vladimir' in message.text:
        bot.send_message(message.chat.id, 'Ба! Знакомые все лица!')
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
