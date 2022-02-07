import discord, commands, re, helpers.helper as helper, optionparse
import re
import time
import io



class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as', self.user)
        client.starttime = time.time()
        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="to >help someone"))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.author.bot:
            return
        if "<@!913901320686153728>" in message.content or "<@913901320686153728>" in message.content:
            command = "help"
            await commands.run_command(command, discord, message, [], client, [])
        if helper.has_pfix(message.content):

            opt = optionparse.parse_options(message.content)
            for x in range(len(opt)):
                if '--'+opt[x] in message.content:
                    message.content = message.content.replace('--'+opt[x],"")

            args = re.split(" +", message.content.strip())

            pfix_length = helper.pfix_sw(message.content)
            command = args[0][pfix_length:]
            await commands.run_command(command, discord, message, args, client, opt)
            args.pop(0)
            optionparse.parse_options(" ".join(args))

client = MyClient()
client.run(open('config/private/secrets.txt').readlines()[0])
