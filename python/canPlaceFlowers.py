# https://leetcode.com/problems/can-place-flowers/

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Time: O(n)
        Space: O(1)
        
        Simply iterate through the flowerbed and plant flowers where possible.
        Keep track of how many flowers we have planted.
        If we reach the required number of flowers, return True. Otherwise, False.
        """
        if n == 0:
            return True

        idx = 0
        length = len(flowerbed)
        count = 0

        while idx < length:
            if flowerbed[idx] == 0:
                # Treat the boundaries as if they are 0s
                prev_is_empty = idx == 0 or flowerbed[idx - 1] == 0
                next_is_empty = idx == length - 1 or flowerbed[idx + 1] == 0

                if prev_is_empty and next_is_empty:
                    # Plant the flower!
                    # We must modify the bed so the NEXT check knows this spot is now full
                    flowerbed[idx] = 1
                    count += 1

                    if count >= n:
                        return True

            idx += 1

        return count >= n
