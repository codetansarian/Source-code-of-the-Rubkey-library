from rubkey import Rubkey, InlineKeypad, InlineButton

TOKEN = "توکن_بات_خودتو_بزار"

bot = Rubkey(token=TOKEN)

users = set()

@bot.command("start")
def start_handler(msg):
    users.add(msg.sender_id)
    
    keypad = InlineKeypad().add_row(
        InlineButton("users_count", f"تعداد كاربران بات ({len(users)})")
    )
    
    msg.reply("سلام به بات خوش اومدی...", inline_keypad=keypad)

@bot.on_button("users_count")
def show_users(msg):
    msg.edit(f"تعداد كاربران بات: {len(users)}")

bot.run()
