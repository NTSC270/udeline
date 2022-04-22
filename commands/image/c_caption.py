from math import ceil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageSequence
from io import BytesIO
import aiohttp
import textwrap
import commands
import json
import os
from dotenv import load_dotenv
load_dotenv()

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
        return await commands.run_command("help", discord, message, ["u>help", "caption"], client, [])

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

async def process_png(image, message, discord, args):

    fontscale = 11

    fnt = ImageFont.truetype("image/fonts/futura.otf", 2 + ceil(image.size[0] // fontscale))

    wordlist = " ".join(args).split(" ")
    n = image.size[0]//fnt.getsize("a")[0]
    for x in wordlist:
        x = " ".join([x[i:i+n] for i in range(0, len(x), n)])

    textarray = textwrap.wrap(" ".join(args), break_long_words=True, width=n)

    offset = 0
    size = (image.size[0],(len(textarray) * fnt.getsize("y")[1]))

    textout = Image.new("RGBA", size, (255, 255, 255, 0))
    textbg = Image.new("RGBA", size, color = 'white')
    textbg2 = Image.new("RGBA", (size[0], size[1]+fnt.getsize("y")[1]), color = 'white')
    nd = ImageDraw.Draw(textout)

    for line in textarray:
        nd.text((size[0]/2, offset), line, font=fnt, anchor="mt", fill="#000010")
        offset += fnt.getsize("y")[1]

    finalout = Image.new("RGBA", (image.size[0], image.size[1] + size[1] + fnt.getsize("y")[1]), (255, 255, 255, 0))
    
    out = Image.alpha_composite(textbg, textout)
    textbg2.paste(out, (0,fnt.getsize("y")[1]//2))
    out = textbg2
    finalout.paste(image, (0, textbg.size[1]+fnt.getsize("y")[1]))
    finalout.paste(out, (0,0))
    
    with BytesIO() as image_binary:
        finalout.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.remove_reaction("⏱️", message.guild.me)
        await message.reply(file=discord.File(image_binary, "image.png"))

async def process_gif(image, message, discord, args):
    frames = []
    duration = []
    
    progmsg = await message.reply(f"processing, please wait...")

    for frame in ImageSequence.Iterator(image):

        frame.convert(mode='RGBA',
            palette=Image.ADAPTIVE
        )
        
        duration.append(frame.info['duration'])

        fontscale = 11
        fnt = ImageFont.truetype("image/fonts/futura.otf", 2 + ceil(frame.size[0] // fontscale))
        n = frame.size[0]//fnt.getsize("a")[0]

        textarray = textwrap.wrap(" ".join(args), break_long_words=True, width=n)

        offset = 0
        size = (frame.size[0],(len(textarray) * fnt.getsize("y")[1]))

        textout = Image.new("P", size, (255, 255, 255, 0))
        textbg = Image.new("P", size, color = 'white')
        textbg2 = Image.new("P", (size[0], size[1]+fnt.getsize("y")[1]), color = 'white')
        nd = ImageDraw.Draw(textout)

        for line in textarray:
            nd.text((size[0]/2, offset), line, font=fnt, anchor="mt", fill="#000000")
            offset += fnt.getsize("y")[1]

        finalout = Image.new("RGBA", (frame.size[0], frame.size[1] + size[1] + fnt.getsize("y")[1]), (255, 255, 255, 0))
        
        textbg.paste(textout)
        textbg2.paste(textbg, (0,fnt.getsize("y")[1]//2))
        textbg = textbg2
        
        textbg.convert(mode='RGBA',
            palette=Image.ADAPTIVE
        )

        finalout.paste(image, (0, textbg.size[1]))
        finalout.paste(textbg, (0,0))

        finalout.convert(mode='P',
            palette=Image.ADAPTIVE
        )
            
        frames.append(finalout)

    frames.pop(1)
        
    with BytesIO() as image_binary:
        frames[0].save(image_binary, 'GIF', save_all=True, optimize=False, duration=duration, loop=0, disposal=2, append_images=frames[1:])
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.gif"))
        await progmsg.delete()