import asyncio
from rubkey import AsyncBot, Keypad, KeyButton

TOKEN = ""
#اینجا  رمز عبور واسه وارد شدن به پنل ادمین هستش
ADMIN_PASSWORD = "ADMINBOT"
bot = AsyncBot(token=TOKEN)

admin_verified = set()

admin_keypad = Keypad(resize=True).add_row(
    KeyButton("admin_btn", "دکمه")
)


@bot.command("start")
async def start(msg):
    await msg.reply("سلام...")


@bot.on_message()
async def handle(msg):
    user_id = msg.sender_id
    
    if not msg.text:
        return
    
    if hasattr(msg, 'button_id') and msg.button_id:
        return
    
    text = msg.text.strip()
    
    if text == ADMIN_PASSWORD:
        admin_verified.add(user_id)
        await msg.reply("پسوورد ادمین تایید شده خب حالا میتونی با این دستور وارد پنل ادمین بشی:\n/admin")
        return
    
    if text == "/admin":
        if user_id in admin_verified:
            await msg.reply("خب وارد پنل ادمین شدی", keypad=admin_keypad)
        else:
            await msg.reply("پسوورد ادمین رو وارد کن")
        return


@bot.on_button("admin_btn")
async def admin_btn(msg):
    user_id = msg.sender_id
    
    if user_id not in admin_verified:
        return
    
    await msg.reply("کلیک کردی")


async def main():
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
