import discord, commands, re, option_parse
import re, time, os, sys
import helper
from dotenv import load_dotenv
load_dotenv()
sys.path.append("replit-keep-alive/src")
from replit_keep_alive import keep_alive

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        client.starttime = time.time()
        if client.user.name == "ndeline":
            client.devmode = True
            await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="to u,,help someone"))
        else:
            await client.change_presence(activity=discord.Streaming(name="u,help for commands", url="https://www.twitch.tv/topgeartv"))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.author.bot:
            return
        if helper.prefix.check(message.content, client)[0]:

            opt = option_parse.parse_options(message.content)
            for x in range(len(opt)):
                if '-'+opt[x] in message.content:
                    message.content = message.content.replace('-'+opt[x],"")
            args = re.split(" +", message.content.strip())
            prefix_len = helper.prefix.check(message.content, client)[1]
            command = args[0][prefix_len:]
            await commands.run_command(command, discord, message, args, client, opt)

if os.getenv("REPLIT") == "True":
    keep_alive()
intents = discord.Intents.all()
client = MyClient(intents=intents)
client.run(os.getenv("TOKEN"))
