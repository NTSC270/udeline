import emoji_data_python
import emoji
import re
import requests
import io


async def run_command(discord, message, args, client, opt):

    if len(args) < 2:
        return await message.reply("i need an emoji to do that")

    kind = "emoji"

    if re.match(emoji_data_python.get_emoji_regex(), args[1].strip()) == None:
        kind = "maybe_discord"

    if kind == "emoji":

        emojicode = emoji_data_python.char_to_unified(args[1])
        emojicldr = emoji.demojize(args[1])
        
        r = requests.get("https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/twitter/282/"+str(emojicldr.replace(":", "").replace("_", "-"))+"_"+str(emojicode).lower()+".png", allow_redirects=True, stream=True)

        buf = io.BytesIO()
        buf.write(r.content)
        buf.seek(0)

        file=discord.File(buf, str(emojicldr.replace(":", "").replace("_", "-"))+".png")

        await message.reply(file=file)
    
    if kind == "maybe_discord":
        if not '<' in args[1]:
            return await message.reply("that doesn't look like a valid emoji, or i don't have access to the server with the emoji")
        kind = "discord"

    if kind == "discord":
        name = args[1].split(':')[2].replace('>', '')
        print(name)
        
        r = requests.get("https://cdn.discordapp.com/emojis/{id}.png?size=1024".format(id=name, format=".png"), allow_redirects=True, stream=True)

        buf = io.BytesIO()
        buf.write(r.content)
        buf.seek(0)

        file=discord.File(buf, args[1].split(':')[1]+".png")
        await message.reply(file=file)

