# list1.py
# Nick Beerman
# AI_240 Bellevue College

def match_ends(words):
    return sum(1 for word in words if len(word) >= 2 and word[0] == word[-1])

def front_x(words):
    x_list = sorted([w for w in words if w.startswith('x')])
    rest = sorted([w for w in words if not w.startswith('x')])
    return x_list + rest

def sort_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])
