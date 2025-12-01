#!/usr/bin/env python3

with open('input.txt') as f:
    listofpairs = [ (line[0], line[1:].strip()) for line in f ]

print(listofpairs)

dial = 50
count = 0

for combo in listofpairs:
    if combo[0] == 'R':
        dial += int(combo[1]) % 100
    elif combo[0] == 'L':
        dial -= int(combo[1]) % 100

    if dial < 0:
        dial += 100
    elif dial > 99:
        dial -= 100
    

    if dial == 0: 
        count += 1
    print(f'turn the dial {combo}, reaching {dial}, zerocount: {count}')
    
        
