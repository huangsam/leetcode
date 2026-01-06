# https://leetcode.com/problems/basic-calculator-ii/

from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        """
        Implement a basic calculator to evaluate a simple expression string.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        if not s:
            return 0

        stack: List[int] = []
        num = 0
        op = "+"

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            # Check if it's an operator or the end of the string
            # The 'or' condition acts as a trigger to process the number and current operator
            if ch in ("+", "-", "/", "*") or i == len(s) - 1:
                match op:
                    case "+":
                        stack.append(num)
                    case "-":
                        stack.append(-num)
                    case "*":
                        tmp = stack.pop()
                        stack.append(tmp * num)
                    case "/":
                        tmp = stack.pop()
                        if tmp // num < 0 and tmp % num != 0:
                            stack.append(tmp // num + 1)
                        else:
                            stack.append(tmp // num)

                # Reset num and update the operator
                num = 0

                # Update the operator to the current character
                op = ch

        return sum(stack)
