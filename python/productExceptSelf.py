# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Return an array where each element is the product of all others.

        For example [1,2,3,4] ->

        Multiply answer[i] by prefix product, before nums[i] from the left.

        prefix @ nums[0] -> $1
        prefix @ nums[1] -> $1 * 1
        prefix @ nums[2] -> $1 * 1 * 2
        prefix @ nums[3] -> $1 * 1 * 2 * 3

        Multiply answer[i] by suffix product, before nums[i] from the right.

        suffix @ nums[3] -> $1
        suffix @ nums[2] -> $1 * 4
        suffix @ nums[1] -> $1 * 4 * 3
        suffix @ nums[0] -> $1 * 4 * 3 * 2

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        n = len(nums)
        answer = [1] * n
        left_prefix, right_suffix = 1, 1
        for left_idx in range(n):
            right_idx = n - left_idx - 1
            left_num, right_num = nums[left_idx], nums[right_idx]

            # Update answer with prefix and suffix products
            answer[left_idx] *= left_prefix
            answer[right_idx] *= right_suffix

            # Update prefix and suffix products
            left_prefix *= left_num
            right_suffix *= right_num
        return answer
