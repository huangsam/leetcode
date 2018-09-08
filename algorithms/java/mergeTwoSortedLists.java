/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(-1);
        ListNode current = result;
        ListNode tmp = null;

        while (true) {
            if (l1 == null) {
                current.next = l2;
                break;
            } else if (l2 == null) {
                current.next = l1;
                break;
            } else {
                if (l1.val <= l2.val) {
                    tmp = l1;
                    l1 = l1.next;
                } else {
                    tmp = l2;
                    l2 = l2.next;
                }
            }
            current.next = tmp;
            current = current.next;
        }
        return result.next;
    }
}
