import math, random
from time import sleep
import asyncio
from game.render import render
async def get_move(client, message, check, message_game, array, plr, discord, flag):
    
    if plr == flag:
        return await message.reply("you win!")
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await message.reply("you didn't move in a minute so i stopped the game")
    else:
        print(reaction)
        if str(reaction) == "<:up:939511415864180756>":
            plr = (plr[0]-1,plr[1])
        if str(reaction) == "<:dn:939511415910309908>":
            plr = (plr[0]+1,plr[1])
        if str(reaction) == "<:lt:939511415948050482>":
            plr = (plr[0],plr[1]-1)
        if str(reaction) == "<:rt:939511415537012767>":
            plr = (plr[0],plr[1]+1)
        embed = discord.Embed(description = render.draw(array, plr, flag), title="get to the flag!")
        await message_game.edit(embed=embed)
        await message.remove_reaction(str(reaction), message.author)
        await get_move(client, message, check, message_game, array, plr, discord, flag)


async def run_command(discord, message, args, client, opt): 
    array = [[1 for x in range(5)] for y in range(5)] 
    plr = (3,1)
    flag = (1,3)

    #init game
    for x in range(3):
        for y in range(3):
            array[1+x][1+y] = 0

    embed = discord.Embed(description = render.draw(array, plr, flag), title="get to the flag!")

    message_game = await message.reply(embed=embed)

    await message_game.add_reaction("<:up:939511415864180756>")
    await message_game.add_reaction("<:dn:939511415910309908>")
    await message_game.add_reaction("<:lt:939511415948050482>")
    await message_game.add_reaction("<:rt:939511415537012767>")

    def check(reaction, user):
        return user == message.author

    await get_move(client, message, check, message_game, array, plr, discord, flag)

    


