# https://leetcode.com/problems/greatest-common-divisor-of-strings/

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Complexity:
        - Time: O(n + m)
        - Space: O(n + m)
        """
        # Step 1: Necessary Condition Check
        # If a common divisor exists, str1 + str2 must equal str2 + str1.
        if str1 + str2 != str2 + str1:
            return ""  # No common divisor pattern found

        # Step 2: Determine the length of the Greatest Common Divisor
        # The length of the GCD string is the GCD of the lengths of the two strings.
        len1 = len(str1)
        len2 = len(str2)

        # Use the Euclidean algorithm (via math.gcd) to find the length
        gcd_length = math.gcd(len1, len2)

        # Step 3: Return the prefix of str1 with the calculated GCD length
        # Since we passed Step 1, this prefix is guaranteed to be the GCD string.
        return str1[0:gcd_length]
