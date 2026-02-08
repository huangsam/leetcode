# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/


class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Find the minimum number of deletions required to make the string balanced.

        A string is balanced if there are no 'b' characters before any 'a' characters.
        We can solve this by counting the number of 'b's we have seen so far and
        the number of 'a's we need to delete to maintain balance. The minimum
        deletions at any point will be the sum of 'b's seen and 'a's left.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        b_count = 0  # Count of 'b' characters seen so far
        a_count = s.count("a")  # Total count of 'a' characters in the string
        min_deletions = a_count  # Start with the case where we delete all 'a's

        for char in s:
            if char == "b":
                b_count += 1
            else:  # char == 'a'
                a_count -= 1

            # The deletions needed at this point is the sum of 'b's seen and 'a's left
            min_deletions = min(min_deletions, b_count + a_count)

        return min_deletions
