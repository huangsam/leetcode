# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Max heap gives largest element while min heap gives
        smallest element. Python offers min heap, so we'll
        keep pushing items in until k size. The heappush
        operation will continue balancing everything inside.

        Once the heap become k-size, we check if the current
        item is greater than the smallest item. Then we will pop
        out the smallest item and rebalance everything else in
        the heap with the new item.

        At the end of the loop, the smallest item in the heap
        should be the kth largest item.
        """
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if min_heap[0] < num:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
        return min_heap[0]
