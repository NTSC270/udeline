
prefixes = {"udeline": ["u-", "u,", "u>", "[]"], "ndeline": ["u=", "u,,", "u>>", "{}"]}
udel_emoji = {"udeline": "<:udeline:962373693579857971> ", "ndeline": "<:ndeline:962373693370155038>"}

class prefix:
    def check(msg, client):
        checked = 0
        for x in prefixes[client.user.name]:
            if msg.startswith(x):
                return [True, len(x), x]
                checked = 1
        if checked == 0:
            return [False, 0, ""]

def time_decorate(timestamp, trim):
    if trim == True:
        timestamp = timestamp.split(".")[0]
    parts = timestamp.split(":")
    return str(parts[0]+"h"+":"+parts[1]+"m"+":"+parts[2]+"s")

def badge_parse(member):
    badges = member.public_flags
    output = []

    if badges.bug_hunter:
        output.append("bug_hunter")
    if badges.bug_hunter_level_2:
        output.append("bug_hunter_2")
    if badges.early_supporter:
        output.append("early_supporter")
    if badges.early_verified_bot_developer:
        output.append("verified_bot_dev")
    if badges.hypesquad_balance:
        output.append("balance")
    if badges.hypesquad_bravery:
        output.append("bravery")
    if badges.hypesquad_brilliance:
        output.append("brilliance")
    if badges.partner:
        output.append("partner")
    if badges.staff:
        output.append("staff")
    if badges.verified_bot:
        output.append("verified_bot")

    return output

def ansi(color, bold):
    bold = 0
    colors = {
        "grey": "[b;30m",
        "red": "[b;31m",
        "green": "[b;32m",
        "yellow": "[b;33m",
        "blue": "[b;34m",
        "pink": "[b;35m",
        "aqua": "[b;36m",
        "white": "[b;37m",
        "dark_fill": "[b;40m",
        "red_fill": "[b;41m",
        "grey_fill": "[b;42m",
        "washed_fill": "[b;44m",
        "discord_fill": "[b;45m",
        "whitefill": "[b;47m",
        "clear": "[0;0m",
        "underline": "[4;31m"
    }

    return colors[color.strip()].replace("b", bold)