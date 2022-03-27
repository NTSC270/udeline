import psutil, time, datetime, db
from helper import time_decorate

async def run_command(discord, message, args, client, opt):
    ramusage = psutil.cpu_percent()
    uptime = time.time() - client.starttime


    embed=discord.Embed(description="uptime: **`"+time_decorate(str(datetime.timedelta(seconds=uptime)),True)+"`**\n"+"latency: **`"+str("???")+"`**\n""RAM usage: **`"+str(ramusage)+"%`**\n", color=0x00ccff)
    embed.set_author(name="udeline stats",icon_url="https://media.discordapp.net/attachments/913898937532940371/937629996476956682/udeline.png")
    embed.set_footer(text="so far, you used this bot "+str(db.dbget("database/activity.json")[str(message.author.id)])+" times")

    mymsg = await message.reply(embed = embed)
    latency = mymsg.created_at - message.created_at

    embed=discord.Embed(description="uptime: **`"+time_decorate(str(datetime.timedelta(seconds=uptime)),True)+"`**\n"+"latency: **`"+time_decorate(str(latency),False)+"`**\n""RAM usage: **`"+str(ramusage)+"%`**\n", color=0x00ccff)
    embed.set_author(name="udeline stats",icon_url="https://media.discordapp.net/attachments/913898937532940371/937629996476956682/udeline.png")
    embed.set_footer(text="so far, you used this bot "+str(db.dbget("database/activity.json")[str(message.author.id)])+" times")

    await mymsg.edit(embed = embed)