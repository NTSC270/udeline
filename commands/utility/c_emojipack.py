import aiohttp 
import zipfile
from io import BytesIO
import time, datetime
from helper import time_decorate

async def run_command(discord, message, args, client, opt):

    if message.guild is None: return await message.reply("this command can only be run in a server")
    start = time.time()
    await message.add_reaction("⏱️")
    bytezip = BytesIO()
    zip_file = zipfile.ZipFile(bytezip, mode="w",compression=zipfile.ZIP_DEFLATED)

    timings = []

    emojis = message.guild.emojis

    async with aiohttp.ClientSession() as session:
        for x in emojis:
            tempstart = time.time()
            async with session.get(str(x.url)) as resp:
                zip_file.writestr(x.name + (".gif" if x.animated else ".png"), await resp.read())
                temptime = time.time() - tempstart
                timings.append(temptime)

    
    zip_file.close()
    bytezip.seek(0)

    total = time.time() - start
    total = time_decorate(str(datetime.timedelta(seconds=total)), False)
    average = 0
    for x in timings:
        average += x
    average = average / len(timings)

    selfmsg = await message.reply("done! all emojis were packed into this file\n>>> time taken: **`"+total+"`**\naverage time per emoji: **`"+time_decorate(str(datetime.timedelta(seconds=average)), False)+"`**", file=discord.File(bytezip, message.guild.name+"_emojis.zip"))
    await message.remove_reaction("⏱️", selfmsg.author)