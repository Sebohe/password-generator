#!/usr/bin/env python3
import secrets
#import hashlib

rng = secrets.SystemRandom()

randbe = secrets.randbelow

word_dict = {}
S_CHARS = '`~!@#$%^&*()-_+=+?/><,'

with open('eff_large_wordlist.txt','r') as words_list:
    for line in words_list:
        line = line.split("\t")
        word_dict[line[0]] = line[1].strip()

passw = ''
for x in range(rng.randrange(7,10)):
    num = 0    
    while num < 11111:
        num = randbe(66666)
        #Since the words list is a dice we can't have any numbers 0789
        for digit in "0789":
            if digit in str(num):
                num = 0 


    passw = passw + word_dict[str(num)]
   
    rand1 = rng.random()
    rand2 = rng.random()
    #print ('{}, {}'.format(rand1, rand2))
    
    if rand2 < rand1:
        
       passw = passw + rng.choice(S_CHARS)




print (len(passw))
print (passw)
