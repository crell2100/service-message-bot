import telebot

import config

bot=telebot.TeleBot(config.Token)

@bot.message_handler()
def service_message(message):
    with open("pic.jpg",'rb') as pic:
        if config.Send_picture and config.Send_text:
            bot.send_photo(message.chat.id, pic, caption=config.Text)
        elif config.Send_picture:
            bot.send_photo(message.chat.id, pic)
        elif config.Send_text:
            bot.send_message(message.chat.id,config.Text)

if __name__ == '__main__':
    bot.polling()
