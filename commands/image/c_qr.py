import qrcode
from io import BytesIO
import PIL, commands

async def run_command(discord, message, args, client, opt): 

    if len(args) < 2:
        await message.reply("i need some text to do that")
        return await commands.run_command("help", discord, message, ["u>help", "qr"], client, [])
    args.pop(0)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(" ".join(args))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    with BytesIO() as image_binary:
        img.save(image_binary, 'PNG')
        image_binary.seek(0)
        await message.reply(file=discord.File(fp=image_binary, filename='qrcode.png'))