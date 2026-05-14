from rubkey import Rubkey, Keypad, KeyButton

TOKEN = "your_token_bot"

bot = Rubkey(token=TOKEN)

number_keypad = Keypad(resize=True)
number_keypad.add_row(
    KeyButton("send_number", "ارسال شماره تلفن", "AskMyPhoneNumber")
)

info_keypad = Keypad(resize=True)
info_keypad.add_row(
    KeyButton("show_info", "اطلاعات")
)

@bot.command("start")
def start_handler(msg):
    msg.reply("سلام لطفا برای ورود به بات شماره تلفن خود را وارد کنید:", keypad=number_keypad)

@bot.on_button("send_number")
def receive_number(msg):
    msg.reply("با موفقیت تایید شدید", keypad=info_keypad)

@bot.on_button("show_info")
def show_info(msg):
    chat_info = bot.get_chat(msg.chat_id)
    data = chat_info.get("chat", {})
    username = data.get("username", "ندارد")
    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    full_name = f"{first_name} {last_name}".strip()
    
    info_text = f"👤 نام: {full_name}\n🆔 یوزرنیم: @{username}\n📱 چت ایدی: {msg.chat_id}\n🆔 سندر ایدی: {msg.sender_id}"
    msg.reply(info_text)

@bot.on_message()
def unknown(msg):
    if msg.contact:
        phone = msg.contact.get("phone_number", "")
        msg.reply(f"شماره {phone} ثبت شد!", keypad=info_keypad)
    elif msg.text != "/start":
        msg.reply("لطفا از دکمه ارسال شماره تلفن استفاده کنید")

bot.run()
