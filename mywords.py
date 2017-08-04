#!/usr/bin/env python3
import secrets
import hashlib


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
        num = secrets.randbelow(66666)
        for digit in "0789":
            if digit in str(num):
                num = 0 


    text = text+word_dict[str(num)]
   
    rand1 = secrets.randbelow(99999999999999999)
    rand2 = secrets.randbelow(99999999999999999)
    print ('{}, {}'.format(rand1, rand2))
    if rand2 < rand1:
        
       text = text+SPECIAL_CHARACTERS[secrets.randbelow(len(SPECIAL_CHARACTERS))]



print (len(text))
print (text)
