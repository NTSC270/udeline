from PIL import Image
from io import BytesIO
import aiohttp
import json
import os
from userget import get_user

async def get_image(message=None,client=None):
    tempargs = message.content.split(" ")
    tempargs.pop(0)

    user = await get_user(query=" ".join(tempargs),client=client,message=message)

    if len(message.attachments) > 0:
        content = message.attachments[0]
        image = Image.open(BytesIO(await content.read()))
        image.url = content.url
        return image

    if message.reference:
        messageref = await message.channel.fetch_message(message.reference.message_id)
        if messageref.attachments:
            content = messageref.attachments[0]
            image = Image.open(BytesIO(await content.read()))
            image.url = content.url
            return image

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
                                image = Image.open(BytesIO(await resp.read()))
                        image.url = messageref.embeds[0].url
                        return image

            if stinkytenormp4 == False:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(messageref.embeds[0].url)) as resp:
                        image = Image.open(BytesIO(await resp.read()))
                        image.url = messageref.embeds[0].url
                        return image

    if user is not None:
        async with aiohttp.ClientSession() as session:
            async with session.get(str(user.display_avatar.url)) as resp:
                image = Image.open(BytesIO(await resp.read()))
                image.url = user.display_avatar.url
                return image
