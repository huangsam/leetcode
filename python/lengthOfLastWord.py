# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Keep iterating until right_at sees a character.
        Keep iterating until left_at does not see a character.
        Note that first and last characters must be checked.
        """
        right_at = len(s) - 1
        while right_at >= 0:
            if s[right_at].isalpha():
                break
            right_at -= 1

        left_at = right_at
        while left_at >= 0:
            if not s[left_at].isalpha():
                break
            left_at -= 1

        return right_at - left_at
