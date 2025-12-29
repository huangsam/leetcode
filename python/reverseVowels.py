# https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        This illustrates the two-pointer technique.
        It only uses O(n) space without auxilliary structures.
        If we did it with a one-pass approach, we would have needed extra
        space to store the vowels and their indices for swapping later on.
        """
        # 1. Convert to list because strings are immutable
        chars = list(s)
        vowels = set("aeiouAEIOU")

        left, right = 0, len(chars) - 1

        while left < right:
            # Move left pointer until it hits a vowel
            while left < right and chars[left] not in vowels:
                left += 1
            # Move right pointer until it hits a vowel
            while left < right and chars[right] not in vowels:
                right -= 1

            # Swap the vowels
            chars[left], chars[right] = chars[right], chars[left]

            # Move both pointers inward to continue
            left += 1
            right -= 1

        return "".join(chars)
