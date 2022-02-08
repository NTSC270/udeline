import db, commands

async def run_command(discord, message, args, client, opt):
    args.pop(0)

    if len(args) < 1:
        return await commands.run_command("help", discord, message, ["u>help", "ascii"], client, [])