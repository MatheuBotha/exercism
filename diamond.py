from typing import List
from pprint import pprint

def rows(letter):
    diamond = []
    radius = ord(letter)-ord('A')+1
    for idx in range(radius):
        current_char = chr(ord('A')+idx)
        row = f"{current_char}".rjust(radius-idx, ' ')
        if idx != 0:
            row += f"{current_char}".rjust(((2*(idx-1))+1)+1)
        row += ''.join([' ' for _ in range(radius-idx-1)])
        diamond.append(row)
    diamond.extend(diamond[:-1][::-1])
    return diamond

def better_rows(letter: str) -> List[str]:
    letters = [chr(k) for k in range(ord('A'), ord(letter) + 1)]
    print(letters)
    alphabet = letters[:-1] + letters[::-1]
    print(alphabet)
    diamond_line = letters[::-1] + letters[1:]
    print(diamond_line)
    return [''.join(x if x == y else ' ' for y in diamond_line) for x in alphabet]

pprint(rows('E'))
pprint(better_rows('E'))