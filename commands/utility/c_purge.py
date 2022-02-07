import asyncio
from time import sleep
import commands


async def run_command(discord, message, args, client, opt):

    if message.author.guild_permissions.manage_messages == False:
        return await message.reply("you lack the required permissions to `manage messages`")
        
    if len(args) < 2:
        await message.reply("you need to tell me how many messages to delete")
        return await commands.run_command("help", discord, message, ["u>help", "purge"], client, [])

    single_member = None
    count = args[1]

    for x in range(len(opt)):
        opt[x] = opt[x].split("=")
        if opt[x][0] == "member":
            single_member = opt[x][1]

    messages = await message.channel.history(limit=int(count)).flatten()
    todelete = []

    delete = asyncio.get_event_loop()

    if single_member != None:
        for x in messages:
            if x.author.id == single_member:
                todelete.append(x)
        await message.channel.delete_messages(todelete)
        msg = await message.channel.send("deleted **`"+str(count)+"`** messages in <#"+str(message.channel.id)+">")
        await asyncio.sleep(5)
        delete.run_until_complete(await msg.delete())
    else:
        await message.channel.delete_messages(messages)
        msg = await message.channel.send("deleted **`"+str(count)+"`** messages in <#"+str(message.channel.id)+">")
        await asyncio.sleep(5)
        delete.run_until_complete(await msg.delete())

    