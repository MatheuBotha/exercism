teens = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tens = {
    0: '',
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

units = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

def say(number):
    words = []
    number_string = str(number)
    is_neg = False
    if number_string[0] == '-':
        is_neg = True
        number_string = number_string[1:]
    number_string = number_string[::-1]
    groups = [number_string[i:i+3] for i in range(0, len(number_string), 3)]
    print(number)
    print(number_string)
    print(groups)

    for group in groups:
        group_in_words = []
        unit = group[0]
        ten = group[1] if len(group) > 1 else None
        hundred = group[2] if len(group) > 2 else None

        if hundred:
            group_in_words.append(f'{units[int(hundred)]} hundred and')
        if ten:
            if ten == '1':
                group_in_words.append(f'{teens[int(ten+unit)]}')
            else:
                group_in_words.append(f'{tens[int(ten)]}-{units[int(unit)]}')
        else:
            group_in_words.append(f'{units[int(unit)]}')
        print(' '.join(group_in_words))

    return ''.join(words)

if __name__ == '__main__':
    examples = [
        0,      # zero
        14,     # fourteen
        50,     # fifty
        98,     # ninety-eight
        -1,     # negative one
        100,    # one hundred
        1111,   # one thousand      one hundred and eleven
        1111111,# one million    one hundred and eleven thousand    one hundred and eleven
    ]


    for e in examples:
        print(say(e))
