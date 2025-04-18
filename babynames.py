#!/usr/bin/env python3
# babynames.py
# Nick Beerman
# AI_240 Bellevue College


import sys
import re

def extract_names(filename):
    with open(filename, 'r') as f:
        text = f.read()

    # Extract the year
    year_match = re.search(r'Popularity\sin\s(\d{4})', text)
    if not year_match:
        sys.stderr.write("Couldn't find the year!\n")
        sys.exit(1)
    year = year_match.group(1)

    # Extract name/rank tuples
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    name_rank_dict = {}

    for rank, boy_name, girl_name in tuples:
        if boy_name not in name_rank_dict:
            name_rank_dict[boy_name] = rank
        if girl_name not in name_rank_dict:
            name_rank_dict[girl_name] = rank

    # Create a sorted list of "name rank" strings
    name_rank_list = [f'{name} {name_rank_dict[name]}' for name in sorted(name_rank_dict.keys())]

    # Final result list
    return [year] + name_rank_list

def main():
    # Command line args
    args = sys.argv[1:]
    if not args:
        print('Usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Check for summary flag
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        args = args[1:]

    for filename in args:
        name_data = extract_names(filename)
        text = '\n'.join(name_data) + '\n'

        if summary:
            with open(filename + '.summary', 'w') as out_file:
                out_file.write(text)
        else:
            print(text)

if __name__ == '__main__':
    main()
