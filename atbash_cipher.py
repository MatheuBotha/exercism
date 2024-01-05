from string import ascii_lowercase
reversed_ascii_lowercase = ascii_lowercase[::-1]
codex = dict(zip(ascii_lowercase, reversed_ascii_lowercase))

def encode(plain_text, group_size=5):
    sanitized_text = ''.join([codex.get(c, c) for c in plain_text.lower() if c.isalnum()])
    return ' '.join([sanitized_text[i:i+group_size] for i in range(0, len(sanitized_text), group_size)])

def decode(plain_text):
    return ''.join([codex.get(c, c) for c in plain_text.lower() if c != ' '])

if __name__ == '__main__':
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