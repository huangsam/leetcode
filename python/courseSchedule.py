# https://leetcode.com/problems/course-schedule/

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Determine if it is possible to finish all courses given the prerequisite pairs.

        Approach:
        - Treat courses as nodes and prerequisites as directed edges: [a, b] means b -> a
        - Build an adjacency list and compute in-degrees for all courses
        - Push courses with in-degree 0 onto a BFS queue
        - Pop courses one by one and decrement neighbor in-degrees
        - Add neighbors to queue once their in-degree reaches 0
        - Return True if completed course count equals numCourses, else False

        Complexity:
        - Time: O(V + E) where V = numCourses and E = len(prerequisites)
        - Space: O(V + E) for adjacency list, in-degree tracker, and queue
        """
        adj: list[list[int]] = [[] for _ in range(numCourses)]
        in_degrees: list[int] = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degrees[course] += 1

        queue: deque[int] = deque(course for course in range(numCourses) if in_degrees[course] == 0)
        completed = 0

        while queue:
            cur = queue.popleft()
            completed += 1

            for neighbor in adj[cur]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
