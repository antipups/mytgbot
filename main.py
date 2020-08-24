from time import sleep
from telebot import TeleBot
from config import *
from threading import Thread
from freelancehunt import parse_new_posts


bot = TeleBot(token=TOKEN)


def send_new_posts():
    while True:
        for title in parse_new_posts():
            bot.send_message(chat_id=MY_ID,
                             text=title)
        sleep(TIME_OUT)


if __name__ == '__main__':
    Thread(target=send_new_posts).start()
    # bot.infinity_polling()
