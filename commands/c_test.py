
# from PIL import Image
# from PIL import ImageOps
# from io import BytesIO
# import PIL, glob, os, math, re, commands
# import requests
# from math import floor
# from scipy.spatial import distance
# import io
# from helpers.userget import get_user as get_user



import db

from PyDictionary import PyDictionary 
import difflib
dictionary=PyDictionary() 

async def run_command(discord, message, args, client, opt): 
    args.pop(0)
    output = []

    activity = db.dbget("misc/emoji_cldr.json")

    for x in list(args):
        output.append(x) 
        for key in activity:
            syns = []
            try:
                syns = dictionary.synonym(x, disable_errors=True)
            except:
                pass

            if x in key or key in x[0:6] or key[0:6] in syns:
                matches = difflib.get_close_matches(x, activity.keys())
                output.append(activity[matches[0] or activity[key]])
                break
        
    return await message.reply(" ".join(output))

    # args.pop(0)

    # binary = f'{int(" ".join(args)):08b}'
    # binary = binary.replace("0", "\\🔳")
    # binary = binary.replace("1", "\\⬜")

    # user = await get_user(query=message.author.name, client=client, message=message)

    # await message.reply(binary)

















    # if len(message.attachments) < 1 and not message.reference:
    #     await message.reply("i need an image to do that")
    #     return await commands.run_command("help", discord, message, ["u>help", "jpeg"], client, [])

    # if len(message.attachments) > 0:
    #     content = message.attachments[0]

    # if message.reference:
    #     messageref = await message.channel.fetch_message(message.reference.message_id)
    #     if messageref.attachments:
    #         content = messageref.attachments[0]
    #     if messageref.embeds:
    #         response = requests.get(messageref.embeds[0].url)
    #         content = response.content
    #     if not messageref.attachments and not messageref.embeds:
    #         await message.reply("i need an image attachment to do that and this message you're replying to doesn't have that")
    #         return await commands.run_command("help", discord, message, ["u>help", "jpeg"], client, [])

    # image = Image.open(BytesIO(await content.read()))
    # image = image.convert('RGB')

    # # colors = ( (0,0,0),(255,0,0), (0,255,0), (255,255,0), (0,0,255), (255,0,255), (0,255,255), (255,255,255) )
    # colors = ( (0,0,0),(34,39,94), (255,255,255), (27,32,76))

    # maxscale = 999999

    # if image.size[0] > maxscale:
    #     scale = (maxscale/image.size[0])
    #     image = image.resize((floor(image.size[0]*scale), floor((image.size[1]*scale))), Image.LINEAR)

    # for x in range(image.size[0]):
    #     for y in range(image.size[1]):
    #         color_dist = []
    #         pixel = image.getpixel((x,y))
    #         for z in colors:
    #             color_dist.append(distance.euclidean(pixel, z))
    #         image.putpixel((x,y), colors[color_dist.index(min(color_dist))])
    
    # with BytesIO() as image_binary:
    #     image.save(image_binary, 'PNG')
    #     image_binary.seek(0)
    #     await message.reply(file=discord.File(image_binary, "image.png"))