// https://leetcode.com/problems/merge-two-sorted-lists/

import container.ListNode;

public final class MergeTwoLists {
    /**
     * Let us proceed by creating a dummy node to minimize null checks.
     * Since list1 and list2 are sorted in increasing order, we can
     * traverse from start to end and link them to next pointer from
     * the dummy onwards. Once the looping is done, whichever one
     * still has leftover can be appended to the tail of the new
     * list. Returning the result should just be dummy.next.
     */
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        ListNode current = dummy;
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                current.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                current.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            current = current.next;
        }
        current.next = (list1 != null) ? list1 : list2;
        return dummy.next;
    }

    public ListNode mergeTwoListsRecursive(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }
        ListNode temp;
        if (l1.val > l2.val) {
            temp = l2;
            temp.next = mergeTwoListsRecursive(l1, l2.next);
            return temp;
        } else {
            temp = l1;
            temp.next = mergeTwoListsRecursive(l1.next, l2);
            return temp;
        }
    }
}
