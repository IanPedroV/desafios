import telebot

from main import run_scrap

bot = telebot.TeleBot('1226598612:AAEl0P82CdgnLb4LEuIQsPDvbDl4zVdm1rA')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot!")


@bot.message_handler(commands=['NadaPraFazer'])
def listen_for_subreddits(message):
    threads_from_subreddit = run_scrap(message)
    for thread in threads_from_subreddit:
        print('subreddit: ' + thread.subreddit + '\n' + 'title: ' + thread.title + '\n' + 'author: ' + thread.author +
              '\n ' + 'link: ' + thread.link + '\n' + 'link comments: ' + thread.link_comment +
              '\n' + 'up_votes: ' + str(thread.up_votes))
        print('-------------------------------------------------------------')


bot.polling()
