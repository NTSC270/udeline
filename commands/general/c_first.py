

async def run_command(discord, message, args, client, opt):

    message_first = await message.channel.history(oldest_first=True, limit=1).flatten()
    message_first = message_first[0]
    await message_first.reply("🌠")