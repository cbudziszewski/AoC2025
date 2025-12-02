#!/usr/bin/env python3

with open('input.txt') as f:
    code = [ pair.split('-') for pair in f.readline().strip().split(',')]

def is_valid(id):
    for n in range(1, len(id)//2 + 1):
        if len(id) % n == 0:
            parts = [ id[i:i+n] for i in range(0, len(id), n)] 
#            print(f'{id} parts {parts} {set(parts)}')
            if len(set(parts)) == 1:
                return False
    return True


summe = 0
for a, b in code:
    d = int(b)-int(a)
    invalid_ids = [id for id in range(int(a), int(b)+1) if not is_valid(str(id))]
    print(invalid_ids)
    summe += sum(invalid_ids)

# 55647141923
print(f'Summe: {summe}')
