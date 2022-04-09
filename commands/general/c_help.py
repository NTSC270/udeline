import sys
sys.path.append('helpers')
import helper, db, markup_ansi
import datetime, markup_ansi

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
    all_cmds = []
    utility = []
    fun = []
    general = []
    other = []
    image = []

    commands_descriptive = db.dbget("helpers/commands.json")

    coloring = {"guildonly": markup_ansi.getc("blue", "1"),
                "": "",
                "forbidden": markup_ansi.getc("red", "1") + markup_ansi.getc("underline", "0")
               }
    for x in commands_descriptive:
        if len(commands_descriptive[x]) > 4:
            if commands_descriptive[x][4] == "util":
                cmdname = coloring[commands_descriptive[x][5]] + x + "[0;0m"
                utility.append(cmdname)
            if commands_descriptive[x][4] == "fun":
                cmdname = coloring[commands_descriptive[x][5]] + x + "[0;0m"
                fun.append(cmdname)
            if commands_descriptive[x][4] == "general":
                cmdname = coloring[commands_descriptive[x][5]] + x + "[0;0m"
                general.append(cmdname)
            if commands_descriptive[x][4] == "other":
                cmdname = coloring[commands_descriptive[x][5]] + x + "[0;0m"
                other.append(cmdname)
            if commands_descriptive[x][4] == "image":
                cmdname = coloring[commands_descriptive[x][5]] + x + "[0;0m"
                image.append(cmdname)
            all_cmds.append(x)

    embed=discord.Embed(description="**prefixes: `"+" ".join(helper.prefixes[client.user.name])+"`**\nblue commands may only be available in guilds, or work differently outside guilds", color=0x00ccff)
    embed.set_author(name=f"{client.user.name} help",icon_url=f"{client.user.display_avatar.url}")
    embed.add_field(name=f"general {helper.udel_emoji[client.user.name]}", value="```ansi\n"+", ".join(general)+"```")
    embed.add_field(name=f"utility {helper.udel_emoji[client.user.name]}", value="```ansi\n"+", ".join(utility)+"```")
    embed.add_field(name=f"fun {helper.udel_emoji[client.user.name]}", value="```ansi\n"+", ".join(fun)+"```")
    embed.add_field(name=f"other {helper.udel_emoji[client.user.name]}", value="```ansi\n"+", ".join(other)+"```")
    embed.add_field(name=f"image {helper.udel_emoji[client.user.name]}", value="```ansi\n"+", ".join(image)+"```")
    
    funfacts = open('misc/fun_facts.txt').readlines()
    now = datetime.datetime.today()
    embed.set_footer(text="Did you know? "+funfacts[now.day % len(funfacts)])
    await message.reply(embed=embed)