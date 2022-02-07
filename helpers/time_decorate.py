

def letters(timestamp, trim):
    if trim == True:
        timestamp = timestamp.split(".")[0]
    parts = timestamp.split(":")
    return str(parts[0]+"h"+":"+parts[1]+"m"+":"+parts[2]+"s")