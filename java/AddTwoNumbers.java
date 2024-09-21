// https://leetcode.com/problems/add-two-numbers/

import container.ListNode;

public final class AddTwoNumbers {
    public static final int TEN = 10;

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(-1);
        ListNode current = result;
        ListNode tmp = null;
        boolean carry = false;
        int val = 0;

        while (l1 != null && l2 != null) {
            val = l1.val + l2.val;
            if (carry) {
                val += 1;
            }

            if (val >= TEN) {
                carry = true;
                val %= TEN;
            } else {
                carry = false;
            }

            tmp = new ListNode(val);
            current.next = tmp;
            current = tmp;

            l1 = l1.next;
            l2 = l2.next;
        }

        while (l1 != null) {
            val = l1.val;
            if (carry) {
                val += 1;
            }
            if (val >= TEN) {
                carry = true;
                val %= TEN;
            } else {
                carry = false;
            }
            tmp = new ListNode(val);
            current.next = tmp;
            current = tmp;
            l1 = l1.next;
        }

        while (l2 != null) {
            val = l2.val;
            if (carry) {
                val += 1;
            }
            if (val >= TEN) {
                carry = true;
                val %= TEN;
            } else {
                carry = false;
            }
            tmp = new ListNode(val);
            current.next = tmp;
            current = tmp;
            l2 = l2.next;
        }

        if (carry) {
            current.next = new ListNode(1);
        }

        return result.next;
    }
}
