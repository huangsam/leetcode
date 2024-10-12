# https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        We are going to collect the mapping of character frequencies
        for ransom note. Then we subtract the frequencies when iterating
        through magazine. If ransom mapping has all values <= 0, then we
        are good to construct the ransom note.
        """
        ransom_mapping = {}

        for ch in ransomNote:
            if ch not in ransom_mapping:
                ransom_mapping[ch] = 0
            ransom_mapping[ch] += 1

        for ch in magazine:
            if ch in ransom_mapping:
                ransom_mapping[ch] -= 1

        return all(val <= 0 for val in ransom_mapping.values())
