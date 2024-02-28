# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    @staticmethod
    def checkAdjustedDistance(a: int, b: int) -> int:
        return min(b - a, 2)

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates up to size of 2.

        Approach
        - Go through N-1 uniques. Whenever there is a mismatch
            - Set range value as old unique
            - Set kth value as new unique
        - Go through Nth unique. If there are more than two items
            - Set range value as Nth unique
        """
        k = 0
        uniq = 0
        cur = 0

        while cur < len(nums):
            if nums[uniq] != nums[cur]:
                dist = self.checkAdjustedDistance(uniq, cur)
                nums[k: k + dist] = [nums[k]] * dist
                k += dist
                nums[k] = nums[cur]
                uniq = cur
            cur += 1

        if cur - 1 > uniq:
            nums[k: k + 2] = [nums[k]] * 2
            return k + 2

        return k + 1
