// https://leetcode.com/problems/merge-k-sorted-lists/

import container.ListNode;

import java.util.Comparator;
import java.util.PriorityQueue;

public class MergeKLists {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }

        PriorityQueue<ListNode> queue = new PriorityQueue<>(
            Comparator.comparingInt(n -> n.val));

        for (ListNode node : lists) {
            if (node != null) {
                queue.add(node);
            }
        }

        ListNode dummy = new ListNode();
        ListNode current = dummy;

        while (!queue.isEmpty()) {
            ListNode lowest = queue.poll();
            current.next = lowest;
            current = current.next;
            if (lowest.next != null) {
                queue.add(lowest.next);
            }
        }

        return dummy.next;
    }
}
