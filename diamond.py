from pprint import pprint

def rows(letter):
    diamond = []
    radius = ord(letter)-ord('A')
    print(radius)
    if radius == 0:
        return ['A']
    
    for idx in range(radius+1):
        print(idx)
        s = f'{chr(ord(letter)-idx)}'
        js = s.rjust(idx+1, ' ')
        print(js)
        diamond.append(js)
    return diamond

print(rows('A'))
print(rows('B'))
print(rows('C'))
