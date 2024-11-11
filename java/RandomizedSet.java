// https://leetcode.com/problems/insert-delete-getrandom-o1/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
class RandomizedSet {
    private final List<Integer> values;
    private final Map<Integer, Integer> valueToIndex;

    public RandomizedSet() {
        values = new ArrayList<>();
        valueToIndex = new HashMap<>();
    }

    public boolean insert(int val) {
        if (valueToIndex.containsKey(val)) {
            return false;
        }
        values.add(val);
        valueToIndex.put(val, values.size() - 1);
        return true;
    }

    public boolean remove(int val) {
        if (!valueToIndex.containsKey(val)) {
            return false;
        }
        int index = valueToIndex.get(val);
        int lastIndex = values.size() - 1;
        int lastItem = values.get(lastIndex);

        values.set(index, lastItem);
        valueToIndex.put(lastItem, index);

        values.remove(lastIndex);

        valueToIndex.remove(val);

        return true;
    }

    public int getRandom() {
        return values.get(new Random().nextInt(values.size()));
    }
}
