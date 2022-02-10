import commands

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

    badges_dict = {
        "nitro": "<:Nitro:941286823957774357>",
        "bug_hunter": "<:BugHunter:941263563643838494>",
        "bug_hunter2": "<:BugHunter2:941267025890783252>",
        "early_supporter": "<:EarlySupporter:941280388158984203> ",
        "verified_bot": "<:VerifiedBotDev:941267025521672193>",
        "hypesquad": "<:Hypesquad:941269103472152606>",
        "balance": "<:BugHunter:941263563643838494>",
        "bravery": "<:Bravery:941267025504923648>",
        "brilliance": "<:Briliance:941267025592987708>",
        "partner": "<:Partner:941268831098261514>",
        "staff": "<:Staff:941268851671326731>",
        "verified_bot": "<:Bot1:941270505397289022><:Bot2:941270505447645185>"
    }

    user_badges = []

    guild = False

    public_flags = None

    if message.guild is not None:
        user = await message.guild.fetch_member(args[0])
        guild = True
        public_flags = user.public_flags
    else:
        user = await client.fetch_user(args[0])

    embed = discord.Embed()
    if not guild:
        embed.set_author(name=f"{user.name}#{user.discriminator}")
    else:
        embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=activity_dict[str(user.raw_status)])
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="joined discord:", value=f"<t:{int(user.created_at.timestamp())}:F>")
    if guild:
        embed.add_field(name="joined server:", value=f"<t:{int(user.joined_at.timestamp())}:F>")
    embed.add_field(name="default avatar color:", value=f"{user.default_avatar} {emoji_dict[str(user.default_avatar)]}")
    
    if user.premium_since is not None:
        public_flags.append("nitro")
    if user.public_flags.bug_hunter:
        public_flags.append("bug_hunter")
    if user.public_flags.bug_hunter_level_2:
        public_flags.append("bug_hunter2")
    
    if guild:
        roles_list = []
        for x in user.roles:
            roles_list.append(f"<@&{x.id}>")
        embed.add_field(name="roles:", value = "".join(roles_list))
    embed.add_field(name="badges:", value = user_badges)

    await message.reply(embed=embed)

    
