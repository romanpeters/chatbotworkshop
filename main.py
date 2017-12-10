import time
import sys
import telepot   # Python wrapper voor de Telegram API
import commands  # importeer je commands uit commands.py

# text berichten linken aan commands
enabled = {"/start": commands.start}



def on_msg(msg):
    if msg.get("text"):  # als het een tekstbericht is

        text = msg["text"].split()  # lijst met alle woorden uit het bericht

        msg["command"] = text[0]  # bewaar het eerste woord uit de lijst in msg["command"]

        if len(text) > 1:  # als het bericht uit meerdere woorden bestaat
            msg["args"] = text[1:]  # dan bewaar je de rest in msg["args"]

        if msg["command"] in enabled.keys():  # als het command in onze lijst met commands staat
            enabled[msg["command"]](msg, bot)  # dan voer je 'm uit, met als parameters het msg- en bot-object
    else:
        # je kunt eventueel ook nog wat doen met berichten die geen tekst hebben
        # zoals locaties, of afbeeldingen.
        pass  # doe dat dan hier


if __name__ == '__main__':  # als het bestand als script wordt uitgevoerd
    bot = telepot.Bot(sys.argv[1])  # pak het eerste argument van de command line voor het bot-object
    # als het je niet uitmaakt dat hackers je API key zouden kunnen stelen
    # kun je ipv sys.argv[1] ook rechtstreeks je API key hier in een string meegeven aan de functie


    print('Online...')  # Laat even zien dat alles goed is geldadn


    # de message_loop functie van het bot-object zorgt dat berichten naar onze functie worden doorgestuurd
    bot.message_loop({'chat': on_msg,
                      })

    # het script moet draaiende blijven om de bot online te houden
    # dus hier een infinite loop om 'm bezig te houden
    while 1:
        time.sleep(10)
