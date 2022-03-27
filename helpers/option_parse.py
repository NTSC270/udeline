import re

options = []

def parse_options(string):
    options = re.split("-", string)
    newopts = []
    for x in options:
        x.strip()
        newopts.append(re.sub(" +.+", "", x))
    return newopts