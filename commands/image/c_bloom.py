from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageEnhance
from io import BytesIO
import math, re, commands
from imageget import get_image


async def run_command(discord, message, args, client, opt): 

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

    image = await get_image(message=message,client=client)
    if image is None:
        await message.reply("i need an image to do that")
        return await commands.run_command("help", discord, message, ["u>help", "bloom"], client, [])
    
    progmsg = await message.reply(f"processing, please wait...")

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