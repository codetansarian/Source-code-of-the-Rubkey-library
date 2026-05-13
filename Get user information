from rubkey import Rubkey
#دراینجا توکن بات خودتو باید وارد کنی
bot = Rubkey(token="yor_token_bot")

@bot.on_message()
def get_user_info(msg):
    #برای دریافت اعطلاعات کامل چت_کاربر
    chat_info = bot.get_chat(msg.chat_id)
    
    #توی این بخش استخراج نام  کامل و نام کاربری
    data = chat_info.get("chat", {})
    username = data.get("username", "ندارد")
    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    full_name = f"{first_name} {last_name}".strip()
    
    reply_text = f"👤 نام: {full_name}\n🆔 یوزرنیم: @{username}\n📱 آیدی: {msg.sender_id}"
    msg.reply(reply_text)

bot.run()
