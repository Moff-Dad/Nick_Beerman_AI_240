# wordcount.py
# Nick Beerman
# AI_240 Bellevue College

import sys

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().lower().split()

def count_words(filename):
    words = read_file(filename)
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def print_words(filename):
    counts = count_words(filename)
    for word in sorted(counts):
        print(f'{word} {counts[word]}')

def print_top(filename):
    counts = count_words(filename)
    top = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    for word, count in top[:20]:
        print(f'{word} {count}')

# Command-line interface
def main():
    if len(sys.argv) != 3:
        print('Usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option, filename = sys.argv[1], sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('Unknown option:', option)
        sys.exit(1)

if __name__ == '__main__':
    main()
