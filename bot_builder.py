from rubkey import Rubkey, Keypad, TextboxButton
import threading

TOKEN = "توکن_بات_وارد_کن"

bot = Rubkey(token=TOKEN)

user_bots = {}
bot_threads = {}

def run_user_bot(user_id, user_token):
    try:
        user_bot = Rubkey(token=user_token)
        
        @user_bot.command("start")
        def start_handler(msg):
            msg.reply("سلام به بات شما خوش آمديد")
        
        user_bot.run()
    except Exception as e:
        print(f"خطا در بات كاربر {user_id}: {e}")

@bot.command("start")
def start(msg):
    text = "به بات ساز خوش آمديد\n"
    text = text + "/new - ساخت بات جديد\n"
    text = text + "/stop - توقف بات من"
    msg.reply(text)

@bot.command("new")
def new_bot(msg):
    keypad = Keypad(one_time=True)
    keypad.add_row(
        TextboxButton("get_token", "ورود توكن بات",
                      place_holder="توكن بات خود را وارد كنيد...",
                      title="ساخت بات جديد")
    )
    msg.reply("توكن بات خود را وارد كنيد:", keypad=keypad)

@bot.on_button("get_token")
def save_and_run(msg):
    token = msg.text
    user_id = msg.sender_id
    
    if user_id in bot_threads and bot_threads[user_id].is_alive():
        msg.reply("شما قبلا بات خود را اجرا كرده ايد.\nابتدا از /stop استفاده كنيد.")
        return
    
    user_bots[user_id] = token
    thread = threading.Thread(target=run_user_bot, args=(user_id, token), daemon=True)
    thread.start()
    bot_threads[user_id] = thread
    
    msg.reply("بات شما با موفقيت اجرا شد.\nحالا بات خودتان را استارت كنيد.")

@bot.command("stop")
def stop_bot(msg):
    user_id = msg.sender_id
    if user_id in bot_threads:
        bot_threads[user_id].join(timeout=0)
        del bot_threads[user_id]
        if user_id in user_bots:
            del user_bots[user_id]
        msg.reply("بات شما متوقف شد.")
    else:
        msg.reply("شما بات در حال اجرايي نداريد.")

bot.run()
