import random
import helpers.markup_ansi

async def run_command(discord, message, args, client, opt):

    if(len(args) > 1):
        seed_fnaf = ""
        args.pop(0)
        for x in args:
            seed_fnaf+=x+" "
        random.seed(seed_fnaf.strip())
        print(seed_fnaf)

    g = ["FNAF*", "UCN*", "NAME*", "SOMEONE'S_SOMETHING*", "RETURN*"]

    f = ["Five", "Scary", "Those", "Nine", "One", "Some", "1 Minute", "Horror"]
    n = ["Nights", "Nights", "Days", "Minutes", "Weeks"]
    a = ["in", "at", "with"]
    s = ["Freddy's", "Sebi TV's", "Rachael's", "CoolingTool's", "Baldi's", "Chuck E. Cheese's", "Scaries", "Scraps", "Mr. Hippo's", "Impostor", "Goomie's"]
    
    number = ["Reignited", "2", "REMASTERED", "REMADE", "3", "4", "5", "Again", "FAN MADE"]
    t = [": Sebi's Wrath", ": The trilogy", ": Rewired", " (CANCELLED)"]

    person = ["Sebi TV's", "Goodwill's", "Freddy's", "Mario's", "Lost", "", "Joe's", "Fred's", "Fredbear's"]
    thing = ["Fright", "Terror House", "Diner", "Universe", "WORLD", 'Family Diner', 'One']

    nighttype = ["Custom", "Scary", "ENDLESS", "Open", "", "Animatronic", "Night Stand", "Sexy"]

    name = ""
    joiner = " "
    poscol = ["red", "green", "yellow", "blue", "white", "dark_fill"]

    pick = round(random.random() * len(g)) % len(g)
    if pick == 0:
        pick = round(random.random() * len(f))
        name += f[pick % len(f)] + joiner
        pick = round(random.random() * len(n))
        name += n[pick % len(n)] + joiner
        pick = round(random.random() * len(a))
        name += a[pick % len(a)] + joiner
        pick = round(random.random() * len(s))
        name += s[pick % len(s)] + joiner
        if random.random() > 0.8:
            pick = round(random.random() * len(number))
            name += number[pick % len(number)] + joiner

    if pick == 1:
        pick = round(random.random() * len(nighttype))
        name += nighttype[pick % len(nighttype)] + joiner
        pick = round(random.random() * len(nighttype))
        name += nighttype[pick % len(nighttype)] + joiner
        pick = round(random.random() * len(n))
        name += n[pick % len(n)].replace("s", "") + joiner
        if random.random() > 0.8:
            pick = round(random.random() * len(number))
            name += number[pick % len(number)] + joiner

    if pick == 2:
        pick = round(random.random() * len(s))
        name += s[pick % len(s)] + joiner
        if random.random() > 0.8:
            pick = round(random.random() * len(number))
            name += number[pick % len(number)] + joiner

    if pick == 3:
        pick = round(random.random() * len(s))
        name += person[pick % len(person)] + joiner
        pick = round(random.random() * len(thing))
        name += thing[pick % len(thing)] + joiner
        if random.random() > 0.8:
            pick = round(random.random() * len(number))
            name += number[pick % len(number)] + joiner
    
    if pick == 4:
        name += "The"+joiner+ "Return"+joiner+ "to"+joiner
        pick = round(random.random() * len(s))
        name += s[pick % len(s)] + joiner
        if random.random() > 0.8:
            pick = round(random.random() * len(number))
            name += number[pick % len(number)] + joiner

    await message.reply(name)

    #await message.channel.send("```ansi\n"+helpers.markup_ansi.getc("clear", "0")+helpers.markup_ansi.getc(poscol[round(random.random() * len(poscol)) % len(poscol)], "1")+name+"```")
