prefix = ['udel>', 'u>']

def has_pfix(msg):
    for x in prefix:
        if msg.startswith(x):
            return True

def pfix_sw(msg):
    for x in prefix:
        if msg.startswith(x):
            return len(x)
def used_pfix(msg):
    for x in prefix:
        if msg.startswith(x):
            return x