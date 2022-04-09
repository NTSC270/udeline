from PIL import Image
from PIL import ImageChops
from PIL import ImageEnhance
from io import BytesIO
import math, re, commands
import aiohttp
import time
import colorsys


async def run_command(discord, message, args, client, opt): 

    progmsg = await message.reply(f"processing, please wait...")
    images = []
    imagehues = []
    for x in message.guild.members:
        async with aiohttp.ClientSession() as session:
            async with session.get(str(x.avatar_url)) as resp:
                image = Image.open(BytesIO(await resp.read()))
                image = image.convert("RGBA")
                image = image.resize((512,512))

                img = image.copy()
                img = img.convert("RGBA")
                img = img.resize((1, 1), resample=0)
                dominant_color = img.getpixel((0, 0))

                image.hue = colorsys.rgb_to_hsv(dominant_color[0]/255, dominant_color[1]/255, dominant_color[2]/255)[0]
                imagehues.append(colorsys.rgb_to_hsv(dominant_color[0]/255, dominant_color[1]/255, dominant_color[2]/255)[0])
                images.append(image)

    out = images[0]

    progress = 0
    step = 512/len(images)

    images.sort(key=lambda x: x.hue)

    for image in images:
        image = image.crop(box=((math.floor(image.size[0]/2-step),0, math.floor(image.size[0]/2)+step, 512)))
        out.paste(image, (math.floor(progress),0))
        progress += step
    with BytesIO() as image_binary:
        out.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))
        await progmsg.delete()