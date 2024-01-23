from string import ascii_lowercase
codex = dict(zip(ascii_lowercase, ascii_lowercase[::-1]))

def cycle_characters(text):
    return (codex.get(c, c) for c in text)

def sanitize_text(text):
    return (c for c in text.lower() if c.isalnum())

def group_characters(text):
    batch = []
    for c in text:
        batch.append(c)
        if len(batch) == 5:
            yield ''.join(batch)
            batch = []
    if batch:
        yield ''.join(batch)
        
def curry(encoding_type):
    def func(text):
        match encoding_type:
            case 'ENCODE':
                return ' '.join(group_characters(cycle_characters(sanitize_text(text))))
            case 'DECODE':
                return ''.join(cycle_characters(sanitize_text(text)))
    return func

# def encode(plain_text, group_size=5):
#     sanitized_text = ''.join(codex.get(c, c) for c in plain_text.lower() if c.isalnum())
#     return ' '.join(sanitized_text[i:i+group_size] for i in range(0, len(sanitized_text), group_size))

# def decode(plain_text):
#     return ''.join(codex.get(c, c) for c in plain_text.lower() if c != ' ')

encode = curry('ENCODE')
decode = curry('DECODE')

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

    # a = curry('ENCODE')
    # print(a('apples'))