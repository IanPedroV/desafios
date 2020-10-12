import os

import telebot

from reddit_scrapper import print_subreddits_and_threads, process_input
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))


def start_bot():
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Olá, bem-vindo ao bot!")

    @bot.message_handler(commands=['NadaPraFazer'])
    def listen_for_subreddits(message):
        subreddits = process_input(message.text.replace('/NadaPraFazer', ''))
        print_subreddits_and_threads(subreddits)
        for subreddit in subreddits:
            for thread in subreddit:
                bot.send_message(message.chat.id,
                                 'subreddit: ' + thread.subreddit + '\n' + 'title: ' + thread.title + '\n' + 'author: '
                                 + thread.author + '\n' + 'link: ' + thread.link + '\n' + 'link comments: '
                                 + thread.link_comment + '\n' + 'up_votes: ' + str(thread.up_votes))

    print("Reddit Concierge successfully started!")
    bot.polling()
