import discord, commands, re, helpers.helper as helper, optionparse
import re
import time
import os
import sys
from dotenv import load_dotenv
sys.path.append("replit-keep-alive/src")
from replit_keep_alive import keep_alive
load_dotenv()


class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as', self.user)
        client.starttime = time.time()
        if client.user.name == "udevline":
            client.devmode = True
            await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="to u>>help someone"))
        else:
            await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="to u>help someone"))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.author.bot:
            return
        if client.user in message.mentions:
            command = "help"
            await commands.run_command(command, discord, message, [], client, [])
        if helper.prefix.check(message.content, client)[0]:

            opt = optionparse.parse_options(message.content)
            for x in range(len(opt)):
                if '--'+opt[x] in message.content:
                    message.content = message.content.replace('--'+opt[x],"")
            args = re.split(" +", message.content.strip())

            prefix_len = helper.prefix.check(message.content, client)[1]
            command = args[0][prefix_len:]
            await commands.run_command(command, discord, message, args, client, opt)
            args.pop(0)
            optionparse.parse_options(" ".join(args))

if os.getenv("REPLIT") == "True":
    keep_alive()
client = MyClient()
client.run(os.getenv("TOKEN"))