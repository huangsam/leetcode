# https://leetcode.com/problems/number-of-recent-calls/

from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        """
        Return the number of pings that have been made from 3000 milliseconds
        ago until now. It is guaranteed that every call to ping uses a
        strictly larger value of t.

        Complexity:
        - Time: O(1) amortized. Each ping is added and removed once
        - Space: O(W), where W is the size of the window
        """
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
