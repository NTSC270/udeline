import sys

sys.path.append('helpers')
import datetime
import math
from io import BytesIO
import helper
import db
from PIL import Image, ImageDraw, ImageFilter, ImageFont


async def run_command(discord, message, args, client, opt):
    if len(args) > 1:
        commands_descriptive = db.dbget("helpers/commands.json")

        if args[1] in commands_descriptive:
            embed = discord.Embed(color=0x00ccff)
            if args[1] == "exec":
                embed.description = commands_descriptive[args[1]][0]+"```ansi\n[1;31m[4;31mahahahaha you cannot use it exec is bot owner only evil face```"
            else:
                embed.description = commands_descriptive[args[1]][0]+"```ansi\n[0;31m```"
            embed.add_field(name="usage", value=args[0].replace("help", "")+commands_descriptive[args[1]][1], inline=True)
            embed.add_field(name="options", value=commands_descriptive[args[1]][2], inline=True)
            embed.add_field(name="example use", value="`"+args[0].replace("help", "")+commands_descriptive[args[1]][3]+"`", inline=False)
            embed.set_author(name="udeline: "+args[1],icon_url="https://media.discordapp.net/attachments/913898937532940371/937629996476956682/udeline.png")
            return await message.reply(embed=embed)
        else:
            return await message.reply("that command doesn't exist")
    image = []

    command_categories = {
        "utility": [],
        "fun": [],
        "general": [],
        "other": [],
        "image": []
    }

    commands_descriptive = db.dbget("helpers/commands.json")

    for x in commands_descriptive:
        if len(commands_descriptive[x]) > 4:
            if commands_descriptive[x][5] == "guildonly":
                command_categories[commands_descriptive[x][4]].append("*"+x)
            elif commands_descriptive[x][5] == "forbidden":
                command_categories[commands_descriptive[x][4]].append("&"+x)
            else:
                command_categories[commands_descriptive[x][4]].append(x)

    image = Image.open(f"image/resources/{client.user.name}.png")
    image = image.filter(ImageFilter.GaussianBlur(radius=0))

    fontscale = 32
    smallfontscale = 20

    draw = ImageDraw.Draw(image)
    categoryfont = ImageFont.truetype("image/fonts/whitrabt.ttf", fontscale)
    font = ImageFont.truetype("image/fonts/whitrabt.ttf", smallfontscale)

    categories = ["general", "utility", "other", "image", "fun"]

    size = len(categories)
    radius = 235
    multiply = 0.8

    for x in range(size):
        theta = ((math.pi*2) / size)
        offsetx = 50
        offsety = 50
        angle = (theta * x)+4.3

        draw.text(((image.size[0]/2)-offsetx + math.sin(angle) * radius, (image.size[1]/2)-offsety + math.cos(angle) * (radius*multiply)), categories[x] ,(255,255,255),font=categoryfont,stroke_width=2, stroke_fill="black")
        for y in range(len(command_categories[categories[x]])):
            if "*" in command_categories[categories[x]][y]:
                draw.text(((image.size[0]/2)-offsetx + math.sin(angle) * radius, (image.size[1]/2)-offsety + math.cos(angle) * (radius*multiply)+fontscale+y*smallfontscale), command_categories[categories[x]][y].replace("*", "") ,(128,200,255),font=font,stroke_width=1, stroke_fill="black")
            elif "&" in command_categories[categories[x]][y]:
                draw.text(((image.size[0]/2)-offsetx + math.sin(angle) * radius, (image.size[1]/2)-offsety + math.cos(angle) * (radius*multiply)+fontscale+y*smallfontscale), command_categories[categories[x]][y].replace("&", "") ,(255,64,64),font=font,stroke_width=1, stroke_fill="black")
            else:
                draw.text(((image.size[0]/2)-offsetx + math.sin(angle) * radius, (image.size[1]/2)-offsety + math.cos(angle) * (radius*multiply)+fontscale+y*smallfontscale), command_categories[categories[x]][y] ,(255,255,255),font=font,stroke_width=1, stroke_fill="black")

    embed=discord.Embed(description="**prefixes: `"+" ".join(helper.prefixes[client.user.name])+"`**\nblue commands may only be available in guilds, or work differently outside guilds", color=0x00ccff)
    embed.set_author(name=f"{client.user.name} help",icon_url=f"{client.user.display_avatar.url}")

    funfacts = open('misc/fun_facts.txt').readlines()
    now = datetime.datetime.today()
    embed.set_footer(text="Did you know? "+funfacts[now.day % len(funfacts)])

    with BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        file = discord.File(image_binary, filename="image.png")
        embed.set_image(url="attachment://image.png")
        await message.reply(file=file,embed=embed)
