class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Get the binary representation for each number i from
        0..n and literally count the number of 1s in each
        string...
        """
        return [bin(i)[2:].count('1') for i in range(n + 1)]
