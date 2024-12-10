import telebot

img = open("pic.jpg", 'rb')

import config

bot=telebot.TeleBot(config.Token)

@bot.message_handler()
def service_message(message):
    if config.Send_picture and config.Send_text:
        bot.send_photo(message.chat.id, img, caption=config.Text)
    elif config.Send_picture:
        bot.send_photo(message.chat.id, img)
    elif config.Send_text:
        bot.send_message(message.chat.id,config.Text)

bot.polling(none_stop=True, interval=1)