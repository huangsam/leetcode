# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Group anagrams together from a list of strings.

        If we treat an anagram as simply a map of alpha counts, then we can
        use a hash table to group them together. Lastly, we can return the
        values of the hash table as a list of lists.

        Complexity:
        - Time: O(n * k log k)
        - Space: O(n * k)
        """
        strings_by_hash: defaultdict[str, list] = defaultdict(list)
        for content in strs:
            sorted_hash = "".join(sorted(content))
            strings_by_hash[sorted_hash].append(content)
        return list(strings_by_hash.values())
