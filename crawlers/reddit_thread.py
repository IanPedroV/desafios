class RedditThread:
    def __init__(self, subreddit=None, title=None, author=None, up_votes=0, link_comment=None, link=None, error=None):
        self.subreddit = subreddit
        self.title = title
        self.author = author
        self.up_votes = up_votes
        self.link_comment = link_comment
        self.link = link
        self.error = error
