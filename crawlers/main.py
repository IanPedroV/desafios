from reddit_scrapper import process_input, print_subreddits_and_threads
from telegram_bot import start_bot


def start():
    mode = input("Do you want to input the subreddits or call me on me telegram?. type 1 for local CLI of 2 for "
                 "telegram")
    if mode == "1":
        reddit_input = input('please input the subreddits as it follows: a;b;c')
        subreddits = process_input(reddit_input)
        print_subreddits_and_threads(subreddits)
    elif mode == "2":
        start_bot()


if __name__ == '__main__':
    start()

