import requests
from bs4 import BeautifulSoup

from redditthread import RedditThread


def parse_url(url):
    return url if url.startswith('http') else 'https://old.reddit.com' + url


def should_add(thread):
    return thread.up_votes >= 5000


def get_all_threads(subreddit):
    url = "https://old.reddit.com/r/" + subreddit + "/"
    # TODO: what if the subreddit was not found?
    # Headers to mimic a browser visit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Returns a requests.models.Response object
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')

    threads = []
    for page_thread in soup.find_all('div', attrs={'class': 'thing'}):
        title = page_thread.find('a', class_="title").text
        author = page_thread.attrs['data-author']
        up_votes = page_thread.find("div", attrs={"class": "score likes"}).text
        link_comment = parse_url(page_thread.attrs['data-permalink'])
        link = parse_url(page_thread.attrs['data-url'])
        thread = RedditThread(title, author, up_votes, link_comment, link)
        if should_add(thread):
            threads.append(thread)
        print(subreddit + " | " + title + " | " + author + " | " + link + " | " + link_comment + " | " + up_votes)
        #TODO: what if no thread had more than 5K upvotes?
    print("-----------------------------------------------------------------")
    return threads


def run_scrap():
    #subreddits = input("digite os subreddits" + "\n")
    # TODO: what if the format was wrong? Clear spaces, trim
    subreddits = "Announcements;funny;AskReddit;gaming;aww;pics;Music;science;worldnews;EarthPorn"
    for subreddit in subreddits.split(";"):
        print(get_all_threads(subreddit))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_scrap()
