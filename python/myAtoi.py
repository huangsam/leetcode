# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        """Convert a string to a 32-bit signed integer."""
        n = len(s)
        i = 0

        # Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # Check sign
        sign = 1
        if i < n and s[i] in ("+", "-"):
            sign = -1 if s[i] == "-" else 1
            i += 1

        # Read digits
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # Clamping
        min_val, max_val = -2**31, 2**31 - 1
        if num < min_val:
            return min_val
        if num > max_val:
            return max_val

        return num
