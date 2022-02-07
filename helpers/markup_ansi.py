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
    "clear": "[0;0m"
}

def getc(color, bold):
    return colors[color.strip()].replace("b", bold)