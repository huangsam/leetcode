# https://leetcode.com/problems/fizz-buzz/

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Return a string array where multiples of 3 are "Fizz", 5 are "Buzz", and both are "FizzBuzz".

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        result = []
        for i in range(1, n + 1):
            # Check divisibility by 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            # Check divisibility by 3 or 5
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            # If not divisible by 3 or 5, append the number as a string
            else:
                result.append(str(i))
        return result
