# https://leetcode.com/problems/course-schedule/

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Determine if it is possible to finish all courses given the prerequisite pairs.

        Approach:
        - Treat courses as nodes and prerequisites as directed edges: [a, b] means b -> a.
        - Use Kahn's algorithm (BFS topological sort) with in-degrees.
        - Initialize an adjacency list and compute in-degrees for all nodes.
        - Push all courses with in-degree 0 (no prerequisites) onto a queue.
        - Pop courses one-by-one, incrementing a count of completed courses and
          decrementing the in-degrees of dependent courses.
        - If a dependent course's in-degree drops to 0, add it to the queue.
        - If total completed courses equals numCourses, no cycles exist; return True.

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
