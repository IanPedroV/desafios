import requests
from bs4 import BeautifulSoup
from reddit_thread import RedditThread

all_threads = []
reddit_url = 'https://old.reddit.com'


def format_url(url):
    return url if url.startswith('http') else reddit_url + url


def should_add(thread):
    return type(thread.up_votes) is int and thread.up_votes >= 5000


def scrap(subreddit):
    # this becomes a constant
    url = reddit_url + '/r/' + subreddit + '/'
    headers = {'User-Agent': 'Mozilla/5.0'}

    page = requests.get(url, headers=headers)
    if page.status_code == 404:
        raise ValueError("subreddit: " + subreddit + "returned a not found response from reddit! Check it to see if "
                                                     "it really exists")
    soup = BeautifulSoup(page.text, 'html.parser')

    threads = []
    for page_thread in soup.find_all('div', attrs={'class': 'thing'}):
        title = page_thread.find('a', class_='title').text
        author = page_thread.attrs['data-author']
        up_votes = get_up_votes(page_thread)
        link_comment = format_url(page_thread.attrs['data-permalink'])
        link = format_url(page_thread.attrs['data-url'])
        thread = RedditThread(subreddit, title, author, up_votes, link_comment, link, None)
        if should_add(thread):
            threads.append(thread)
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


def get_all_threads(subreddits):
    for subreddit in subreddits:
        try:
            threads = scrap(subreddit)
            all_threads.append(threads)
        except ValueError as error:
            all_threads.append(RedditThread(title=subreddit, error=str(error)))
    return all_threads


def process_input(reddit_input):
    reddit_input_split = reddit_input.strip().split(';')
    if len(reddit_input_split) < 1:
        raise ValueError("Subreddits should be in format: a;b;c")
    subreddits = get_all_threads(reddit_input_split)
    return subreddits


def has_error(subreddit):
    return hasattr(subreddit, 'error') and subreddit.error is not None


def print_subreddits_and_threads(subreddits):
    for subreddit in subreddits:
        if has_error(subreddit):
            print('\nError occurred when trying to scrap, message: ' + subreddit.error)
            print('***************************************')
            break
        for thread in subreddit:
            print('subreddit: ' + thread.subreddit + '\n' + 'title: ' + thread.title + '\n' + 'author: '
                  + thread.author + '\n' + 'link: ' + thread.link + '\n' + 'link comments: '
                  + thread.link_comment + '\n' + 'up_votes: ' + str(thread.up_votes))
            print('----------------------------------------')
