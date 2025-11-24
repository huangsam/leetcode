#!/bin/bash
set -euo pipefail

# Match for LeetCode URLs in all solution folders

: << 'eof'
We use grep to collect LeetCode URLs from each solution folder.

Here are the grep options explained:
    -o = Print matching parts of matching line
    -a = Process binary file as text
    -h = Supress prefixing of filename
    -r = Read all files under each directory

We then apply sort and uniq to enforce unique links. The sort is needed
because uniq only detects duplicates on adjacent lines.
eof

grep -o -a -h -r 'https://leetcode.com.*' {java,python} | sort | uniq
