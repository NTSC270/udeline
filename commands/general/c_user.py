import commands
from helper import badge_parse
from userget import get_user 
import datetime

async def run_command(discord, message, args, client, opt):
    args.pop(0)

    if len(args) < 1:
        await message.reply("i need a user id to do that")
        return await commands.run_command("help", discord, message, ["u>help", "user"], client, [])

    activity_dict = {
        "online": "https://cdn.discordapp.com/emojis/941045780289060904.webp?size=96&quality=lossless",
        "idle": "https://cdn.discordapp.com/emojis/941045780054171699.webp?size=96&quality=lossless",
        "dnd": "https://cdn.discordapp.com/emojis/941045335348904018.webp?size=96&quality=lossless",
        "offline": "https://cdn.discordapp.com/emojis/941046079330345020.webp?size=96&quality=lossless",
        "streaming": "https://cdn.discordapp.com/emojis/941045780213551104.webp?size=96&quality=lossless",
        "mobile": "https://cdn.discordapp.com/emojis/941045780125474907.webp?size=96&quality=lossless"
    }


    emoji_dict = {
        "blurple": "<:blurple:941060844047962142>",
        "grey": "<:gray:941063007063142450>",
        "green": "<:green:941063007084101733>",
        "orange": "<:yellow:941063007306391643>",
        "red": "<:red:941063007230885898>",
        "pink": "<:pink:941063007318970429>",
    }
    default_avatar_index = [
        "blurple",
        "grey",
        "green",
        "orange",
        "red",
        "pink"
    ]

    badges_dict = {
        "nitro": "<:Nitro:941286823957774357>",
        "bug_hunter": "<:BugHunter:941263563643838494>",
        "bug_hunter2": "<:BugHunter2:941267025890783252>",
        "early_supporter": "<:EarlySupporter:941280388158984203> ",
        "verified_bot_dev": "<:VerifiedBotDev:941267025521672193>",
        "hypesquad": "<:Hypesquad:941269103472152606>",
        "balance": "<:Balance:941267083767971851>",
        "bravery": "<:Bravery:941267025504923648>",
        "brilliance": "<:Briliance:941267025592987708>",
        "partner": "<:Partner:941268831098261514>",
        "staff": "<:Staff:941268851671326731>",
        "verified_bot": "<:Bot1:941270505397289022><:Bot2:941270505447645185>",
        "certified_moderator": "<:Mod:941828496504787004>"
    }

    def split_def_url(url):
        parts = url.split("/")
        parts = parts[len(parts)-1].split(".")
        return parts[0]

    guild = False

    user = await get_user(query=args[0],client=client,message=message)
    if user is None:
        return await message.reply("i can't find a user like that")
    if hasattr(user, "nick"):
        guild = True

    embed = discord.Embed()

    if not guild:
        embed.set_author(name=f"{user.name}#{user.discriminator}")
    else:
        nick = f"({user.nick})" if user.nick is not None else ""
        embed.set_author(name=f"{user.name}#{user.discriminator} {nick}", icon_url=activity_dict[str(user.raw_status)])

    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name="joined discord:", value=f"<t:{int(user.created_at.timestamp())}:F>")

    if guild:
        embed.add_field(name="joined server:", value=f"<t:{int(user.joined_at.timestamp())}:F>")


    def_avatar_name = split_def_url(user.default_avatar.url)
    embed.add_field(name="default avatar color:", value=f"{default_avatar_index[int(def_avatar_name)]} {str(emoji_dict[default_avatar_index[int(def_avatar_name)]])}")

    if guild:
        roles_list = []
        for x in user.roles:
            roles_list.append(f"<@&{x.id}>")
        roles_list.pop(0)
        embed.add_field(name="roles:", value = "@everyone" + "".join(roles_list))
        embed.add_field(name="time out:", value = f"lasts for {user.communication_disabled_until.replace(tzinfo=None) - datetime.datetime.now()}" if user.timed_out else "no", inline=False) if guild else None
        
    out = badge_parse(user)
    icon = []
    for x in out:
        icon.append(badges_dict[x])

    embed.add_field(name="badges:", value = "".join(icon) if len(icon) > 0 else "none", inline=True if len(icon) > 0 else False)
    
    embed.add_field(name="bot:", value = "yes" if user.bot else "no")


    await message.reply(embed=embed)
