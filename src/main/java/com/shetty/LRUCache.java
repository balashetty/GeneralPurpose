import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class LRUCache {

    private int capacity;
    private Map<Integer, Integer> map;
    private LinkedList<Integer> list;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.list = new LinkedList<>();
    }

    public int get(int key) {
        if (map.containsKey(key)) {
            list.remove(Integer.valueOf(key));
            list.addLast(key);
            return map.get(key);
        }
        return -1;
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            list.remove(Integer.valueOf(key));
        } else {
            if (map.size() == capacity) {
                int firstKey = list.removeFirst();
                map.remove(firstKey);
            }
        }
        map.put(key, value);
        list.addLast(key);
    }

    public static void main(String[] args) {
        LRUCache cache = new LRUCache(2);

        cache.put(1, 1);
        cache.put(2, 2);
        System.out.println(cache.get(1)); // returns 1
        cache.put(3, 3); // evicts key 2
        System.out.println(cache.get(2)); // returns -1 (not found)
        cache.put(1, 4); // updates key 1
        System.out.println(cache.get(1)); // returns 4
    }
}