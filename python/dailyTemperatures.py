# https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Given a list of daily temperatures, return a list such that, for each
        day in the input, tells you how many days you would have to wait until
        a warmer temperature. If no such day exists, put 0 instead.

        Uses a monotonic stack to keep track of of the indices of the
        temperatures that have not yet found a warmer temperature.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        answer = [0] * len(temperatures)

        st: list[int] = []

        for i, temp in enumerate(temperatures):
            # While a warmer temperature exists
            while st and temp > temperatures[st[-1]]:
                j = st.pop()

                # Store the number of days waiting until the warmer temp
                answer[j] = i - j

            st.append(i)

        return answer
