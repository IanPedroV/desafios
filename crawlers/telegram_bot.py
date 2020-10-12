import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from reddit_scrapper import has_error, print_subreddits_and_threads, process_input
from dotenv import load_dotenv

load_dotenv()


def listen_for_subreddits(update, context):
    chat_id = update.message.chat_id
    subreddits = process_input(context.args[0])
    print_subreddits_and_threads(subreddits)
    for subreddit in subreddits:
        if has_error(subreddit):
            context.bot.send_message(chat_id, '\nError occurred when trying to scrap, message: ' + subreddit.error)
            break

        for thread in subreddit:
            context.bot.send_message(chat_id,
                                     'subreddit: ' + thread.subreddit + '\n' + 'title: ' + thread.title + '\n' + 'author: '
                                     + thread.author + '\n' + 'link: ' + thread.link + '\n' + 'link comments: '
                                     + thread.link_comment + '\n' + 'up_votes: ' + str(thread.up_votes))


def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, 'Type /NadaPraFazer subrreditA;subrreditB;subrreditC')


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command. Try /start")


def start_bot():
    updater = Updater(os.getenv('TELEGRAM_TOKEN'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('NadaPraFazer', listen_for_subreddits))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    updater.start_polling()
    print("Reddit Concierge successfully started!")
    updater.idle()
