# https://leetcode.com/problems/find-the-highest-altitude/


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """
        Find the highest altitude of a point.

        We encode the prefix sum into current. As we continue to update
        the variable, we track the max height found so far.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        current = 0
        highest = 0
        for num in gain:
            current += num
            highest = max(highest, current)
        return highest
