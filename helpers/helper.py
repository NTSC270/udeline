import json

prefixes = {"udeline": ["u,", "u>"], "udevline": ["u,,", "u>>"]}
udel_emoji = {"udeline": "<:udeline:937436511899627620>", "udevline": "<:udevline:940528057830211584>"}

class prefix:
    def check(msg, client):
        checked = 0
        for x in prefixes[client.user.name]:
            if msg.startswith(x):
                return [True, len(x), x]
                checked = 1
        if checked == 0:
            return [False, 0, ""]