#!/usr/bin/env python3
import secrets
from os import path

rng = secrets.SystemRandom()
S_CHARS = '`~!@#$%^&*()-_+=+?/><,'

def rollDice(dieQty=5):
    min = 1
    max = 6
    num =''
    for x in range(dieQty):
        n = str(rng.randrange(min, max))
        num = num + n

    return num


if __name__ == '__main__':

    curdir  = path.dirname(path.abspath(__file__))
    word_dict = {}
    with open(curdir + '/eff_large_wordlist.txt','r') as words_list:
        for line in words_list:
            line = line.split("\t")
            word_dict[line[0]] = line[1].strip()

    # Number of passwords to generate
    for x in range(6):
        passw = ''
        sCharPresent = False
        #this determines the word length
        for x in range(rng.randrange(4,10)):
            num = rollDice() 

            rand1 = rng.random()
            rand2 = rng.random()
            if not sCharPresent:
                if rand2 < rand1:
                    sCharPresent = True
                    passw = passw + rng.choice(S_CHARS)

            passw = passw + word_dict[str(num)].title()

        passw = passw + rng.choice(S_CHARS)
        print (len(passw))
        print (passw)
