# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determine if a string is a valid palindrome.

        Use a two-pointer approach: start one pointer at the beginning and one at the
        end. Move them towards the center, skipping non-alphanumeric characters, and
        compare the alphanumeric characters case-insensitively.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
