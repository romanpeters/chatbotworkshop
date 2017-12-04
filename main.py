import telepot
import time
import commands
import sys

enabled = {"/start": commands.start}


def on_msg(msg):
    text = msg["text"].split()

    msg["command"] = text[0]

    if len(text) > 1:
        msg["args"] = text[1:]

    if msg["command"] in enabled.keys():
        commands[msg["command"]](msg, bot)



if __name__ == '__main__':
    bot = telepot.Bot(sys.argv[1])

    print('Online...')
    bot.message_loop({'chat': on_msg,
                      })

    while 1:
        time.sleep(10)
