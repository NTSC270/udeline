from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageSequence
from io import BytesIO
import os
from dotenv import load_dotenv
load_dotenv()
import commands
import aiohttp, os, json
import textwrap

from math import floor, sqrt

from functools import partial
from concurrent.futures import ThreadPoolExecutor
import asyncio
from imageget import get_image

thread_pool = ThreadPoolExecutor()



async def run_command(discord, message, args, client, opt): 
    args.pop(0)

    image = await get_image(message=message,client=client)
    url = image.url

    if len(args) < 1:
        await message.reply("i need some text to do that")
        return await commands.run_command("help", discord, message, ["u>help", "caption2"], client, [])

    if url.endswith("png") or url.endswith("jpg") or url.endswith("jpeg"):
        await message.add_reaction("⏱️")
        await process_png(image, message,discord, args)

    else:
        loop = asyncio.get_running_loop()
        try:
            await loop.run_in_executor(
                thread_pool, 
                partial(await process_gif(image, message, discord, args))
            )
        except:
            pass

async def process_png(image, args, discord, message):

    fontscale = 12

    fnt = ImageFont.truetype("image/fonts/sansserif.ttf", image.size[0]//fontscale)

    textlist = " ".join(args)

    n = image.size[0]//fnt.getsize("a")[0]
    
    textarray = textwrap.wrap(textlist, break_long_words=True, width=n)

    textbg = Image.new("RGBA", (image.size[0],len(textarray) * fnt.getsize("y")[1]), color = 'white')

    textcontext = ImageDraw.Draw(textbg)

    offset = 0

    for line in textarray:
        textcontext.text((fnt.getsize("a")[0],offset), line, font=fnt, fill="black")
        offset += fnt.getsize("y")[1]

    finalout = Image.new("RGBA", (image.size[0], image.size[1]+textbg.size[1]+fnt.getsize("a")[1]), color="white")

    finalout.alpha_composite(image)
    finalout.alpha_composite(textbg, (0,image.size[1]+fnt.getsize("a")[1]//2))

    with BytesIO() as image_binary:
        finalout.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.remove_reaction("⏱️", message.guild.me)
        await message.reply(file=discord.File(image_binary, "image.png"))

async def process_gif(args, discord, message, content):
        frames = []
        duration = []
            
        image = content

        progmsg = await message.reply(f"processing, please wait...")

        for frame in ImageSequence.Iterator(image):

            frame.convert(mode='RGBX',
                palette=Image.ADAPTIVE,
                # colors=256,
                # dither=1
            )
            duration.append(frame.info['duration'])

            fontscale = 12

            fnt = ImageFont.truetype("image/fonts/sansserif.ttf", frame.size[0]//fontscale)

            textlist = " ".join(args)

            n = frame.size[0]//fnt.getsize("a")[0]
            
            textarray = textwrap.wrap(textlist, break_long_words=True, width=n)

            textbg = Image.new("RGBX", (frame.size[0],len(textarray) * fnt.getsize("y")[1]), color = 'white')

            textcontext = ImageDraw.Draw(textbg)

            offset = 0

            for line in textarray:
                textcontext.text((fnt.getsize("a")[0],offset), line, font=fnt, fill="black")
                offset += fnt.getsize("y")[1]

            finalout = Image.new("RGBX", (frame.size[0], frame.size[1]+textbg.size[1]+fnt.getsize("a")[1]), color="white")

            finalout.paste(frame)
            finalout.paste(textbg, (0,frame.size[1]+fnt.getsize("a")[1]//2))

            frames.append(finalout)

        with BytesIO() as image_binary:
            frames[0].save(image_binary, 'GIF', save_all=True, optimize=False, duration=duration, loop=0, disposal=2, append_images=frames[1:])
            image_binary.seek(0)
            await message.reply(file=discord.File(image_binary, "image.gif"))
            await progmsg.delete()
