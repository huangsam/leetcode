# https://leetcode.com/problems/4sum/


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Identify all unique quadruplets in the array that sum up to the target.

        Lock in the first two elements and then use two pointers to find the
        remaining two elements that sum up to the target. To speed up the
        process, we skip duplicate elements to avoid redundant checks.

        Complexity:
        - Time: O(n^3)
        - Space: O(n) due to Tim Sort
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            # Dupe check 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Dupe check 2
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                remains = target - nums[i] - nums[j]
                l, r = j + 1, n - 1

                # Two pointer traversal
                while l < r:
                    two_sum = nums[l] + nums[r]
                    if two_sum < remains:
                        l += 1
                    elif two_sum > remains:
                        r -= 1
                    else:
                        # Add to result when it is distinct
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        # Dupe check 3
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

        return result
