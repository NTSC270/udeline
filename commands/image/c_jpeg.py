

from PIL import Image
from PIL import ImageEnhance
from io import BytesIO
import PIL, glob, os, math, re, commands


async def run_command(discord, message, args, client, opt): 

    if len(message.attachments) < 1:
        await message.reply("i need an image attachment to do that")
        return await commands.run_command("help", discord, message, ["u>help", "jpeg"], client, [])


    amp = 5
    for x in range(len(opt)):
        opt[x] = opt[x].split("=")
        if opt[x][0] == "quality":
            if math.isnan(float(opt[x][1])):
                return await message.reply("\"power\" option must be number")
            amp = float(re.sub("\n.*$", "", opt[x][1]))

    content = message.attachments[0]
    image = Image.open(BytesIO(await content.read()))
    image = image.convert('RGB')
    with BytesIO() as image_binary:
        image.save(image_binary, 'JPEG', quality = int(amp))
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))