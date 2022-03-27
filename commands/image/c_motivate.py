from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()
import commands
import textwrap

from math import floor

from imageget import get_image


async def run_command(discord, message, args, client, opt): 
    args.pop(0)

    image = await get_image(message=message,client=client)
    
    if len(args) < 1:
        await message.reply("i need some text to do that")
        return await commands.run_command("help", discord, message, ["u>help", "motivate"], client, [])

    await message.add_reaction("⏱️")
    image = image.convert("RGBA")

    minscale = 256
    fontscale = 7
    pdscale = 1.2

    if image.size[0] < minscale:
        scale = minscale/image.size[0]
        image = image.resize((floor(image.size[0]*scale), floor(image.size[1]*scale)), Image.NEAREST)


    textbg = Image.new("RGBA", (floor(image.size[0]*pdscale),floor(image.size[1]*pdscale)), color = 'black')
    

    textbgdraw = ImageDraw.Draw(textbg)

    composite_position_tl = (floor(textbg.size[0]//2 - image.size[0] // 2), floor(textbg.size[1] // 2 - image.size[1] // 2))
    composite_position_br = (floor(textbg.size[0]//2 + image.size[0] // 2), floor(textbg.size[1] // 2 + image.size[1] // 2))

    textbgdraw.rectangle([(composite_position_tl[0]-5, composite_position_tl[1]-5), (composite_position_br[0]+5, composite_position_br[1]+5)], fill ="white")
    textbgdraw.rectangle([(composite_position_tl[0]-3, composite_position_tl[1]-3), (composite_position_br[0]+3, composite_position_br[1]+3)], fill ="black")

    textbg.alpha_composite(image, composite_position_tl)




    fnt = ImageFont.truetype("image/fonts/timesnewroman.ttf", textbg.size[0]//fontscale)

    n = textbg.size[0]//fnt.getsize("a")[0]

    textlist = " ".join(args).split(",", 1)
    textlist[0] = textlist[0].strip()

    textarray = textwrap.wrap(textlist[0], break_long_words=True, width=n)

    textout = Image.new("RGBA", (floor(image.size[0]*pdscale),floor(fnt.getsize("y")[1] * len(textarray))+fnt.getsize("y")[1]//2), (255, 255, 255, 0))

    textcontext = ImageDraw.Draw(textout)

    offset = 0

    for line in textarray:
        textcontext.text((textbg.size[0]//2,offset), line, font=fnt, anchor="mt", fill="white")
        offset += fnt.getsize("y")[1]

    finalout = Image.new("RGBA", (textbg.size[0], textbg.size[1]+textout.size[1]), color="black")

    finalout.alpha_composite(textbg)
    finalout.alpha_composite(textout, (0,textbg.size[1]))

    if len(textlist) > 1:

        textlist[1] = textlist[1].strip()

        fnt = ImageFont.truetype("image/fonts/timesnewroman.ttf", textbg.size[0]//(fontscale*2))

        n = textbg.size[0]//fnt.getsize("a")[0]

        textarraysub = textwrap.wrap(textlist[1], break_long_words=True, width=n)

        textoutsub = Image.new("RGBA", (floor(image.size[0]*pdscale),floor(fnt.getsize("y")[1] * len(textarraysub))), (255, 255, 255, 0))

        textcontextsub = ImageDraw.Draw(textoutsub)

        offset = 0

        for line in textarraysub:
            textcontextsub.text((textbg.size[0]//2,offset), line, font=fnt, anchor="mt", fill="white")
            offset += fnt.getsize("y")[1]

        finalout = Image.new("RGBA", (textbg.size[0], textbg.size[1]+textout.size[1]+textoutsub.size[1]+fnt.getsize("y")[1]), color="black")

        finalout.alpha_composite(textbg)
        finalout.alpha_composite(textout, (0,textbg.size[1]))
        finalout.alpha_composite(textoutsub, (0,textbg.size[1]+textout.size[1]))

    with BytesIO() as image_binary:
        finalout.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.remove_reaction("⏱️", message.guild.me)
        await message.reply(file=discord.File(image_binary, "image.png"))

