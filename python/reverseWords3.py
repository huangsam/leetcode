# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse characters in each word while preserving word order.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        string = ""
        for word in s.split():
            string += word[::-1] + " "
        return string.strip()
