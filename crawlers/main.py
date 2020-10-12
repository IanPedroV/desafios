from reddit_scrapper import receive_subreddits
from telegram_bot import start_bot


def start():
    mode = input("Do you want to input the subreddits or call me on me telegram?. type 1 for local CLI of 2 for telegram")
    if mode == "1":
        subreddits = input('please input the subreddits as it follows: a;b;c')
        receive_subreddits(subreddits)
    elif mode == "2":
        start_bot()


if __name__ == '__main__':
    start()

