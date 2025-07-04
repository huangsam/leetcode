// https://leetcode.com/problems/swap-nodes-in-pairs/

import container.ListNode;

class SwapPairs {
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
