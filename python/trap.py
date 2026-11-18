# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Calculate the amount of water that can be trapped after raining.

        Maintain the max heights seen so far from both ends. The
        water trapped at each position is determined by the min of
        the max heights from both ends minus the current height.

        Complexity:
        - Time: O(n)
        - Memory: O(1)
        """
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        result = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1

        return result

    def trapWithMonoStack(self, height: list[int]) -> int:
        """
        Calculate the amount of water that can be trapped after raining.

        We use a mono stack to keep track of the indices of the heights.
        Left wall is the last index in the stack, right wall is the
        current index, and the bottom is the index popped from the stack.

        Complexity:
        - Time: O(n)
        - Memory: O(n)
        """
        st: list[int] = []
        result = 0
        for i, h in enumerate(height):
            while st and h > height[st[-1]]:
                j = st.pop()

                # There is no left wall to trap water
                if not st:
                    break

                # Width is based on the left wall and right wall
                width = i - st[-1] - 1

                # Height of water is determined by the shorter wall
                height_diff = min(height[i], height[st[-1]]) - height[j]

                area = height_diff * width

                result += area
            st.append(i)
        return result
