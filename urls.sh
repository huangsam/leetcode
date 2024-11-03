#!/bin/bash

# Match for LeetCode URLs in all solution folders

<<'eof'
We use grep to find all LeetCode URLs in the various folders.

Here are the grep options explained:
    -o = Print matching parts of matching line
    -a = Process binary file as text
    -h = Supress prefixing of filename
    -r = Read all files under each directory

We then apply sort and uniq to enforce unique links. That is because
uniq only detects duplicates on adjacent lines.
eof

grep -o -a -h -r "https://leetcode.com.*" {java,python} | sort | uniq
