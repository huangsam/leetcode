// https://leetcode.com/problems/palindrome-linked-list/

package solution;

import model.ListNode;

public class PalindromeLinkedList {
    /**
     * Checks if a singly linked list is a palindrome.
     *
     * This is achieved by following multiple steps:
     *
     * <ol>
     *     <li>Find the middle node of the list.</li>
     *     <li>Reverse the second half of the list.</li>
     *     <li>Compare the first half and the reversed second half.</li>
     *     <li>Restore the second half to its original order.</li>
     * </ol>
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(n)</li>
     *     <li>Space: O(1)</li>
     * </ul>
     */
    public boolean isPalindrome(ListNode head) {
        // Handle edge cases with 0 or 1 node
        if (head == null || head.next == null) {
            return true;
        }

        // Find the middle node
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse the list starting from the node after the middle node
        ListNode second = reverseList(slow.next);

        try {
            // Compare the first half and the reversed second half
            ListNode p1 = head, p2 = second;
            while (p2 != null) {
                if (p1.val != p2.val) {
                    return false;
                }
                p1 = p1.next;
                p2 = p2.next;
            }
            return true;
        } finally {
            // Restore the second half of the list to its original order
            slow.next = reverseList(second);
        }
    }

    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        while (current != null) {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }
}
