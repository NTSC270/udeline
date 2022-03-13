

from PIL import Image
from PIL import ImageOps
from io import BytesIO
import requests
import PIL, glob, os, math, re, commands


async def run_command(discord, message, args, client, opt): 

    if len(message.attachments) < 1 and not message.reference:
        await message.reply("i need an image to do that")
        return await commands.run_command("help", discord, message, ["u>help", "grayscale"], client, [])

    if len(message.attachments) > 0:
        content = message.attachments[0]

    # amp = 10
    # for x in range(len(opt)):
    #     opt[x] = opt[x].split("=")
    #     if opt[x][0] == "power":
    #         if math.isnan(float(opt[x][1])):
    #             return await message.reply("\"power\" option must be number")
    #         amp = float(re.sub("\n.*$", "", opt[x][1]))

    if message.reference:
        messageref = await message.channel.fetch_message(message.reference.message_id)
        if messageref.attachments:
            content = messageref.attachments[0]
        if messageref.embeds:
            response = requests.get(messageref.embeds[0].url)
            content = response.content
        if not messageref.attachments and not messageref.embeds:
            await message.reply("i need an image attachment to do that and this message you're replying to doesn't have that")
            return await commands.run_command("help", discord, message, ["u>help", "grayscale"], client, [])

    image = Image.open(BytesIO(await content.read()))
    img2 = ImageOps.grayscale(image)
    with BytesIO() as image_binary:
        img2.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))