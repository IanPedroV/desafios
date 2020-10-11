import requests
from bs4 import BeautifulSoup
from reddit_thread import RedditThread

import telebot

all_threads = []


def format_url(url):
    return url if url.startswith('http') else 'https://old.reddit.com' + url


def should_add(thread):
    return type(thread.up_votes) is int and thread.up_votes >= 5000


def get_threads(subreddit):
    url = 'https://old.reddit.com/r/' + subreddit + '/'
    # TODO: what if the subreddit was not found?
    headers = {'User-Agent': 'Mozilla/5.0'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    threads = []
    for page_thread in soup.find_all('div', attrs={'class': 'thing'}):
        title = page_thread.find('a', class_='title').text
        author = page_thread.attrs['data-author']
        up_votes = get_up_votes(page_thread)
        link_comment = format_url(page_thread.attrs['data-permalink'])
        link = format_url(page_thread.attrs['data-url'])
        thread = RedditThread(subreddit, title, author, up_votes, link_comment, link)
        if should_add(thread):
            threads.append(thread)
        # TODO: what if no thread had more than 5K up_votes?
    return threads


def get_up_votes(page_thread):
    score_likes_component = page_thread.find('div', attrs={'class': 'score likes'})
    try:
        score_likes = int(score_likes_component.attrs['title'])
        return score_likes
    except KeyError:
        score_likes = score_likes_component.text
        try:
            score_likes = int(score_likes)
            return score_likes
        except ValueError:
            return 'No up_votes amount found!'


def run_scrap(subreddits):
    # TODO: what if the format was wrong? Clear spaces, trim
    for subreddit in subreddits.split(';'):
        thread = get_threads(subreddit)
        all_threads.append(thread)
    return all_threads


bot = telebot.TeleBot('1226598612:AAEl0P82CdgnLb4LEuIQsPDvbDl4zVdm1rA')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Olá, bem-vindo ao bot!")


@bot.message_handler(commands=['NadaPraFazer'])
def listen_for_subreddits(message):
    subreddit = run_scrap(message.text.replace('/NadaPraFazer', '').strip())
    for subreddit in subreddit:
        for thread in subreddit:
            bot.reply_to(message, 'subreddit: ' + thread.subreddit + '\n' + 'title: ' + thread.title + '\n' + 'author: '
                         + thread.author + '\n' + 'link: ' + thread.link + '\n' + 'link comments: '
                         + thread.link_comment + '\n' + 'up_votes: ' + str(thread.up_votes))


bot.polling()
