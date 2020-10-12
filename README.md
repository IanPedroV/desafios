# Desafios IDwall

This applications are the Idwall challenges for a java back-end dev position.

Summarizing, those are two different apps. One is a reddit webcrawler with telegram integration and the other is a algorithm for text
justification.

## Building

First of all, clone this repository:

`git clone https://github.com/IanPedroV/desafios/`

The docker compose will handle all the building and stuff for you. If you don't have docker, just run the project
inside your IDEs.

The crawler needs a TELEGRAM_TOKEN=TOKEN inside a .env in its root folder to run, it was provider in the e-mail for Mirella xD

Having docker, just run:

`docker-compose up`

You might need to grab a cup of coffee while your application is coming up. 

The docker will build the StringFormatter with maven, but will not run it, that have to be done manually. It uses the 
provived template, so it's very straightforward :)

The crawler will be available in the end of the compose build: just access it: t.me/RedditConciergeBot and have fun!