#!/usr/bin/env python3
from secrets import randbelow
from secerets import SystemRandom
#import hashlib


word_dict = {}
SPECIAL_CHARACTERS = '`~!@#$%^&*()-_+=+?/><,'

with open('eff_large_wordlist.txt','r') as words_list:
    for line in words_list:
        line = line.split("\t")
        word_dict[line[0]] = line[1].strip()

text = ''
for x in range(7):
    num = 0    
    while num < 11111:
        num = randbelow(66666)
        #Since the words list is a dice we can't have any numbers 0789
        for digit in "0789":
            if digit in str(num):
                num = 0 


    passw = passw+word_dict[str(num)]
   
    rand1 = SystemRandom 
    rand2 = SystemRandom
    #print ('{}, {}'.format(rand1, rand2))
    
    if rand2 < rand1:
        
       passw = passw + SPECIAL_CHARACTERS[randbelow(len(SPECIAL_CHARACTERS))]



print (len(text))
print (text)
