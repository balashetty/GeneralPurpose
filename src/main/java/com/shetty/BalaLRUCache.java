package com.shetty;

import java.util.HashMap;
import java.util.LinkedList;

public class BalaLRUCache<K, V> {
	private HashMap<K, V> data = new HashMap<K, V>();
	private LinkedList<K> order = new LinkedList<K>();
	int capacity;
	
	public BalaLRUCache(int capacity) {
		this.capacity = capacity;
	}
	
	public void put(K key, V value) {
		if (order.size() >= capacity) {
			K keyRemoved = order.removeLast();
			data.remove(keyRemoved);
		}
		
		order.addFirst(key);
		data.put(key, value);
	}
	
	public V get(K key) {
		V value = data.get(key);
		
		if (value != null) {
			order.remove(key);
			order.addFirst(key);
		}
			
		return value;
	}
	
	public void show() {
		System.out.println(data);
		System.out.println(order);
	}
	
	public static void main(String[] args) {
		BalaLRUCache<Integer,String> cache = new BalaLRUCache<Integer, String>(3);
		cache.put(1, "Bala");
		cache.put(2, "Shetty");
		cache.put(3, "Kanchugarabettu");
		cache.show();
		cache.put(4, "Java");
		cache.show();
	}

}
