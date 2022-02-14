import secrets
import helpers.db as db

async def run_command(discord, message, args, client, opt):

    g = ["FNAF*", "UCN*", "NAME*", "SOMEONE'S_SOMETHING*", "RETURN*", "SNAST*"]

    f = ["Five", "Scary", "Those", "Nine", "One", "Some", "1 Minute", "Horror"]
    n = ["Nights", "Nights", "Days", "Minutes", "Weeks"]
    a = ["at", "in", "with"]
    s = ["Sebi TV's", "Freddy's", "Rachael's", "CoolingTool's", "Baldi's", "Chuck E. Cheese's", "Scaries", "Scraps", "Mr. Hippo's", "Impostor", "Goomie's"]
    
    number = ["Reignited", "2", "REMASTERED", "REMADE", "3", "4", "5", "Again", "FAN MADE"]
    t = [": Sebi's Wrath", ": The trilogy", ": Rewired", " (CANCELLED)", ": Brother Location", " (WIP)", " REUPLOADED"]

    person = ["Sebi TV's", "Goodwill's", "Freddy's", "Mario's", "Lost", "", "Joe's", "Fred's", "Fredbear's"]
    thing = ["Fright", "Terror House", "Diner", "Universe", "WORLD", 'Family Diner', 'One']

    nighttype = ["Custom", "Scary", "ENDLESS", "Open", "", "Animatronic", "Night Stand", "Sexy"]

    name = ""

    async def complete_name_gen(name):

        fnafnames = db.dbget("database/fnaf.json")

        fnafnames.setdefault(name, 0)
        
        fnafnames[name] = fnafnames[name] + 1
        db.dbwrite(fnafnames, "database/fnaf.json")

        name.strip()

        if "Scary Nights at Sebi TV's 2" in name:
            name = f"**{name}**"

        await message.reply(f"{name} ({fnafnames[name]})")

    pick = secrets.choice(g)
    if pick == "FNAF*":
        name += secrets.choice(f) + " "
        name += secrets.choice(n) + " "
        name += secrets.choice(a) + " "
        name += secrets.choice(s) + " "
        if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 7:
            name += secrets.choice(number)
            if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 4:
                name += secrets.choice(t)+ " "
        return await complete_name_gen(name)

    if pick == "UCN*":
        name += secrets.choice(nighttype) + " "
        name += secrets.choice(nighttype) + " "
        name += secrets.choice(n) + " "
        if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 7:
            name += secrets.choice(number)
            if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 4:
                name += secrets.choice(t)+ " "

        return await complete_name_gen(name)

    if pick == "NAME*":
        name += secrets.choice(s) + " "
        if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 7:
            name += secrets.choice(number)
            if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 4:
                name += secrets.choice(t)+ " "

        return await complete_name_gen(name)

    if pick == "SOMEONE'S_SOMETHING*":
        name += secrets.choice(person) + " "
        name += secrets.choice(thing) + " "
        if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 7:
            name += secrets.choice(number)
            if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 4:
                name += secrets.choice(t)+ " "

        return await complete_name_gen(name)
    
    if pick == "RETURN*":
        name += "The Return to "
        name += secrets.choice(s) + " "
        if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 7:
            name += secrets.choice(number)
            if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 4:
                name += secrets.choice(t)+ " "
    
    if pick == "SNAST*":
        name += "Scary Nights at "
        name += secrets.choice(s) + " "
        if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 7:
            name += secrets.choice(number)
            if secrets.choice([0,1,2,3,4,5,6,7,8,9]) > 4:
                name += secrets.choice(t)+ " "

        return await complete_name_gen(name)

