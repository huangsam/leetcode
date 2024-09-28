# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Iterate through the linked list, collect the ids of each list node
        and store them sequentially in an array, and store the random id that
        they are connected to (or None).

        These two sets of data should be sufficient to reconstruct a fully
        new copy of the linked list, such that all the brand new nodes are
        not pointing at nodes in the original list.
        """
        if not head:
            return None

        # Mapping of list index -> original node
        old_ids = []

        # Mapping of current node -> random node
        id_to_id = {}

        # Mapping of original node -> list index
        id_to_idx = {}

        # List of new nodes, with same size and same values
        new_list = []

        curr, idx = head, 0
        while curr:
            # Copy node values from original list
            new_list.append(Node(curr.val))

            curr_id, random_id = id(curr), id(curr.random)

            # Connect current index to random index of original list
            old_ids.append(curr_id)
            id_to_id[curr_id] = random_id if curr.random is not None else None
            id_to_idx[curr_id] = idx

            curr = curr.next
            idx += 1

        first = new_list[0]
        first.random = self.getRandom(new_list, old_ids, id_to_id, id_to_idx, 0)

        for i in range(1, len(new_list)):
            prev, curr = new_list[i-1], new_list[i]
            prev.next = curr
            curr.random = self.getRandom(new_list, old_ids, id_to_id, id_to_idx, i)

        # Return head pointer
        return new_list[0]

    def getRandom(self, new_list, old_ids, id_to_id, id_to_idx, n) -> 'Optional[Node]':
        id_at_n = old_ids[n]
        random_at_n = id_to_id[id_at_n]
        random_idx = id_to_idx[random_at_n] if random_at_n else -1
        return new_list[random_idx] if random_idx >= 0 else None
