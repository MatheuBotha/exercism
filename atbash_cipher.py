from pprint import pprint
from string import ascii_lowercase
reversed_ascii_lowercase = ascii_lowercase[::-1]
codex = dict(zip(ascii_lowercase, reversed_ascii_lowercase))

def encode_character(c):
    if c in codex:
        return codex[c]
    elif c.isdigit():
        return c
    return ''

def encode(plain_text):
    result = []
    encoded_character_count = 0
    for c in plain_text.lower():
        encoded_character = encode_character(c)
        if encoded_character != '':
            result.append(encode_character(c))
            encoded_character_count += 1
            if encoded_character_count%5 == 0 and encoded_character_count != 0:
                result.append(' ')
    return ''.join(result).strip()

def decode(plain_text):
    return ''.join([encode_character(c) for c in plain_text.lower()])

if __name__ == '__main__':
    pprint(codex)

    examples = [
        'test',
        'x123 yes',
        'gvhg',
        'gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt',
        'OMG',
        'mindblowingly',
        'Testing,1 2 3, testing.'
    ]

    for x in examples:
        a = encode(x)
        b = decode(a)
        print(x)
        print(a)
        print(b)
        print()