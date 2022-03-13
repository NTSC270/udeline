

from PIL import Image
from PIL import ImageEnhance
from io import BytesIO
import PIL, glob, os, math, re, commands

import requests

async def run_command(discord, message, args, client, opt): 

    if len(message.attachments) < 1 and not message.reference:
        await message.reply("i need an image to do that")
        return await commands.run_command("help", discord, message, ["u>help", "ifunny"], client, [])

    if len(message.attachments) > 0:
        content = message.attachments[0]

    img = Image.open('image/resources/ifunny.jpg', 'r')
    img2 = Image.open('image/resources/ifunny_bar.jpg', 'r')
    img_w, img_h = img.size

    if message.reference:
        messageref = await message.channel.fetch_message(message.reference.message_id)
        if messageref.attachments:
            content = messageref.attachments[0]
        if messageref.embeds:
            response = requests.get(messageref.embeds[0].url)
            content = response.content
        if not messageref.attachments and not messageref.embeds:
            await message.reply("i need an image attachment to do that and this message you're replying to doesn't have that")
            return await commands.run_command("help", discord, message, ["u>help", "ifunny"], client, [])

    image = Image.open(BytesIO(await content.read()))
    bg_w, bg_h = image.size
    offset = ((bg_w - img_w), (bg_h - img_h))
    image.paste(img2, (0, offset[1]))
    image.paste(img, offset)
    with BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))