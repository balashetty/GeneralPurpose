package com.shetty.code.practice;

import java.util.HashMap;
import java.util.LinkedList;

public class LRUCache {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	private int capacity;
	HashMap<String, String> data = new HashMap<>();
	LinkedList<String> order = new LinkedList<>();
	
	public LRUCache(int capacity) {
		this.capacity = capacity;		
	}

	public void put(String key, String value) {
		if (capacity == order.size()) {
			String keyRemoved = order.removeFirst();
			data.remove(keyRemoved);
		}
		
		data.put(key, value);
		order.addLast(key);
	}
	
	public String get(String key) {
		String value = data.get(key);
		
		if (value != null) {
			order.remove(key);
			order.addLast(key);
		}
		
		return value;
	}
}
