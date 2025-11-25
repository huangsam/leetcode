#!/bin/bash
set -euo pipefail

# Match for LeetCode URLs in all solution folders

: << 'eof'
We use grep to collect LeetCode URLs from each solution folder and show
which language(s) have solutions for each URL.

Here are the grep options explained:
    -o = Print matching parts of matching line
    -a = Process binary file as text
    -h = Suppress prefixing of filename
    -r = Read all files under each directory

We optimize by using awk to track which languages have each URL in a single pass.
eof

# Use awk to process all URLs efficiently in one pass
{
    grep -o -a -h -r 'https://leetcode.com.*' java 2>/dev/null | awk '{print $0, "Java"}'
    grep -o -a -h -r 'https://leetcode.com.*' python 2>/dev/null | awk '{print $0, "Python"}'
} | awk '
{
    url = $1
    lang = $2
    if (lang == "Java") has_java[url] = 1
    if (lang == "Python") has_python[url] = 1
    urls[url] = 1
}
END {
    for (url in urls) {
        if (has_java[url] && has_python[url]) {
            print url " [Java, Python]"
        } else if (has_java[url]) {
            print url " [Java]"
        } else if (has_python[url]) {
            print url " [Python]"
        }
    }
}' | sort
