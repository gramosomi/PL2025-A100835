import sys
import re

def tokenize(code):
    token_specification = [
        ('KEYWORD', r'select|where|limit', re.IGNORECASE),
        ('VAR', r'\?[a-zA-Z_][a-zA-Z_0-9]*'),
        ('URI', r'dbo:[a-zA-Z_][a-zA-Z_0-9]*|foaf:[a-zA-Z_][a-zA-Z_0-9]*'),
        ('STRING', r'".*?"(@[a-zA-Z]+)?'),
        ('NUM', r'\d+'),
        ('SYMB', r'[{}.]'),
        ('WHITESPACE', r'\s+'),
        ('MISSMATCH', r'.'),
    ]

    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex, *_ in token_specification)
    tokens = []
    line_num = 1

    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group(kind)
        
        if kind == 'WHITESPACE':
            line_num += value.count('\n')
        elif kind == 'UNKMISSMATCHNOWN':   
            pass
        elif kind == 'NUM':
            tokens.append((value, 'NUMBER'))
        elif kind == 'STRING':
            tokens.append((value, 'STRING'))
        elif kind == 'VAR':
            tokens.append((value, 'VAR'))
        elif kind == 'URI':
            tokens.append((value, 'URI'))
        elif kind == 'KEYWORD':
            tokens.append((value, 'KEYWORD'))
        elif kind == 'SYMB':
            tokens.append((value, 'SYMBOL'))
    
    return tokens

message = sys.stdin.read()
print(tokenize(message))
    


            