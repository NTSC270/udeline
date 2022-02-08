import sys
sys.path.append('helpers')
import helper, db, markup_ansi
import datetime

async def run_command(discord, message, args, client, opt):
    if len(args) > 1:
        commands_descriptive = db.dbget("helpers/commands.json")

        if args[1] in commands_descriptive:
            embed=discord.Embed( description=commands_descriptive[args[1]][0]+"```ansi\n[0;31m```", color=0x00ccff)
            embed.add_field(name="usage", value=args[0].replace("help", "")+commands_descriptive[args[1]][1], inline=True)
            embed.add_field(name="options", value=commands_descriptive[args[1]][2], inline=True)
            embed.add_field(name="example use", value="`"+args[0].replace("help", "")+commands_descriptive[args[1]][3]+"`", inline=False)
            embed.set_author(name="udeline: "+args[1],icon_url="https://media.discordapp.net/attachments/913898937532940371/937629996476956682/udeline.png")
            return await message.reply(embed=embed)
        else:
            return await message.reply("that command doesn't exist")
    all_cmds = []
    utility = []
    fun = []
    general = []
    other = []
    image = []

    commands_descriptive = db.dbget("helpers/commands.json")
    for x in commands_descriptive:
        if len(commands_descriptive[x]) > 4:
            if commands_descriptive[x][4] == "util":
                utility.append(x)
            if commands_descriptive[x][4] == "fun":
                fun.append(x)
            if commands_descriptive[x][4] == "general":
                general.append(x)
            if commands_descriptive[x][4] == "other":
                other.append(x)
            if commands_descriptive[x][4] == "image":
                image.append(x)
            all_cmds.append(x)

    embed=discord.Embed(description="**prefixes: `"+", ".join(helper.prefixes[client.user.name])+"`**", color=0x00ccff)
    embed.set_author(name=f"{client.user.name} help",icon_url=f"{client.user.avatar_url}")
    embed.add_field(name=f"general {helper.udel_emoji[client.user.name]}", value="```m\n"+", ".join(general)+"```")
    embed.add_field(name=f"utility {helper.udel_emoji[client.user.name]}", value="```m\n"+", ".join(utility)+"```")
    embed.add_field(name=f"fun {helper.udel_emoji[client.user.name]}", value="```m\n"+", ".join(fun)+"```")
    embed.add_field(name=f"other {helper.udel_emoji[client.user.name]}", value="```m\n"+", ".join(other)+"```")
    embed.add_field(name=f"image {helper.udel_emoji[client.user.name]}", value="```m\n"+", ".join(image)+"```")
    
    funfacts = open('misc/fun_facts.txt').readlines()
    now = datetime.datetime.today()
    embed.set_footer(text="Did you know? "+funfacts[now.day % len(funfacts)])
    await message.reply(embed=embed)