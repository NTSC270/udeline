async def run_command(discord, message, args, client, opt):
    args.pop(0)
    if len(args) < 1:
        return await message.reply("i need some text to do that")
    args.sort()
    await message.reply(" ".join(args))

