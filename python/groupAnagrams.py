# https://leetcode.com/problems/group-anagrams/

from collections import Counter, defaultdict
from typing import DefaultDict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together from a list of strings.

        Assume that anagram is simply a map of alpha counts.

        Then we can create a hash key from the character frequency count.
        Each unique hash key will map to a list of strings that are anagrams.

        Lastly, we iterate through the values of the dictionary, returning
        it as a list of lists.

        Complexity:
        - Time: O(n * k)
        - Space: O(n * k)
        """
        strings_by_hash: DefaultDict[tuple, list] = defaultdict(list)
        for content in strs:
            strings_by_hash[self._getKey(content)].append(content)
        return list(strings_by_hash.values())

    def _getKey(self, content: str) -> tuple:
        return tuple(sorted(Counter(content).items()))
