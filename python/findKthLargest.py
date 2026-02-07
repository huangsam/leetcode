# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find the kth largest element in an unsorted array.

        We use a min heap to keep track of the k largest items.
        If heap has k items when a new item comes, we pop out
        the smallest item and insert the new item in.

        At the end of the loop, the smallest item in the heap
        should be the kth largest item.

        Complexity:
        - Time: O(n * log(k))
        - Space: O(k)
        """
        min_heap: List[int] = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if min_heap[0] < num:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        return min_heap[0]
