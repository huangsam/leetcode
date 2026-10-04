# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        Find three integers at distinct indices in nums such that the
        sum is closest to target.

        Approach:
        - Apply sorting as we are only interested in the sum
        - Each number can be treated as an anchor once
        - For the numbers to the right of anchor, we use left and right ptr
        - If cur_sum < target, move left ptr to the right
        - If cur_sum > target, move right ptr to the left
        - If cur_sum == target, abort right away
        - At each iteration, check if abs(target-cur_sum) beats closest_sum
        - If we're closer at any point, update closest_sum

        Complexity:
        - Time: O(n^2)
        - Memory: O(1)
        """
        # Apply sorting as discussed
        nums.sort()

        # Setting a simple baseline instead of float("inf")
        closest_sum = nums[0] + nums[1] + nums[2]

        # Proceed with the approach
        for i in range(len(nums) - 2):
            anchor = nums[i]

            # Skip processing of dupes as the work is already done
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = anchor + nums[left] + nums[right]

                # Abort if we have an exact match!
                if cur_sum == target:
                    return cur_sum

                # Update closest_sum if cur_sum is closer
                if abs(target - cur_sum) < abs(target - closest_sum):
                    closest_sum = cur_sum

                # Update pointer to compensate for target
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1

        return closest_sum
