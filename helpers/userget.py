

async def get_user(query=None,client=None,message=None):
    if client == None:
        return

    user_id = None
    name = None
    isnum = False

    try:
        int(query)
        isnum = True
    except:
        isnum = False

    if isnum:
        user_id = int(query)
    else:
        name = query

    if user_id == None and name == None and message == None:
        return

    if len(message.mentions) > 0:
        return message.mentions[0]

    if user_id is not None and message.guild is not None:
        return message.guild.get_member(user_id)
    if user_id is not None and message.guild is None:
        return await client.fetch_user(user_id)
    if name is not None and message.guild is not None:
        guildusers = message.guild.members 
        memberuser = next((x for x in guildusers if name in x.name.lower()), None)

        allusers = client.users
        clientuser = next((x for x in allusers if name in x.name.lower()), None)

        return memberuser or clientuser
    if name is not None and message.guild is None:
        allusers = client.users
        return next((x for x in allusers if name in x.name.lower()), None)