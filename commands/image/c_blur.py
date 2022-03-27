
from PIL import ImageFilter
from io import BytesIO
import math, re, commands
from imageget import get_image

import requests


async def run_command(discord, message, args, client, opt): 

    amp = 10
    for x in range(len(opt)):
        opt[x] = opt[x].split("=")
        if opt[x][0] == "power":
            if math.isnan(float(opt[x][1])):
                return await message.reply("\"power\" option must be number")
            amp = float(re.sub("\n.*$", "", opt[x][1]))

    image = await get_image(message=message,client=client)
    if image is None:
        await message.reply("i need an image to do that")
        return await commands.run_command("help", discord, message, ["u>help", "saturate"], client, [])

    img2 = image.filter(ImageFilter.GaussianBlur(radius=amp))
    with BytesIO() as image_binary:
        img2.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))