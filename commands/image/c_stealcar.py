

from math import ceil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageSequence
from io import BytesIO
import requests
import textwrap
import commands


async def run_command(discord, message, args, client, opt): 
    # args.pop(0)

    # if len(args) < 1:
    #     await message.reply("i need some text to do that")
    #     return await commands.run_command("help", discord, message, ["u>help", "caption"], client, [])


    await message.add_reaction("⏱️")

    # fontscale = 11.25

    fnt = ImageFont.truetype("image/fonts/xband.ttf", 60)

    textout = Image.new("RGBA", (600,600), (255, 255, 255, 0))
    textbg = Image.new("RGBA", (600,600), color = 'black')
    nd = ImageDraw.Draw(textout)

    nd.text((600/2, 600/2), "YOU WOULDN'T \nSTEAL A CAR", font=fnt, anchor="mt", fill=(255, 255, 255, 255))
    
    out = Image.alpha_composite(textbg, textout)

    with BytesIO() as image_binary:
        out.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.remove_reaction("⏱️", message.guild.me)
        await message.reply(file=discord.File(image_binary, "image.png"))

