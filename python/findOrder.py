# https://leetcode.com/problems/course-schedule-ii/


from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Find the ordering of courses to take for all courses. If no such ordering
        exists, then return an empty list.

        We use Kahn's BFS approach here. Note that when a course no longer
        has dependencies, traversal starts across the unlocked courses.

        Complexity:
        - Time: O(v + e) where v = course count and e = req count
        - Memory: O(v)
        """
        adj: list[list[int]] = [[] for _ in range(numCourses)]
        in_degree: list[int] = [0] * numCourses

        result: list[int] = []

        for target, depend in prerequisites:
            adj[depend].append(target)
            in_degree[target] += 1

        q: deque[int] = deque(i for i, deg in enumerate(in_degree) if deg == 0)

        while q:
            item = q.popleft()
            result.append(item)
            for unlock in adj[item]:
                in_degree[unlock] -= 1
                if in_degree[unlock] == 0:
                    q.append(unlock)

        if len(result) != numCourses:
            return []
        return result
