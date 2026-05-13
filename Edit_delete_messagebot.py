from rubkey import Rubkey
import time

TOKEN = "اینجا_توکن_باتت_بزار"

bot = Rubkey(token=TOKEN)

@bot.command("start")
def start_handler(msg):
    sent_msg = msg.reply("سلام")
    
    time.sleep(3)
    
    sent_msg.edit("تا 3 ثانیه دیگه متنمو می پاکم")
    
    time.sleep(3)
    
    sent_msg.delete()

bot.run()
