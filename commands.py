# Voeg hier je eigen commands toe

def start(msg, bot):
    # het msg-object bevat alle informatie van het bericht
    # inclusief het command en args die wij hebben toegevoegd
    print(f"command:   {msg['command']}") # f-strings zijn handig voor string interpolatie
    print(f"arguments: {msg.get('args')}")

    reply_text = f"Hello {msg['from']['first_name']}!"

    # berichten terugsturen doe je naar het unieke ID van het chatgesprek
    # gelukkig is dat ID meegegeven aan het oorspronkelijke bericht in msg["chat"]["id"]
    bot.sendMessage(msg["chat"]["id"], reply_text)