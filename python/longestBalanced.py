# https://leetcode.com/problems/longest-balanced-subarray-ii/

from typing import Dict, List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        """
        Finds the length of the longest balanced subarray in the given
        list of integers. A balanced subarray is defined as a subarray
        where the number of distinct even numbers equals the number of
        distinct odd numbers.

        The algorithm uses a segment tree with lazy propagation to efficiently
        track the difference between the count of distinct even and odd numbers in
        various subarrays. It updates the tree as it iterates through the
        input list and performs binary searches to find the longest balanced
        subarray at each step.

        Complexity:
        - Time: O(n log n)
        - Space: O(n)
        """
        n = len(nums)
        if n == 0:
            return 0

        # Using flat lists for high performance
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        tree_lazy = [0] * (4 * n)

        def push(node, s, e):
            """Pushes the lazy updates down to the children of the current node."""
            # If it's a leaf node or there's nothing to push, exit
            if tree_lazy[node] == 0 or s == e:
                # Safety clear the lazy value to prevent stale updates
                tree_lazy[node] = 0
                return

            v = tree_lazy[node]
            # Left child
            tree_min[2 * node + 1] += v
            tree_max[2 * node + 1] += v
            tree_lazy[2 * node + 1] += v
            # Right child
            tree_min[2 * node + 2] += v
            tree_max[2 * node + 2] += v
            tree_lazy[2 * node + 2] += v

            tree_lazy[node] = 0

        def update(node, s, e, l, r, val):
            """Updates the segment tree in the range [l, r] by adding val."""
            if l <= s and e <= r:
                tree_min[node] += val
                tree_max[node] += val
                tree_lazy[node] += val
                return

            push(node, s, e)
            m = (s + e) // 2
            if l <= m:
                update(2 * node + 1, s, m, l, r, val)
            if r > m:
                update(2 * node + 2, m + 1, e, l, r, val)

            tree_min[node] = min(tree_min[2 * node + 1], tree_min[2 * node + 2])
            tree_max[node] = max(tree_max[2 * node + 1], tree_max[2 * node + 2])

        def find_leftmost_zero(node, s, e, l, r):
            """Finds the leftmost index in the range [l, r] where the value is zero."""
            # If 0 isn't within [min, max], or we are out of range, prune the search
            if tree_min[node] > 0 or tree_max[node] < 0 or s > r or e < l:
                return -1
            if s == e:
                return s

            push(node, s, e)
            m = (s + e) // 2

            # Binary search behavior: Always check the left side first
            res = find_leftmost_zero(2 * node + 1, s, m, l, r)
            if res == -1:  # Only check right if left didn't have a zero
                res = find_leftmost_zero(2 * node + 2, m + 1, e, l, r)
            return res

        ans = 0
        last_seen: Dict[int, int] = {}

        for i, val in enumerate(nums):
            prev_idx = last_seen.get(val, -1)
            diff = 1 if val % 2 == 0 else -1

            # The "Clever" bit: Update the range where this instance is 'distinct'
            update(0, 0, n - 1, prev_idx + 1, i, diff)
            last_seen[val] = i

            # Binary search through the tree for the earliest zero in the current valid window
            leftmost_l = find_leftmost_zero(0, 0, n - 1, 0, i)
            if leftmost_l != -1:
                ans = max(ans, i - leftmost_l + 1)

        return ans
