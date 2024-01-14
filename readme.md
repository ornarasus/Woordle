# Woordle 
**About the project:** The port of the Wordle game in Telegram

<a href="https://t.me/PlayWoordleBot">
<img alt="Demo Bot: Woordle" src="https://img.shields.io/badge/Demo_Bot-Woordle-blue?style=for-the-badge&logo=telegram">
</a>

**Technology stack**
* *Bot API*: aiogram
* *Container*: Docker
* *XML Toolkit*: lxml

# Build image
```sh
git clone https://github.com/ornarasus/Woordle.git
cd Woordle
docker build --tag woordle .
docker tag woordle ornarasus/woordle
```
# Pull image
```sh
docker pull ornarasus/woordle
```
# Run container
```sh
docker run -e TOKEN={Token Bot Api} -e COUNT_LETTERS={5-6} -e COUNT_ATTEMPTS={4-12} -d ornarasus/woordle
```