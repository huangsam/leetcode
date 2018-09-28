// https://leetcode.com/problems/add-two-numbers/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
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

            if (val >= 10) {
                carry = true;
                val %= 10;
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
            if (val >= 10) {
                carry = true;
                val %= 10;
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
            if (val >= 10) {
                carry = true;
                val %= 10;
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
