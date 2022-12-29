#! /usr/bin/env python3

#
# modextract.py
# Version: 0.1.0
# Date: 2022-12-29
#
# Extracts mod IDs from an Arma 3 HTML file and writes them to
# the standard output.
#

import re
import sys

#
# Globals
#

# RE for extracting IDs
re_id = re.compile('^\s*<a\s+href="http[s]?://steamcommunity.com/sharedfiles/filedetails/\?id=(\d+)"')

# List of extracted IDs
ids = []

#
# Functions
#

# Print to STDERR.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Formats the mod ID to be written to the output.
def format_id(id):
    return f"@{id};"

#
# Main
#

# Check if the input file is specified
if len(sys.argv) < 2:
    sys.exit('Missing file name')

# Determine file name from the command line args
file_name = sys.argv[1]

# Read the file and extract IDs
with open(file_name) as file:
    for line in file:
        match = re_id.match(line)
        if match:
            id = match.group(1)
            ids.append(id)

# Print the results
if len(ids) > 0:
    eprint(f'{len(ids)} IDs found:')
    for id in ids:
        print(format_id(id), end='')
else:
    eprint(f"No IDs found in file '{file_name}'.")
