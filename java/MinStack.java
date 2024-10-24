// https://leetcode.com/problems/min-stack/

import java.util.Deque;
import java.util.LinkedList;

public class MinStack {
    private Deque<Integer> standard;
    private Deque<Integer> minimum;

    public MinStack() {
        standard = new LinkedList<>();
        minimum = new LinkedList<>();
    }

    public void push(int val) {
        standard.addFirst(val);
        if (minimum.size() == 0 || minimum.getFirst() >= val) {
            minimum.addFirst(val);
        }
    }

    public void pop() {
        if (standard.size() == 0) {
            return;
        }
        Integer removed = standard.removeFirst();
        if (minimum.size() > 0 && removed.equals(minimum.getFirst())) {
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

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
