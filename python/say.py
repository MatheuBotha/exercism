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

magnitude_word = [
    '',
    'thousand',
    'million',
    'billion',
    'trillion',
    'quadrillion',
]

def say(number):
    if number < 0:
        raise ValueError('input out of range')
    if number > 999_999_999_999:
        raise ValueError('input out of range')
    if number == 0:
        return 'zero'
    words = []
    number_string = str(number)
    is_neg = False
    if number_string[0] == '-':
        is_neg = True
        number_string = number_string[1:]
    number_string = number_string[::-1]
    groups = [number_string[i:i+3] for i in range(0, len(number_string), 3)]
    # print(groups)
    for idx, group in enumerate(groups):
        group_in_words = []
        unit = group[0]
        ten = group[1] if len(group) > 1 else None
        hundred = group[2] if len(group) > 2 else None
        # print(unit)
        # print(ten)
        # print(hundred)
        if hundred != '0' and hundred != None:
            group_in_words.append(f'{units[int(hundred)]} hundred')

        if ten != '0' and ten != None:
            # if hundred:
            #     group_in_words.append('and')
            if ten == '1':
                group_in_words.append(f'{teens[int(ten+unit)]}')
            elif ten == '0' and unit == '0':
                pass
            elif unit == '0':
                group_in_words.append(f'{tens[int(ten)]}')
            else:
                group_in_words.append(f'{tens[int(ten)]}-{units[int(unit)]}')
        elif unit != '0':
            group_in_words.append(f'{units[int(unit)]}')

        if f'{hundred}{ten}{unit}' != '000':
            group_in_words.append(magnitude_word[idx])
        words.append(' '.join(group_in_words))
        # print(words)
    if is_neg:
        words.append('negative')

    return ' '.join(words[::-1]).strip()

if __name__ == '__main__':
    examples = [
        0,      # zero
        1,
        14,     # fourteen
        50,     # fifty
        98,     # ninety-eight
        -1,     # negative one
        100,    # one hundred
        1111,   # one thousand      one hundred and eleven
        1000,
        1000000,
        1002345,
        1111111,# one million    one hundred and eleven thousand    one hundred and eleven
    ]


    for e in examples:
        print(e)
        print(say(e))
        print()
