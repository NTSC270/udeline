import json

prefixes = {"udeline": ["u>", "udel>"], "udevline": ["u>>", "udel>>"]}
class prefix:
    def check(msg, client):
        for x in prefixes[client.user.name]:
            if msg.startswith(x):
                return [True, len(x), x]
            else:
                return [False, 0, ""]