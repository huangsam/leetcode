# https://leetcode.com/problems/reverse-string/


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Reverse the input list of characters in place.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        for i in range(len(s) // 2):
            r = len(s) - i - 1
            s[i], s[r] = s[r], s[i]
