import asyncio
from rubkey import AsyncBot, Keypad, KeyButton

TOKEN = ""
bot = AsyncBot(token=TOKEN)

main_keypad = Keypad(resize=True, one_time=False)
main_keypad.add_row(
    KeyButton("btn1", "دکمه 1"),
    KeyButton("btn2", "دکمه 2")
)

back_keypad = Keypad(resize=True, one_time=False)
back_keypad.add_row(KeyButton("back", "بازگشت"))


@bot.command("start")
async def start(msg):
    await msg.reply("نمونه کیپد با Async و بازگشت", keypad=main_keypad)


@bot.on_button("btn1")
async def btn1(msg):
    await msg.reply("دکمه 1 زدی...", keypad=back_keypad)


@bot.on_button("btn2")
async def btn2(msg):
    await msg.reply("دکمه 2 زدی...")


@bot.on_button("back")
async def back(msg):
    await msg.reply("بازگشت", keypad=main_keypad)


async def main():
    await bot.run()


if __name__ == "__main__":
    asyncio.run(main())
