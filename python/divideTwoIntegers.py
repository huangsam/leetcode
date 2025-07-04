# https://leetcode.com/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Assume we are dealing with an environment that could only store
        # integers within the 32-bit signed integer range
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        # Handle the specific edge case for overflow: MIN_INT / -1
        # This division would result in 2^31, which is > MAX_INT
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        is_negative: bool = (dividend < 0) ^ (divisor < 0)
        result = 0

        remaining, divisor_abs = abs(dividend), abs(divisor)
        while remaining >= divisor_abs:
            current_divisor = divisor_abs
            current_quotient = 1

            # Prevent overflow if current_divisor becomes negative
            while (current_divisor << 1) <= remaining and (current_divisor << 1) > 0:
                current_divisor <<= 1
                current_quotient <<= 1

            # At this point, current_divisor is the largest it can be
            remaining -= current_divisor
            result += current_quotient

        if is_negative:
            # If the result is negative, apply the MIN_INT boundary
            return max(MIN_INT, -result)
        else:
            # If the result is positive, apply the MAX_INT boundary
            return min(MAX_INT, result)
