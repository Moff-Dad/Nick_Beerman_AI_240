# string1.py
# Nick Beerman
# AI_240 Bellevue College

def donuts(count):
    if count >= 10:
        return 'Number of donuts: many'
    return f'Number of donuts: {count}'

def both_ends(s):
    if len(s) < 2:
        return ''
    return s[:2] + s[-2:]

def fix_start(s):
    first = s[0]
    return first + s[1:].replace(first, '*')

def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]
