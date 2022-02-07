

from PIL import Image
from PIL import ImageEnhance
from io import BytesIO
import PIL, glob, os, math, re, commands


async def run_command(discord, message, args, client, opt): 

    if len(message.attachments) < 1:
        await message.reply("i need an image attachment to do that")
        return await commands.run_command("help", discord, message, ["u>help", "ifunny"], client, [])

    content = message.attachments[0]
    img = Image.open('image/resources/ifunny.jpg', 'r')
    img2 = Image.open('image/resources/ifunny_bar.jpg', 'r')
    img_w, img_h = img.size
    image = Image.open(BytesIO(await content.read()))
    bg_w, bg_h = image.size
    offset = ((bg_w - img_w), (bg_h - img_h))
    image.paste(img2, (0, offset[1]))
    image.paste(img, offset)
    with BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))