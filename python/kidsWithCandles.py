from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Complexity:
        - Time: O(n)
        - Space: O(n)

        Start by finding the max possible value. Then create a boolean list
        of len(candies) where you literally go through a second pass. Can I be
        more efficient simply by relying the i and i-1? No I don't think so
        because that would only give you the local maxima, not the absolute
        maxima. You can only find the absolute maxima in O(N).
        """
        max_count_for_kid = max(candies)

        result = [False] * len(candies)
        for index, current_count in enumerate(candies):
            if current_count + extraCandies >= max_count_for_kid:
                result[index] = True

        return result
