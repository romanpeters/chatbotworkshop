# Telegram chatbot

### Handleiding

##### Telegram
We gebruiken de chat-service Telegram, voornamelijk omdat WhatsApp geen bots toestaat.
De API key voor je bot krijg je van een andere Telegram bot; the Botfather.
Stuur een berichtje naar @TheBotFather op Telegram. Met `/newbot` kun je bij hem de naam van je bot kiezen en krijg je je API key.


##### Python 3.6
Als je nog niet de laatste versie van Python hebt kun je die [hier](https://www.python.org/downloads/) downloaden.
Hier zitten ook pip en IDLE bij inbegrepen.
Pip is de package manager van Python, en IDLE de standaard editor.
Er zijn veel verschillende editors en ontwikkelomgevingen voor Python, misschien heb je er al wel een in gebruik. 
Mocht dat niet zo zijn, dan kun je voor deze workshop het beste IDLE gebruiken.

##### Telepot
Om met de Telegram API te communiceren gebruiken we de [Telepot module](https://github.com/nickoala/telepot).
Je kunt deze downloaden via de command line, met pip:
`pip install telepot`.  
Als je meerdere versies van Python op je computer hebt staan, is het misschien nodig om de juiste versie te specificeren.
Gebruik dan `pip3` in plaats van `pip` om het voor Python 3 te installeren.

##### Code
Om het overzichtelijk te houden heb ik het programma in twee bestanden opgesplitst:
[`main.py`](https://github.com/romanpeters/chatbotworkshop/blob/master/commands.py) en [`commands.py`](https://github.com/romanpeters/chatbotworkshop/blob/master/main.py). 
Je kunt in principe ook maar één bestand gebruiken, maar met grotere projecten kom je dan wel een beetje in de knoop.  
Clone of download dit project en open het met de twee bestanden met je editor.

Je kunt je bot online brengen door `main.py` te runnen.
Dit kan via de commandline met `python main.py APIKEY`, waar `APIKEY` de key is die jij van de BotFather hebt gekregen.
Als je het bestand via je editor wilt draaien, kun je in `main.py` onderin `sys.argv[1]` vervangen voor jouw API key in stringvorm.

Als alles goed gaat verschijnt er `online...` in beeld en kun je berichten sturen naar de door jou gekozen username voor de bot.
Je kunt nu je eigen commands bedenken en toevoegen in `commands.py`. 
Om ze aan een tekstcommando te linken moet je ze daarna ook toevoegen aan `enabled` in `main.py`.  


 


