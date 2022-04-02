from PIL import Image
from PIL import ImageChops
from PIL import ImageEnhance
from io import BytesIO
import math, re, commands
import aiohttp


async def run_command(discord, message, args, client, opt): 

    images = []
    for x in message.guild.members:
        async with aiohttp.ClientSession() as session:
            async with session.get(str(x.display_avatar.url)) as resp:
                image = Image.open(BytesIO(await resp.read()))
                image = image.convert("RGBA")
                image = image.resize((512,512))
                images.append(image)

    progmsg = await message.reply(f"processing, please wait...")

    out = Image.new(size=images[0].size, mode="RGBA", color="black")

    for image in images:
        out = Image.blend(out, image, alpha=1/len(images))

    with BytesIO() as image_binary:
        out.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))
        await progmsg.delete()