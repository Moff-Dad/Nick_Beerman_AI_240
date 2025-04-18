#!/usr/bin/env python3
# logpuzzle.py
# Nick Beerman
# AI_240 Bellevue College

import os
import re
import sys
import urllib.request

def read_urls(filename):
    """Parses the given logfile and returns a list of puzzle URLs."""
    # Extract server hostname from filename (e.g., place_code.google.com → code.google.com)
    host_match = re.search(r'_(\S+)', filename)
    if not host_match:
        sys.stderr.write("Error: Filename must contain a server hostname after underscore.\n")
        sys.exit(1)
    hostname = host_match.group(1)

    # Read log file and extract puzzle paths
    with open(filename, 'r') as f:
        text = f.read()

    # Find all /...puzzle... file paths
    matches = re.findall(r'GET (\S*puzzle\S*) HTTP', text)
    urls = set(f'http://{hostname}{path}' for path in matches)

    # Use custom sort key if filename has advanced format (Part C)
    def sort_key(url):
        match = re.search(r'-\w+-(\w+)\.jpg', url)
        return match.group(1) if match else url

    return sorted(urls, key=sort_key)

def download_images(img_urls, dest_dir):
    """Given the URLs, downloads each image into the given directory and creates an index.html file to display them."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Create index.html content
    index_path = os.path.join(dest_dir, 'index.html')
    with open(index_path, 'w') as index_file:
        index_file.write('<html>\n<body>\n')

        for i, url in enumerate(img_urls):
            local_name = f'img{i}.jpg'
            local_path = os.path.join(dest_dir, local_name)

            print(f'Downloading {url} as {local_name}...')
            urllib.request.urlretrieve(url, local_path)

            index_file.write(f'<img src="{local_name}">')

        index_file.write('\n</body>\n</html>\n')

def main():
    args = sys.argv[1:]
    if not args:
        print('usage: [--todir dir] logfile')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    # Remaining arg is the log filename
    logfile = args[0]
    img_urls = read_urls(logfile)

    if todir:
        download_images(img_urls, todir)
    else:
        # Just print
