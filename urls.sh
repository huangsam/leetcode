#!/bin/bash

# Match for LeetCode URLs in all solution folders

# Here are the command options explained:
#   -o = Print matching parts of matching line
#   -a = Process binary file as text
#   -h = Supress prefixing of filename
#   -r = Read all files under each directory
grep -o -a -h -r "https://leetcode.com.*" {java,python}
