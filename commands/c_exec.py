import textwrap, contextlib, io
from traceback import format_exception
textwrap.tabsize = 4


async def run_command(discord, message, args, client, opt):


    code = message.content.replace("u>"+"exec"+" ", "")
    if code.startswith("```py"):
        code = code[5:]
        code = code[:len(code) - 3]
    code = code.replace("    ", "   ")
    code = textwrap.indent(code, "   ")
    try:
        local_vars = {
            "discord": discord,
            "client": client,
            "message": message
        }
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{code}", local_vars
            )
            obj = await local_vars["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"

            await message.reply("```py\n"+result[0:1990]+"```")
            # f = io.BytesIO(bytes(result, "utf8"))
            # await message.reply(file=discord.File(f, "output.txt"))

    except Exception as e:
        await message.reply("```m\n"+("".join(format_exception(e, e, e.__traceback__)))[0:1992]+"```")