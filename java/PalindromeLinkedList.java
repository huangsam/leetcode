// https://leetcode.com/problems/palindrome-linked-list/

import container.ListNode;

public class PalindromeLinkedList {
    /**
     * Test cases to evaluate:
     *
     * <pre>
     * [0] -> true
     * [0, 0] -> true
     * [1, 2, 3, 2, 1] -> true
     * [3, 1, 3] -> true
     * [2, 5, 4, 2] -> false
     * [1, 2, 3] -> false
     * </pre>
     */
    public boolean isPalindrome(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        while (current != null) {
            ListNode tmp = new ListNode(current.val);
            current = current.next;
            tmp.next = prev;
            prev = tmp;
        }
        while (head != null && prev != null) {
            if (head.val != prev.val) {
                return false;
            }
            head = head.next;
            prev = prev.next;
        }
        return true;
    }
}
