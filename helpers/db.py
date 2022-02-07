import json

def dbget(filename):
    with open(filename, 'r') as f:
        datatemp = json.load(f)
        f.close() 
        return datatemp


def dbwrite(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
    f.close()
