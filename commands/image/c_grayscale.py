

from PIL import Image
from PIL import ImageOps
from io import BytesIO
from imageget import get_image
import commands


async def run_command(discord, message, args, client, opt): 

    image = await get_image(message=message,client=client)
    if image is None:
        await message.reply("i need an image to do that")
        return await commands.run_command("help", discord, message, ["u>help", "saturate"], client, [])

    img2 = ImageOps.grayscale(image)
    with BytesIO() as image_binary:
        img2.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))