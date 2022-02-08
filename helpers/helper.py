import json

prefixes = {"udeline": ["u>", "udel>"], "udevline": ["u>>", "udel>>"]}
udel_emoji = {"udeline": "<:udeline:937436511899627620>", "udevline": "<:udevline:940528057830211584>"}

class prefix:
    def check(msg, client):
        for x in prefixes[client.user.name]:
            if msg.startswith(x):
                return [True, len(x), x]
            else:
                return [False, 0, ""]