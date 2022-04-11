import db

from PyDictionary import PyDictionary 
import difflib
dictionary=PyDictionary() 

async def run_command(discord, message, args, client, opt): 
    args.pop(0)
    output = []

    activity = db.dbget("misc/emoji_cldr.json")

    for x in list(args):
        output.append(x) 
        for key in activity:
            syns = []
            try:
                syns = dictionary.synonym(x, disable_errors=True)
            except:
                pass

            if x in key or key in x[0:6] or key[0:6] in syns:
                matches = difflib.get_close_matches(x, activity.keys())
                temp = ""
                if(len(matches) > 0):
                    temp = activity[matches[0]]
                else:
                    temp = activity[key]
                output.append(temp)
                break
        
    return await message.reply(" ".join(output))
