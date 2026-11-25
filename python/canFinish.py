# https://leetcode.com/problems/course-schedule/

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Determine if it is possible to finish all courses given the prerequisites.
        They are represented as a list of pairs [a, b] where b is needed for a.

        Approach:
        - Treat courses as nodes and prerequisites as directed edges: [a, b] means b -> a
        - Build an adjacency list and compute in-degrees for all courses
        - Push courses with in-degree 0 onto a BFS queue
        - Pop courses one by one and decrement neighbor in-degrees
        - Add neighbors to queue once their in-degree reaches 0
        - Return True if completed course count equals numCourses, else False

        Complexity:
        - Time: O(v + e) where v = numCourses and e = len(prerequisites)
        - Space: O(v + e) for adjacency list, in-degree tracker, and queue
        """
        # Tracks index as course and value as the courses that depend on it
        adj: list[list[int]] = [[] for _ in range(numCourses)]
        # Tracks index as course and value as the number of prerequisites
        in_degrees: list[int] = [0] * numCourses

        for target, depend in prerequisites:
            adj[depend].append(target)
            in_degrees[target] += 1

        queue: deque[int] = deque(course for course in range(numCourses) if in_degrees[course] == 0)
        completed = 0

        while queue:
            cur = queue.popleft()
            completed += 1

            # Decrease in-degree for all neighbors and add to queue if
            # they have no remaining prerequisites
            for neighbor in adj[cur]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses

    def canFinishDepth(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        With this variation, we want to check whether a cycle exists or not.
        If no cycle exists, then all tasks can be completed.

        Complexity:
        - Time: O(v + e)
        - Memory: O(v)
        """
        visiting: set[int] = set()
        visited: set[int] = set()

        # Adjacency list for exactly n courses
        adj: list[list[int]] = [[] for _ in range(numCourses)]

        for target, depend in prerequisites:
            adj[depend].append(target)

        def dfs(course: int) -> bool:
            """Check whether a cycle exists or not."""
            if course in visited:
                return False
            if course in visiting:
                return True
            visiting.add(course)
            for neighbor in adj[course]:
                if dfs(neighbor):
                    return True
            visiting.remove(course)
            visited.add(course)
            return False

        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False

        return True
