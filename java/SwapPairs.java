// https://leetcode.com/problems/swap-nodes-in-pairs/

import container.ListNode;

class SwapPairs {
    /**
     * Swaps every two adjacent nodes in a linked list and returns the modified list.
     * If the list has an odd number of nodes, the last node remains unchanged.
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(n)</li>
     *     <li>Space: O(1)</li>
     * </ul>
     */
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(-1);
        ListNode prev = dummy;
        ListNode curr = head;

        // Handle all pair swaps first
        while (curr != null && curr.next != null) {
            ListNode nxt = curr.next;
            ListNode tmp = nxt.next;

            // Swap positions and links
            nxt.next = curr;
            curr.next = tmp;

            // Link prev to swapped nxt
            prev.next = nxt;

            // Advance to the next pair
            prev = curr;
            curr = curr.next;
        }

        // Handle final node as last step
        if (curr != null) {
            prev.next = curr;
        }

        return dummy.next;
    }
}
