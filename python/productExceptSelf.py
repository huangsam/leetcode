# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1)

        For example [1,2,3,4] ->

        Multiply answer[i] by prefix product, before nums[i].

        prefix @ nums[0] -> $1
        prefix @ nums[1] -> $1 * 1
        prefix @ nums[2] -> $1 * 1 * 2
        prefix @ nums[3] -> $1 * 1 * 2 * 3

        Multiply answer[i] by suffix product, before nums[i].

        suffix @ nums[3] -> $1
        suffix @ nums[2] -> $1 * 4
        suffix @ nums[1] -> $1 * 4 * 3
        suffix @ nums[0] -> $1 * 4 * 3 * 2
        """
        answer = [1] * len(nums)
        left_val, right_val = 1, 1
        for left_idx in range(len(nums)):
            right_idx = len(nums) - left_idx - 1

            left_num, right_num = nums[left_idx], nums[right_idx]

            # Prefix product before nums[left_idx]
            answer[left_idx] *= left_val

            # Suffix product before nums[right_idx]
            answer[right_idx] *= right_val

            left_val *= left_num
            right_val *= right_num
        return answer
