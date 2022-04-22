import secrets
import helpers.db as db

async def run_command(discord, message, args, client, opt):
    leader = db.dbget('database/activity.json')
    output = {k: v for k, v in sorted(leader.items(), key=lambda item: item[1])}
    array = []
    for x in output:
        user = await client.fetch_user(x)
        array.append(f"**{user.name}#{user.discriminator}**: {output[x]}")
    array.reverse()

    array[0] = "🏅 "+array[0]
    array[1] = "🥈 "+array[1]
    array[2] = "🥉 "+array[2]
    for x in range(len(array)):
        if x > 2:
            array[x] = "▫️ "+array[x]

    array = array[:10]
    array.append("...")

    embed = discord.Embed(description="\n".join(array),title="bot usage leaderboard")

    return await message.reply(embed=embed)