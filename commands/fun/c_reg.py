import commands

async def run_command(discord, message, args, client, opt):


    if len(args) < 1 and not message.reference:
        await message.reply("i need some text to do that")
        return await commands.run_command("reg", discord, message, ["u>help", "ascii"], client, [])

    args.pop(0)
    out = ""
    text = " ".join(args)
    if message.reference:
        messageref = await message.channel.fetch_message(message.reference.message_id)
        text = messageref.content
    def getChar(char):
        if char in ["0",'1',"2","3","4","5","6","7","8","9"]:
            return char+u"\uFE0F"+u"\u20E3"
        if ord(char.upper())-65 > 25 or ord(char.upper())-65 < 0:
            return char
            
        return chr(ord(char.upper())+127397)
    
    for i in text:
        out += getChar(i) + "​"
    return await message.reply(out)