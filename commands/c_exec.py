import textwrap, contextlib, io
from traceback import format_exception
textwrap.tabsize = 4
from syntax_highlight import highlighting as style


async def run_command(discord, message, args, client, opt):

    if(message.author.id != 839035980371460107): return

    args.pop(0)
    code = " ".join(args)

    file = False
    mobile = False
    for x in range(len(opt)):
        opt[x] = opt[x].split("=")
        if opt[x][0] == "file":
            file = True
        if opt[x][0] == "m":
            mobile = True

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
            if stdout.getvalue() != "":
                result = f"{stdout.getvalue()}\n{style(str(obj))}"
                mresult = f"{stdout.getvalue()}\n{str(obj)}"
            else:
                result = f"{style(str(obj))}"
                mresult = f"{str(obj)}"

            if(obj != None):
                if mobile: return await message.reply(embed=discord.Embed(description=f"```py\n{mresult}```"))
                if not file: return await message.reply(embed=discord.Embed(description=f"```ansi\n{result}```"))
                f = io.BytesIO(bytes(result, "utf8"))
                await message.reply(file=discord.File(f, "output.ansi"))

    except Exception as e:
        exception = style("".join(format_exception(e, e, e.__traceback__)))
        mexception = "".join(format_exception(e, e, e.__traceback__))
        if mobile: return await message.reply(embed=discord.Embed(description=f"```py\n{mexception}```"))
        if not file: return await message.reply(embed=discord.Embed(description=f"```ansi\n{exception}```"))
        f = io.BytesIO(bytes(exception, "utf8"))
        await message.reply(file=discord.File(f, "output.ansi"))