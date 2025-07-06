# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(f"0b{a}", 2) + int(f"0b{b}", 2))[2:]
