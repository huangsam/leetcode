# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = max(len(word1), len(word2))
        diff_length = abs(len(word1) - len(word2))

        i = 0
        merged_chars = []

        # Store characters from overlapping ranges
        while i < max_length - diff_length:
            merged_chars.append(word1[i])
            merged_chars.append(word2[i])
            i += 1

        # Store characters from longer word
        if len(word1) > len(word2):
            merged_chars.extend(word1[i : i + diff_length])
        else:
            merged_chars.extend(word2[i : i + diff_length])

        return "".join(merged_chars)
