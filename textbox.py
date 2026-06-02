from rubkey import Rubkey, Keypad, TextboxButton

TOKEN = "توکن_باتتو_بزن_اینجا"

bot = Rubkey(token=TOKEN)

@bot.command("start")
def start(msg):
    msg.reply("سلام. از دستور /get استفاده كنيد.")

@bot.command("get")
def ask_text(msg):
    keypad = Keypad(one_time=True)
    keypad.add_row(
        TextboxButton("name_btn", "ورود متن", 
                      place_holder="متن خود را بنويسيد...",
                      title="ورود اطلاعات")
    )
    msg.reply("لطفا متن خود را وارد كنيد:", keypad=keypad)

@bot.on_button("name_btn")
def get_text(msg):
    msg.reply("متن شما: " + msg.text)

bot.run()
