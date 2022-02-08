import sys
sys.path.append('commands')
import fun.c_fnaf as c_fnaf, general.c_first as c_first, general.c_help as c_help, other.c_image as c_image, utility.c_copy as c_copy, fun.c_doodlebob as c_doodlebob, other.c_sort as c_sort, c_test, c_exec, general.c_ascii as c_ascii, utility.c_emojipack as c_emojipack, general.c_ping as c_ping, utility.c_purge as c_purge, utility.c_emoji as c_emoji, image.c_saturate as c_saturate, image.c_jpeg as c_jpeg
import image.c_grayscale as c_grayscale, image.c_ifunny as c_ifunny, image.c_qr as c_qr
import db, json
from os.path import exists

gametesters = [839035980371460107, 821432433491705977]

async def run_command(command, discord, message, args, client, opt):
    if command == "fnaf":
        await c_fnaf.run_command(discord, message, args, client, opt)
    if command == "first":
        await c_first.run_command(discord, message, args, client, opt)
    if command == "help":
        await c_help.run_command(discord, message, args, client, opt)
    if command == "image":
        await c_image.run_command(discord, message, args, client, opt)
    if command == "copy":
        await c_copy.run_command(discord, message, args, client, opt)
    if command == "doodlebob":
        await c_doodlebob.run_command(discord, message, args, client, opt)
    if command == "sort":
        await c_sort.run_command(discord, message, args, client, opt)
    if command == "test" and message.author.id in gametesters:
        await c_test.run_command(discord, message, args, client, opt)
    if command == "exec" and message.author.id == 839035980371460107:
        await c_exec.run_command(discord, message, args, client, opt)
    if command == "ascii":
        await c_ascii.run_command(discord, message, args, client, opt)
    if command == "emojipack":
        await c_emojipack.run_command(discord, message, args, client, opt)
    if command == "ping":
        await c_ping.run_command(discord, message, args, client, opt)
    if command == "purge":
        await c_purge.run_command(discord, message, args, client, opt)
    if command == "emoji":
        await c_emoji.run_command(discord, message, args, client, opt)
    if command == "saturate":
        await c_saturate.run_command(discord, message, args, client, opt)
    if command == "jpeg":
        await c_jpeg.run_command(discord, message, args, client, opt)
    if command == "grayscale":
        await c_grayscale.run_command(discord, message, args, client, opt)
    if command == "ifunny":
            await c_ifunny.run_command(discord, message, args, client, opt)
    if command == "qr":
            await c_qr.run_command(discord, message, args, client, opt)

    activity_measure(message)

def activity_measure(message):
    activity = db.dbget("database/activity.json")

    usertosave = str(message.author.id)
    activity.setdefault(usertosave, 0)
    
    activity[usertosave] = activity[usertosave] + 1
    db.dbwrite(activity, "database/activity.json")
