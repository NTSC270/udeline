    
    
from PIL import Image
from io import BytesIO
import commands
from imageget import get_image


async def run_command(discord, message, args, client, opt): 

    image = await get_image(message=message,client=client)
    if image is None:
        await message.reply("i need an image to do that")
        return await commands.run_command("help", discord, message, ["u>help", "saturate"], client, [])

    progmsg = await message.reply(f"processing, please wait...")

    image = image.convert('RGBA')
    newimage = Image.new(size=(image.size[0]*3,image.size[1]*3), mode="RGBA")
    
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = image.getpixel((x,y))
            for z in range(3):
                newimage.putpixel((x*3,y*3+z), (pixel[0],0,0))
                newimage.putpixel((x*3+1,y*3+z), (0,pixel[1],0))
                newimage.putpixel((x*3+2,y*3+z), (0,0,pixel[2]))

    with BytesIO() as image_binary:
        newimage.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.png"))
        await progmsg.delete()