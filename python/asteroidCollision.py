# https://leetcode.com/problems/asteroid-collision/

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Find out the state of the asteroids after all collisions.

        The indices of the asteroids in the input list represent their positions.
        The absolute value of each element represents the size of the asteroid.
        The sign represents its direction (+ => right, - => left).
        Each asteroid moves at the same speed.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        st: List[int] = []
        for num in asteroids:
            # Right-moving asteroids never cause a collision
            if num > 0:
                st.append(num)
                continue

            # Clean out smaller collisions
            while st and 0 < st[-1] < -num:
                st.pop()

            # Case 1: All right collisions are complete
            if not st or st[-1] < 0:
                st.append(num)

            # Case 2: Right collision is as big as left collision
            elif st[-1] == -num:
                st.pop()

        return st
