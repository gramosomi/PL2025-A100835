import sys 
import re 

def artist_alphabetical_order():
    composers = []
    for line in sys.stdin:
        composer = re.search(r'\d{4};[^;]*;([^;]*);', line)
        if composer:
            composers.append(composer.group(1))
    composers.sort()
    print(composers)


def music_by_period():
    periods = {}
    for line in sys.stdin:
        period = re.search(r'\d{4};([^;]*);', line)
        if period:
            if period.group(1) in periods:
                periods[period.group(1)] += 1
            else:
                periods[period.group(1)] = 1
    print(periods)

def dictionary_from_period():
    dictionary = {}
    for linha in sys.stdin:
        m = re.search(r'(((\d{4};)([^;]*);.*$)|^([^;\n]*);[^ \w])', linha)
        if m:
            if m[2]:
                name = m.group(5)
            else:
                category = m.group(4)
                if category not in dictionary:
                    dictionary[category] = []
                dictionary[category].append(name)

    for key, value in dictionary.items():
        value.sort()
        print(key, ":", value)
    


#artist_alphabetical_order()
#music_by_period()
#dictionary_from_period()