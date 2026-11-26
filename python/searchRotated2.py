# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """
        Search for a target in a rotated sorted array with duplicates.

        Use the modified binary search from searchRotated but also check
        for the case where [lo] == [mid] == [hi] to handle ambiguity.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True

            # Ambiguous case: both ends match mid
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1

            # Case 1: The left half is sorted
            elif nums[lo] <= nums[mid]:
                # Target is inside this sorted left half
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # Case 2: The right half is sorted
            else:
                # Target is inside this sorted right half
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False
