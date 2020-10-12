# Desafio 1: Strings

Webcrawlers! How not to love them? I've worked with them in the past, and it's always fun to play with them!

This project is in it's core a reddit webcrawler. It receives a list of subreddits and returns information of the threads
with 5000 upvotes or more! 

It also comes with a built-in telegram integration, so you can pass the subreddits for the Reddit Concierge bot and he'll reply
the same info for you!

## Running
Don't forget to create a .env file with a `TELEGRAM_TOKEN=TOKEN` inside!

If you run this with docker it will automatically chooses the telegram response, but this one also prints the data in the CLI, so it's 
easier to test it!

If you are running directly the py file, just follow the given instructions! :)

## Stack choices
- Python 3
- python-telegram-bot
- request