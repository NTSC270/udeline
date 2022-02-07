from dataclasses import replace
import random
import re
import math
import commands

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

async def run_command(discord, message, args, client, opt):
    args.pop(0)
    if len(args) < 1:
        await message.reply("i need some text to do that")
        return await commands.run_command("help", discord, message, ["u>help", "doodlebob"], client, [])
    words = args
    doodleisms = ['hoy', 'mi', 'me', 'fro', 'yay', 'mey', 'mee', 'mea', 'hoy', 'noy']
    for i in range(len(words)):
        replacement = []
        for j in range(syllable_count(words[i])):
            random.seed(words[i])
            random.shuffle(doodleisms)
            replacement.append(doodleisms[math.floor(random.random() * len(doodleisms))])
        replacement = "".join(replacement)
        words[i] = re.sub("[a-zA-ZşŞÇçÖöüÜıIiİĞğ]+",replacement, words[i])
    await message.reply(" ".join(words))
