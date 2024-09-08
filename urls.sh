#!/bin/bash

# Match for LeetCode URLs in all solution folders
grep -o -a -h -r "https://leetcode.com.*" {java,python}
