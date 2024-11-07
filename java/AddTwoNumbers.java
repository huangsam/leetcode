// https://leetcode.com/problems/add-two-numbers/

import container.ListNode;

public class AddTwoNumbers {
    private static final int TEN = 10;

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) {
            return null; // Both lists empty
        }

        ListNode result = new ListNode(0); // No dummy value needed
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

        return result;
    }
}
