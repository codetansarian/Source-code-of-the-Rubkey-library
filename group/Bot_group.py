from rubkey import Keypad, KeyButton
from rubkey.groupbot import GroupBot, GroupHandlers

bot = GroupBot("your_token")
handlers = GroupHandlers()

@handlers.command("start", group_only=False)
def start(msg, group_info):
    if group_info:
        msg.reply(f"سلام به گروه {group_info['title']}!\nایدی: {group_info['chat_id']}")
    else:
        msg.reply("سلام! به ربات خوش آمدید.")

@handlers.command("group_info", group_only=True)
def group_info_cmd(msg, group_info):
    msg.reply(f"نام گروه: {group_info['title']}\nایدی: {group_info['chat_id']}")

@handlers.on_message(group_only=True)
def group_messages(msg, group_info):
    if msg.text == "سلام":
        msg.reply(f"سلام به گروه {group_info['title']}!")

@handlers.on_message(group_only=False)
def all_messages(msg, group_info):
    msg.reply(f"پیام شما دریافت شد!")

bot.set_group_handlers(handlers)
bot.run()
