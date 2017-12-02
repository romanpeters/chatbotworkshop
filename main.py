import telepot
import time
import commands

commands = {"/start": commands.start}


def on_msg(msg):
    command = msg["text"]

    if command in commands.keys():
        commands[command](msg, bot)



if __name__ == '__main__':
    bot = telepot.Bot("plaats hier je Telegram API key")

    print('Online...')
    bot.message_loop({'chat': on_msg,
                      })

    while 1:
        time.sleep(10)
