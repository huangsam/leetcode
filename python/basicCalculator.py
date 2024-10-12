# https://leetcode.com/problems/basic-calculator-ii/

from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack: List[int] = []
        num = 0
        op = "+"
        slen = len(s)
        for i in range(slen):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in ("+", "-", "/", "*") or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    tmp = stack.pop()
                    stack.append(tmp * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:  # round negval down
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                num = 0
                op = s[i]
        return sum(stack)
