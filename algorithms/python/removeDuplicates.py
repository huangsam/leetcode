# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_found = 0
        cur_num = None
        for num in nums:
            if cur_num is None or cur_num != num:
                cur_num = num
                nums[nums_found] = cur_num
                nums_found += 1
        return nums_found
