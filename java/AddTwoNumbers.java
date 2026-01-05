// https://leetcode.com/problems/add-two-numbers/

import container.ListNode;

public class AddTwoNumbers {
    private static final int TEN = 10;

    /**
     * Adds two numbers represented as linked lists and returns the sum as a linked list.
     * Each node in the input linked lists contains a single digit, and the digits are stored
     * in reverse order, meaning the 1's digit is at the head of the list.
     *
     * <p> The method handles cases where the input lists have different lengths and also accounts
     * for any carry that may result from the addition.
     *
     * <p>Complexity:
     * <ul>
     *     <li>Time: O(max(m, n)), where m and n are lengths of the input lists.</li>
     *     <li>Space: O(max(m, n)), as we create a new list for the result.</li>
     * </ul>
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) {
            return null; // Both lists empty
        }

        ListNode result = new ListNode(); // Avoids extra null checks
        ListNode current = result;
        boolean carry = false;

        while (l1 != null || l2 != null || carry) {
            int val = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + (carry ? 1 : 0);

            carry = val >= TEN;
            val %= TEN;

            ListNode newNode = new ListNode(val);
            current.next = newNode;
            current = newNode;

            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }

        return result.next;
    }
}
