# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Time: O(n)
        Space: O(n)
        """
        reversed_words = []

        # Process all tokens in reverse order
        for rev_word in s.strip()[::-1].split():
            # Each token can be reversed to get the word
            reversed_words.append(rev_word[::-1])

        # Join all words as a single string
        return " ".join(reversed_words)
