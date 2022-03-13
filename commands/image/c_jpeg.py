

from PIL import Image
from PIL import ImageEnhance
from io import BytesIO
import PIL, glob, os, math, re, commands
import requests


async def run_command(discord, message, args, client, opt): 

    if len(message.attachments) < 1 and not message.reference:
        await message.reply("i need an image to do that")
        return await commands.run_command("help", discord, message, ["u>help", "jpeg"], client, [])

    if len(message.attachments) > 0:
        content = message.attachments[0]

    amp = 5
    for x in range(len(opt)):
        opt[x] = opt[x].split("=")
        if opt[x][0] == "quality":
            if math.isnan(float(opt[x][1])):
                return await message.reply("\"power\" option must be number")
            amp = float(re.sub("\n.*$", "", opt[x][1]))

    if message.reference:
        messageref = await message.channel.fetch_message(message.reference.message_id)
        if messageref.attachments:
            content = messageref.attachments[0]
        if messageref.embeds:
            response = requests.get(messageref.embeds[0].url)
            content = response.content
        if not messageref.attachments and not messageref.embeds:
            await message.reply("i need an image attachment to do that and this message you're replying to doesn't have that")
            return await commands.run_command("help", discord, message, ["u>help", "jpeg"], client, [])

    image = Image.open(BytesIO(await content.read()))
    image = image.convert('RGB')
    with BytesIO() as image_binary:
        image.save(image_binary, 'JPEG', quality = int(amp))
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.jpg"))