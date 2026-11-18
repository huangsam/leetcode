# https://leetcode.com/problems/largest-rectangle-in-histogram/


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Find the largest rectangle area in an array of heights.

        Uses mono stack for getting smaller heights. This mono problem
        is unique in that it requires looking at 2 walls and also needs
        a way to flush stack leftovers.

        Complexity:
        - Time: O(n)
        - Memory: O(n)
        """
        # For storing the max area of the rect
        result = 0

        # Mono stack for indices of prior heights
        st: list[int] = []

        # Virtual height 0 at index len(heights) ensures st is flushed
        for i in range(len(heights) + 1):
            height = heights[i] if i < len(heights) else 0

            # The height is the wall for how far the width can be
            while st and height < heights[st[-1]]:
                j = st.pop()

                # Width spans exclusively between left and right walls
                width = i - st[-1] - 1 if st else i

                area = width * heights[j]
                if result < area:
                    result = area

            st.append(i)

        return result
