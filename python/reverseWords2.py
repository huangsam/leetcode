# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        string = ""
        for word in s.split():
            string += word[::-1] + " "
        return string.strip()
