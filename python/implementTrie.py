# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    """
    Prefix tree (Trie) supporting word insertion, exact search, and prefix search.

    Approach:
    - Each TrieNode stores a mapping of characters to child TrieNodes and a boolean
      flag indicating whether a valid word terminates at this node.
    - insert(word): Traverse the tree down each character of the word, creating
      new nodes whenever a character branch is missing. Mark the final node as end of word.
    - search(word): Traverse down each character. If any character branch is missing,
      return False. If all match, return whether the last node is marked as end of word.
    - startsWith(prefix): Similar to search, but only checks that the path exists
      (regardless of whether a complete word ends there).

    Complexity:
    - Time:
        - insert: O(L) where L is the length of the word
        - search: O(L) where L is the length of the word
        - startsWith: O(P) where P is the length of the prefix
    - Space: O(N * L) total memory in worst case, where N is the number of keys
      and L is the average length
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
