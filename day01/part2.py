#!/usr/bin/env python3

with open('input.txt') as f:
    listofpairs = [ (line[0], line[1:].strip()) for line in f ]

dial = 50
count = 0

# count all times we click past 0: 

for combo in listofpairs:
    nulldurchgaenge = abs(int(combo[1])) // 100
    hit = 0

    if combo[0] == 'R':
        dial += int(combo[1]) % 100
        if dial > 100:
            nulldurchgaenge += 1
        if dial >= 100:
            dial -= 100

    if combo[0] == 'L':
        if dial == 0:
            dial = 100
        dial -= int(combo[1]) % 100
        if dial < 0:
            dial += 100
            nulldurchgaenge += 1

    if dial == 0:
        hit = 1

    count = count + nulldurchgaenge + hit

    print(f'turn the dial {combo},\t reaching {dial}\t nulldurchgänge {nulldurchgaenge} + hit {hit} = {count}')
    
print(f'Zero Clicks: {count}')

