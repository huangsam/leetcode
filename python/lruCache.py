# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key: int = key
        self.val: int = val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    """
    Least Recently Used (LRU) cache supporting get and put in O(1) time.

    Approach:
    - Combine a hash map (dict) for O(1) key lookups with a doubly-linked list
      to maintain usage order in O(1) time.
    - Use dummy head and tail sentinel nodes to simplify boundary conditions.
    - Head sentinel is adjacent to the least recently used (LRU) node.
    - Tail sentinel is adjacent to the most recently used (MRU) node.
    - On get(key): If present, remove node from current position, insert at tail (MRU),
      and return its value. Otherwise, return -1.
    - On put(key, value): If key exists, update value and move to tail. If new,
      insert at tail. If over capacity, remove node directly after dummy head (LRU).

    Complexity:
    - Time: O(1) for both get and put
    - Space: O(capacity) to store key-node mappings and list nodes
    """

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}

        # Sentinel dummy nodes
        self.head: Node = Node()
        self.tail: Node = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove an existing node from the doubly-linked list."""
        prev_node = node.prev
        next_node = node.next
        if prev_node is not None:
            prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node

    def _insert_at_tail(self, node: Node) -> None:
        """Insert a node right before the tail sentinel (as most recently used)."""
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        if prev_node is not None:
            prev_node.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._insert_at_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert_at_tail(node)
            return

        if len(self.cache) >= self.capacity:
            # Evict LRU node (immediately after head sentinel)
            lru_node = self.head.next
            if lru_node is not None and lru_node != self.tail:
                self._remove(lru_node)
                del self.cache[lru_node.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_at_tail(new_node)
