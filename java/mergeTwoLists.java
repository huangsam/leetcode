// https://leetcode.com/problems/merge-two-sorted-lists/

import container.ListNode;

public class mergeTwoLists {
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

    public ListNode mergeTwoListsRecursive(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
        if(l2 == null) return l1;
        ListNode temp;
        if(l1.val > l2.val) {
            temp = l2;
            temp.next = mergeTwoListsRecursive(l1,l2.next);
            return temp;
        }
        else {
            temp = l1;
            temp.next = mergeTwoListsRecursive(l1.next,l2);
            return temp;
        }
    }
}
