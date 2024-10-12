# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Collect all letters and numbers, converting them to lowercase as we go.
        Then see if the reverse iteration is the same as the forward iteration.
        """
        char_list = [ch.lower() for ch in s if ch.isalnum()]
        return all(char_list[i] == char_list[len(char_list) - i - 1] for i in range(len(char_list)))
