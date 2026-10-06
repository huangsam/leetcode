# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    """
    Prefix tree (Trie) supporting word insertion, exact search, and prefix search.

    Approach:
    - Store child character nodes in a dict and track end of word with a boolean flag
    - On insert: traverse characters, create missing nodes, and mark last node as word end
    - On search: traverse characters and verify final node is marked as end of word
    - On startsWith: traverse characters and verify prefix path exists in the tree

    Complexity:
    - Time: O(L) for insert/search and O(P) for startsWith, where L/P are string lengths
    - Space: O(N * L) total memory, where N is key count and L is average key length
    """

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
