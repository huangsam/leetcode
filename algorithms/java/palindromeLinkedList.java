// https://leetcode.com/problems/palindrome-linked-list/description/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
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

/*
Test cases:
[0, 0]
[1, 2, 3, 2, 1]
[3, 1, 3]
[2, 5, 4, 2]
[1, 2, 3]
[]
*/
