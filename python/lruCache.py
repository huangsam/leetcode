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
    - Combine a hash map for O(1) lookups with a doubly-linked list for O(1) reordering
    - Use dummy head and tail sentinels to eliminate boundary null checks
    - Maintain least recently used node at head and most recently used node at tail
    - On get: detach existing node, re-insert at tail, and return value (or -1 if missing)
    - On put: update and move existing node to tail, or insert new node at tail
    - Evict node after dummy head and remove from map when capacity is exceeded

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
