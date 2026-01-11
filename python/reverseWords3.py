# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse characters in each word while preserving word order.

        Split the string into words, reverse the characters in each word using string slicing, then join the reversed words with spaces.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        string = ""
        for word in s.split():
            string += word[::-1] + " "
        return string.strip()
