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

thread_pool = ThreadPoolExecutor()


async def run_command(discord, message, args, client, opt): 
    args.pop(0)
    
    if len(message.attachments) < 1 and not message.reference:
        await message.reply("i need an image to do that")
        return await commands.run_command("help", discord, message, ["u>help", "caption"], client, [])
    if len(message.attachments) > 0:
        content = message.attachments[0]
        url = content.url
        content = Image.open(BytesIO(await content.read()))

    if message.reference:
        messageref = await message.channel.fetch_message(message.reference.message_id)
        if messageref.attachments:
            content = messageref.attachments[0]
            url = content.url
            content = Image.open(BytesIO(await content.read()))

        if messageref.embeds:
            stinkytenormp4 = False
            if "https://tenor.com/view/" in str(messageref.embeds[0].url):
                stinkytenormp4 = True
                async with aiohttp.ClientSession() as session:
                    tenor_id = messageref.embeds[0].url.split("-").pop()
                    tenorapikey = os.getenv("TENOR")
                    async with session.get(f"https://g.tenor.com/v1/gifs?ids={tenor_id}&media_filter=minimal&limit=1&key={tenorapikey}") as resp:
                        outurl = json.loads(await resp.read())["results"][0]["media"][0]["gif"]["url"]
                        async with aiohttp.ClientSession() as session:
                            async with session.get(str(outurl)) as resp:
                                content = Image.open(BytesIO(await resp.read()))

            if stinkytenormp4 == False:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(messageref.embeds[0].url)) as resp:
                        content = Image.open(BytesIO(await resp.read()))

            url = messageref.embeds[0].url
        if not messageref.attachments and not messageref.embeds:
            await message.reply("i need an image attachment to do that and this message you're replying to doesn't have that")
            return await commands.run_command("help", discord, message, ["u>help", "caption"], client, [])

    if len(args) < 1:
        await message.reply("i need some text to do that")
        return await commands.run_command("help", discord, message, ["u>help", "caption"], client, [])


    if url.endswith("png") or url.endswith("jpg") or url.endswith("jpeg"):

        await message.add_reaction("⏱️")

        image = content

        await process_png(image, message,discord, args)

    else:
        image = content

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
    tempframes = []
    duration = []

    for frame in ImageSequence.Iterator(image):
        tempframes.append(frame)
    progmsg = await message.reply(f"processing, please wait...")

    for frame in ImageSequence.Iterator(image):
        duration.append(frame.info['duration'])

        fontscale = 11

        fnt = ImageFont.truetype("image/fonts/futura.otf", 2 + ceil(frame.size[0] // fontscale))

        n = frame.size[0]//fnt.getsize("a")[0]

        textarray = textwrap.wrap(" ".join(args), break_long_words=True, width=n)

        offset = 0
        size = (frame.size[0],(len(textarray) * fnt.getsize("y")[1]))

        textout = Image.new("RGBX", size, (255, 255, 255, 0))
        textbg = Image.new("RGBX", size, color = 'white')
        textbg2 = Image.new("RGBX", (size[0], size[1]+fnt.getsize("y")[1]), color = 'white')
        nd = ImageDraw.Draw(textout)

        for line in textarray:
            nd.text((size[0]/2, offset), line, font=fnt, anchor="mt", fill="#000000")
            offset += fnt.getsize("y")[1]

        finalout = Image.new("RGBX", (frame.size[0], frame.size[1] + size[1] + fnt.getsize("y")[1]), (255, 255, 255, 0))
        
        textbg.paste(textout)
        textbg2.paste(textbg, (0,fnt.getsize("y")[1]//2))
        textbg = textbg2
        frame.convert(mode='RGBX',
            palette=Image.ADAPTIVE,
            # colors=256,
            # dither=1
        )
        finalout.paste(image, (0, textbg.size[1]))
        finalout.paste(textbg, (0,0))
            
        frames.append(finalout)
        
    with BytesIO() as image_binary:
        frames[0].save(image_binary, 'GIF', save_all=True, optimize=False, duration=duration, loop=0, disposal=2, append_images=frames[1:])
        image_binary.seek(0)
        await message.reply(file=discord.File(image_binary, "image.gif"))
        await progmsg.delete()