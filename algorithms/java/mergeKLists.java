// https://leetcode.com/problems/merge-k-sorted-lists/description/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        ListNode temp;
        if (l1.val > l2.val) {
            temp = l2;
            temp.next = mergeTwoLists(l1, l2.next);
            return temp;
        }
        else {
            temp = l1;
            temp.next = mergeTwoLists(l1.next, l2);
            return temp;
        }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 2) {
            return mergeTwoLists(lists[0], lists[1]);
        } else if (lists.length == 1) {
            return lists[0];
        } else if (lists.length == 0) {
            return null;
        }
        int half = lists.length / 2;
        ListNode leftList = mergeKLists(Arrays.copyOfRange(lists, 0, half));
        ListNode rightList = mergeKLists(Arrays.copyOfRange(lists, half, lists.length));
        return mergeTwoLists(leftList, rightList);
    }
}
