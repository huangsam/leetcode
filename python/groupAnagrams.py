# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Assume that anagram is simply a map of alpha counts.

        Then we will generate a hash based on the frequency
        count of all 26 letters in the alphabet.

        Then each of the strings with the exact same
        hash will fall under the same key.

        Lastly, we iterate through the values of the
        dictionary, returning it as a list of lists.
        """
        strings_by_hash: defaultdict[int, list] = defaultdict(list)
        for content in strs:
            strings_by_hash[self.getHash(content)].append(content)
        return list(strings_by_hash.values())

    def getHash(self, content: str) -> int:
        freq = [0] * 26
        for ch in content:
            freq[ord(ch) - ord('a')] += 1
        key_list = []
        for idx, val in enumerate(freq):
            key_list.append(f'{idx}-{val}')
        return hash(tuple(key_list))
