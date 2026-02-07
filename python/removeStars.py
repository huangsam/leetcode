# https://leetcode.com/problems/removing-stars-from-a-string/

from typing import List


class Solution:
    def removeStars(self, s: str) -> str:
        """
        Return the string after removing stars and the closest non-star characters
        to their left.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        builder: List[str] = []
        for ch in s:
            if ch == "*":
                # Remove the closest non-star character to the left
                builder.pop()
            else:
                # Append the non-star character as usual
                builder.append(ch)
        return "".join(builder)
