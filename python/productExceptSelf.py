# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1,2,3,4 -> 1,2,6,24
        24/1, 24/2, 24/3, 24/4
        """
        # Figure out where the zeros are
        zero_at = []

        # Figure out what the total non-zero product is
        product = 1

        for idx, num in enumerate(nums):
            if num != 0:
                product *= num
            else:
                zero_at.append(idx)

        answer = [0] * len(nums)

        if len(zero_at) >= 2:
            return answer

        if len(zero_at) == 1:
            answer[zero_at[0]] = product
            return answer

        for i in range(len(nums)):
            answer[i] = product // nums[i]

        return answer
