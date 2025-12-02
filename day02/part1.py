#!/usr/bin/env python3

with open('input.txt') as f:
    code = [ pair.split('-') for pair in f.readline().strip().split(',')]

def is_valid(id):
    l = len(id)
    # odd number of digits is always valid
    if l % 2 == 1:
        return True

    a = id[:l//2]
    b = id[l//2:]

    return not a == b

summe = 0
for a, b in code:
    d = int(b)-int(a)
    invalid_ids = [id for id in range(int(a), int(b)+1) if not is_valid(str(id))]
    summe += sum(invalid_ids)

# 44854383294
print(f'Summe: {summe}')
