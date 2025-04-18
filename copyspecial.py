#!/usr/bin/env python3
# copyspecial.py
# Nick Beerman
# AI_240 Bellevue College

import sys
import os
import re
import shutil
import subprocess

def get_special_paths(dir):
    """Return list of absolute paths to special files in the given dir."""
    special_files = []
    for filename in os.listdir(dir):
        if re.search(r'__\w+__', filename):
            full_path = os.path.abspath(os.path.join(dir, filename))
            special_files.append(full_path)
    return special_files

def copy_to(paths, dest_dir):
    """Copy special files in 'paths' to 'dest_dir' (create if doesn't exist)."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for path in paths:
        shutil.copy(path, dest_dir)

def zip_to(paths, zipfile):
    """Zip all files in 'paths' into the zipfile."""
    cmd = ['zip', '-j', zipfile] + paths
    print("Command I'm going to do:", ' '.join(cmd))
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)

def main():
    # Command line args
    args = sys.argv[1:]
    if not args:
        print("Usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    todir = ''
    tozip = ''
    
    # Handle optional flags
    while args and args[0].startswith('--'):
        if args[0] == '--todir':
            todir = args[1]
            del args[0:2]
        elif args[0] == '--tozip':
            tozip = args[1]
            del args[0:2]
        else:
            print('Unknown flag:', args[0])
            sys.exit(1)

    if not args:
        print("Error: Must specify at least one directory.")
        sys.exit(1)

    # Get all special files from all input directories
    special_paths = []
    for dir in args:
        special_paths.extend(get_special_paths(dir))

    # Action based on flags
    if todir:
        copy_to(special_paths, todir)
    elif tozip:
        zip_to(special_paths, tozip)
    else:
        print('\n'.join(special_paths))

if __name__ == '__main__':
    main()
