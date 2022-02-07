import json, random, string, shutil, io, commands

async def run_command(discord, message, args, client, opt):

    if len(args) < 2 and not message.reference:
        await message.reply("i need a message to copy")
        return await commands.run_command("help", discord, message, ["u>help", "copy"], client, [])
    mobile = False
    for x in range(len(opt)):
        opt[x] = opt[x].split("=")
        if opt[x][0] == "mobile":
            mobile = True

    if len(args) == 2:
        msgid = args[1]
    if message.reference:
        msgid = message.reference.message_id
        

    msg = await message.channel.fetch_message(msgid)

    if message.author.is_on_mobile() == True:
        mobile = True

    if not mobile:
        f = io.BytesIO(bytes(msg.content, "utf8"))
        await message.reply("",file=discord.File(f, "message.txt"))
    else:
        embed = discord.Embed(description=msg.content[0:2000],color=0x00ccff)
        embed.title = "copy the text from the description"
        await message.reply(embed=embed)
    
    
    #await message.reply("```"+msg.content.replace("```", "`\0`\0`")+"```")

