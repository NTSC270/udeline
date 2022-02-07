import asyncio
from pyppeteer import launch
import commands


async def run_command(discord, message, args, client, opt):
    if client.user.name == "udevline" and message.author.id != 839035980371460107:
        return await message.reply("this command is unavailable in the development bot")
    
    args.pop(0)

    if len(args) < 1:
        await message.reply("i need an url to do that")
        return await commands.run_command("help", discord, message, ["u>help", "web"], client, [])
    
    browser = await launch()
    page = await browser.newPage()
    await page.goto(args[0])
    await page.screenshot({'path': 'example.png'})

    await message.reply(file=discord.File("example.png"))

