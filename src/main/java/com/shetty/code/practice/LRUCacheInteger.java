package com.shetty.code.practice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class LRUCacheInteger {

	public static void main(String[] args) {
		System.out.println("[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]");

	    List<Integer> sourceList = Arrays.asList(1, 2, 3, 4, 5);
	    System.out.println("first:" + sourceList.getFirst() + ", last:" + sourceList.getLast());
	    Integer[] targetArray = sourceList.toArray(new Integer[0]);
		
	   // [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
	    		
		LRUCacheInteger cache = new LRUCacheInteger(2);
//		cache.put(1, 1);
//		cache.put(2, 2);
//		System.out.println(cache.get(1));
//		cache.put(3, 3);
//		System.out.println(cache.get(2));
//		cache.put(4, 4);
//		System.out.println(cache.get(1));
//		System.out.println(cache.get(3));
//		System.out.println(cache.get(4));
//		
		
		System.out.println(cache.get(2));

		cache.put(2, 6);
		System.out.println(cache.get(1));

		cache.put(1, 5);
		cache.put(1, 2);
		System.out.println(cache.get(1));
		System.out.println(cache.get(2));
	}
	
	private int capacity;
	Map<Integer, Integer> data = new HashMap<>();
	List<Integer> order = new LinkedList<>();
	
	public LRUCacheInteger(int capacity) {
		this.capacity = capacity;		
	}
	
	public void put(int key, int value) {
		if (order.contains(key)) {
			order.remove(Integer.valueOf(key));
		} else if (capacity == order.size()) {
			Integer keyRemoved = order.removeFirst();
			data.remove(keyRemoved);
		}
		
		data.put(key, value);
		order.addLast(key);
	}
	
	public int get(int key) {
		Integer value = data.get(key);
		
		if (value != null) {
			order.remove(Integer.valueOf(key));
			order.addLast(key);
			
			return value;
		} 
		
		return -1;
	}
}
