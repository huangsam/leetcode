// https://leetcode.com/problems/merge-k-sorted-lists/

import java.util.Arrays;

import container.ListNode;

public class MergeKLists {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 2) {
            return mergeTwoLists(lists[0], lists[1]);
        }
        if (lists.length == 1) {
            return lists[0];
        }
        if (lists.length == 0) {
            return null;
        }
        int half = lists.length / 2;
        return mergeTwoLists(
            mergeKLists(Arrays.copyOfRange(lists, 0, half)),
            mergeKLists(Arrays.copyOfRange(lists, half, lists.length))
        );
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        return (list1.val < list2.val)
            ? new ListNode(
            list1.val, mergeTwoLists(list1.next, list2))
            : new ListNode(
            list2.val, mergeTwoLists(list1, list2.next));
    }
}
