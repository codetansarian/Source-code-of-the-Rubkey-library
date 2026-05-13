from rubkey import Rubkey

TOKEN = "توکن_باتت_اینجا_وارد_کن"

bot = Rubkey(token=TOKEN)

@bot.command("start")
def start_with_slash(msg):
    msg.reply("بات با اسلش جواب داد")

@bot.on_message()
def all_messages(msg):
    if msg.text == "start":
        msg.reply("بات بدون اسلش جواب داد")
    elif msg.text == "test":
        msg.reply("این هم دستور test بدون اسلش")

bot.run()
