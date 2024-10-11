# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        For example [1,2,3,4] ->

        Multiply answer[i] by prefix product, before nums[i].

        prefix @ num[0] -> $1
        prefix @ num[1] -> $1 * 1
        prefix @ num[2] -> $1 * 1 * 2
        ...

        Multiply answer[i] by suffix product, before nums[i].

        suffix @ num[0] -> $1 * 4 * 3 * 2
        suffix @ num[1] -> $1 * 4 * 3
        suffix @ num[2] -> $1 * 4
        ...
        """
        answer = [1] * len(nums)

        # Multiply answer by prefix, just before including num
        left = 1
        for idx, num in enumerate(nums):
            answer[idx] *= left
            left *= num

        # Multiply answer by suffix, just before including num
        right = 1
        for idx, num in enumerate(nums[::-1]):
            answer[len(nums) - idx - 1] *= right
            right *= num

        return answer
