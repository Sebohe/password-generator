#!/usr/bin/env python3
import secrets
#import hashlib

rng = secrets.SystemRandom()

word_dict = {}
S_CHARS = '`~!@#$%^&*()-_+=+?/><,'

with open('eff_large_wordlist.txt','r') as words_list:
    for line in words_list:
        line = line.split("\t")
        word_dict[line[0]] = line[1].strip()


passw = ''

#this determines the word length
for x in range(6):
    passw = ''
    for x in range(rng.randrange(4,10)):
        goodNumber = False
        while not goodNumber:
            num = rng.randrange(11111,66666)
            #Since the words list is a dice we can't have any numbers 0789
            goodNumber = True
            for digit in "0789":
                if digit in str(num):
                    goodNumber = False

        newWord = word_dict[str(num)]
        passw = passw + newWord.title()

    passw = passw + rng.choice(S_CHARS)
    print (len(passw))
    print (passw)
