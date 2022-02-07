import requests 
import zipfile
from io import BytesIO
import time, datetime
import time_decorate, re

async def run_command(discord, message, args, client, opt):
    start = time.time()
    await message.add_reaction("⏱️")
    bytezip = BytesIO()
    zip_file = zipfile.ZipFile(bytezip, mode="w",compression=zipfile.ZIP_DEFLATED)

    timings = []

    emojis = message.guild.emojis
    emojidatas = []
    usednames = []

    for x in emojis:
        tempstart = time.time()
        r = requests.get(x.url, allow_redirects=True, stream=True)
        zip_file.writestr(x.name + (".gif" if x.animated else ".png"), r.content)
        temptime = time.time() - tempstart
        timings.append(temptime)

    
    zip_file.close()
    bytezip.seek(0)

    total = time.time() - start
    total = time_decorate.letters(str(datetime.timedelta(seconds=total)), False)
    average = 0
    for x in timings:
        average += x
    average = average / len(timings)

    selfmsg = await message.reply("done! all emojis were packed into this file\n>>> time taken: **`"+total+"`**\naverage time per emoji: **`"+time_decorate.letters(str(datetime.timedelta(seconds=average)), False)+"`**", file=discord.File(bytezip, message.guild.name+"_emojis.zip"))
    await message.remove_reaction("⏱️", selfmsg.author)