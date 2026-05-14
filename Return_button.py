from rubkey import Rubkey, Keypad, KeyButton

TOKEN = "Your_token_bot"

bot = Rubkey(token=TOKEN)

def get_user_name(chat_id):
    chat_info = bot.get_chat(chat_id)
    data = chat_info.get("chat", {})
    first_name = data.get("first_name", "User")
    return first_name

main_keypad = Keypad(resize=True).add_row(
    KeyButton("test1", "Test 1"),
    KeyButton("test2", "Test 2")
)

back_keypad = Keypad(resize=True).add_row(
    KeyButton("back", "Back")
)

@bot.command("start")
def start_handler(msg):
    name = get_user_name(msg.chat_id)
    msg.reply(f"Hello {name}", keypad=main_keypad)

@bot.on_button("test1")
def test1_handler(msg):
    msg.reply("Clicked! Click back to return:", keypad=back_keypad)

@bot.on_button("test2")
def test2_handler(msg):
    msg.reply("Clicked! Click back to return:", keypad=back_keypad)

@bot.on_button("back")
def back_handler(msg):
    msg.reply("You returned", keypad=main_keypad)

bot.run()
