import random
import helpers.markup_ansi
import requests, json

async def run_command(discord, message, args, client, opt):
    if len(args) > 1:
        args.pop(0)
    else:
        return await message.reply("i need a text prompt to do that")
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': " ".join(args),
        },
        headers={'api-key': '23e20387-716c-41e4-9773-2a653e726b32'}
    )

    await message.reply(json.loads(r.text)["output_url"])

