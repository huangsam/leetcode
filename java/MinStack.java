// https://leetcode.com/problems/min-stack/

import java.util.Deque;
import java.util.LinkedList;

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
public class MinStack {
    private final Deque<Integer> standard;
    private final Deque<Integer> minimum;

    public MinStack() {
        standard = new LinkedList<>();
        minimum = new LinkedList<>();
    }

    public void push(int val) {
        standard.addFirst(val);
        if (minimum.isEmpty() || minimum.getFirst() >= val) {
            minimum.addFirst(val);
        }
    }

    public void pop() {
        if (standard.isEmpty()) {
            return;
        }
        Integer removed = standard.removeFirst();
        if (!minimum.isEmpty() && removed.equals(minimum.getFirst())) {
            minimum.removeFirst();
        }
    }

    public int top() {
        return standard.getFirst();
    }

    public int getMin() {
        return minimum.getFirst();
    }
}
