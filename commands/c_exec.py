import textwrap, contextlib, io
from traceback import format_exception
textwrap.tabsize = 4
import datetime
from syntax_highlight import highlighting as style


async def run_command(discord, message, args, client, opt):

    if message.content.startswith("u>exec"):
        code = message.content.replace("u>"+"exec"+" ", "")
    else:
        code = message.content.replace("u>>"+"exec"+" ", "")

    if code.startswith("```py"):
        code = code[5:]
        code = code[:len(code) - 3]
    code = code.replace("    ", "   ")
    code = textwrap.indent(code, "   ")
    try:
        local_vars = {
            "discord": discord,
            "client": client,
            "message": message,
            "args": args
        }
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{code}", local_vars
            )
            obj = await local_vars["func"]()
            result = f"{stdout.getvalue()}\n{style(str(obj))}"

            if(obj != None):
                f = io.BytesIO(bytes(result, "utf8"))
                await message.reply(file=discord.File(f, "output.ansi"))

    except Exception as e:
        exception = style("".join(format_exception(e, e, e.__traceback__)))
        f = io.BytesIO(bytes(exception, "utf8"))
        await message.reply(file=discord.File(f, "output.ansi"))