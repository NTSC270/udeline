

from PIL import Image
import commands
from imageget import get_image
from io import BytesIO


async def run_command(discord, message, args, client, opt): 

    img = Image.open('image/resources/ifunny.jpg', 'r')
    img2 = Image.open('image/resources/ifunny_bar.jpg', 'r')
    img_w, img_h = img.size


    image = await get_image(message=message,client=client)
    if image is None:
        await message.reply("i need an image to do that")
        return await commands.run_command("help", discord, message, ["u>help", "saturate"], client, [])

    bg_w, bg_h = image.size
    offset = ((bg_w - img_w), (bg_h - img_h))
    image.paste(img2, (0, offset[1]))
    image.paste(img, offset)
    with BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))