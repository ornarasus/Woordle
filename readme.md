# Woordle 
**About the project:** The port of the Wordle game in Telegram

<a href="https://t.me/PlayWoordleBot">
<img alt="Demo Bot: Woordle" src="https://img.shields.io/badge/Demo_Bot-Wordle-blue?style=for-the-badge&logo=telegram">
</a>

**Technology stack**
* *API*: Aiogram
* *Container*: Docker

# Installation:
1) Clone this repo: `git clone https://github.com/ornarasus/Woordle.git`
2) Change directory: `cd Woordle`
3) Build image: `docker build --tag woordle .`
4) Run container: `docker run -e TOKEN={Token Bot Api} -e COUNT_LITTERS={5-6} -e COUNT_ATTEMPTS={4-12} -d woordle`
