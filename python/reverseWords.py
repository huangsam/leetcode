# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = []
        for rev_word in s.strip()[::-1].split():
            reversed_words.append(rev_word[::-1])
        return " ".join(reversed_words)
