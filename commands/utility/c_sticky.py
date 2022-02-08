import db, commands

async def run_command(discord, message, args, client, opt):
    args.pop(0)

    if len(args) < 1:
        await message.reply("i need some text to make the sticky")
        return await commands.run_command("help", discord, message, ["u>help", "sticky"], client, [])
    
        