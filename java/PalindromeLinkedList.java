// https://leetcode.com/problems/palindrome-linked-list/

import container.ListNode;

public class PalindromeLinkedList {
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
