
import numpy


from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageEnhance
from io import BytesIO
import math, re, commands
import requests


async def run_command(discord, message, args, client, opt): 

    if len(message.attachments) < 1 and not message.reference:
        await message.reply("i need an image attachment to do that")
        return await commands.run_command("help", discord, message, ["u>help", "saturate"], client, [])

    if len(message.attachments) > 0:
        content = message.attachments[0]

    rad = 10
    power = 1.3
    for x in range(len(opt)):
        opt[x] = opt[x].split("=")
        if opt[x][0] == "power":
            if math.isnan(float(opt[x][1])):
                return await message.reply("\"power\" option must be number")
            if float(opt[x][1]) < 0 or float(opt[x][1]) > 1:
                return await message.reply("\"power\" option must be within range of 0.0 - 1.0")
            power = float(re.sub("\n.*$", "", opt[x][1]))
        if opt[x][0] == "radius":
            if math.isnan(float(opt[x][1])):
                return await message.reply("\"radius\" option must be number")
            
            
            rad = float(re.sub("\n.*$", "", opt[x][1]))


    if message.reference:
        messageref = await message.channel.fetch_message(message.reference.message_id)
        if messageref.attachments:
            content = messageref.attachments[0]
        if messageref.embeds:
            response = requests.get(messageref.embeds[0].url)
            content = response.content
            content = Image.open(BytesIO(response.content))
        if not messageref.attachments and not messageref.embeds:
            await message.reply("i need an image attachment to do that and this message you're replying to doesn't have that")
            return await commands.run_command("help", discord, message, ["u>help", "saturate"], client, [])

    progmsg = await message.reply(f"processing, please wait...")

    image = Image.open(BytesIO(await content.read()))
    image = image.convert(mode="RGBA")

    img2 = image.filter(ImageFilter.GaussianBlur(radius=rad))
    conv = ImageEnhance.Brightness(img2)

    img2 = conv.enhance(power)

    out = ImageChops.screen(img2, image)

    with BytesIO() as image_binary:
        out.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))
        await progmsg.delete()