package com.shetty;

import java.util.HashMap;
import java.util.Map;

public class ListNodeLRUCache {

	public static void main(String[] args) {
		ListNodeLRUCache cache = new ListNodeLRUCache(3);
		cache.put(1, 1);
		cache.put(2, 2);
		cache.put(3, 3);
		cache.show();
		cache.put(4, 4);
		cache.show();
	}

	int capacity;
	Map<Integer, ListNode> dic;
	ListNode head;
	ListNode tail;

	public ListNodeLRUCache(int capacity) {
		this.capacity = capacity;
		dic = new HashMap<>();
		head = new ListNode(-1, -1);
		tail = new ListNode(-1, -1);
		head.next = tail;
		tail.prev = head;
	}

	public void show() {
		for (Map.Entry<Integer, ListNode> e : dic.entrySet()) {
			System.out.println("key:" + e.getKey() + ", value:" + e.getValue());
		}
	}
	
	public int get(int key) {
		if (!dic.containsKey(key)) {
			return -1;
		}

		ListNode node = dic.get(key);
		remove(node);
		add(node);
		return node.val;
	}

	public void put(int key, int value) {
		if (dic.containsKey(key)) {
			ListNode oldNode = dic.get(key);
			remove(oldNode);
		}

		ListNode node = new ListNode(key, value);
		dic.put(key, node);
		add(node);

		if (dic.size() > capacity) {
			ListNode nodeToDelete = head.next;
			remove(nodeToDelete);
			dic.remove(nodeToDelete.key);
		}
	}

	public void add(ListNode node) {
		ListNode previousEnd = tail.prev;
		previousEnd.next = node;
		node.prev = previousEnd;
		node.next = tail;
		tail.prev = node;
	}

	public void remove(ListNode node) {
		node.prev.next = node.next;
		node.next.prev = node.prev;
	}
}

class ListNode {
	int key;
	int val;
	ListNode next;
	ListNode prev;

	public ListNode(int key, int val) {
		this.key = key;
		this.val = val;
	}

	@Override
	public String toString() {
		return "ListNode [key=" + key + ", val=" + val + "]";
	}
}
