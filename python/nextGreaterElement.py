# https://leetcode.com/problems/next-greater-element-i/


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Find the next greater element for every element in nums1 which matches
        an element in nums2. nums1 doesn't have to be ordered like nums2.
        All numbers in nums1 and nums2 are unique.

        Use a hash map from val to idx to reduce the lookup time for nums2 into
        nums1 if such a number exists.

        Complexity:
        - Time: O(n + m)
        - Memory: O(n + m)
        """
        idx1_map: dict[int, int] = {num: i for i, num in enumerate(nums1)}
        st2: list[int] = []
        ans1: list[int] = [-1] * len(nums1)
        ans2: list[int] = [-1] * len(nums2)
        for i, val in enumerate(nums2):
            while st2 and val > nums2[st2[-1]]:
                j = st2.pop()
                ans2[j] = val

                # Get the matching result for nums1[i] == nums2[j]
                val2 = nums2[j]
                if val2 in idx1_map:
                    ans1[idx1_map[val2]] = val

            # Keep appending to the stack
            st2.append(i)

        return ans1
