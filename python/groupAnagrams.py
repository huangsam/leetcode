# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Group anagrams together from a list of strings.

        Assume that anagram is simply a map of alpha counts.

        Then we can create a hash key from the sorted version of each string.
        Each unique hash key will map to a list of strings that are anagrams.

        Lastly, we iterate through the values of the dictionary, returning
        it as a list of lists.

        Complexity:
        - Time: O(n * k log k)
        - Space: O(n * k)
        """
        strings_by_hash: defaultdict[str, list] = defaultdict(list)
        for content in strs:
            sorted_hash = "".join(sorted(content))
            strings_by_hash[sorted_hash].append(content)
        return list(strings_by_hash.values())
