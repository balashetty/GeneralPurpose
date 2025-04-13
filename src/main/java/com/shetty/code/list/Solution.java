package com.shetty.code.list;

import java.util.HashMap;
import java.util.Map;

public class Solution {

	public static void main(String[] args) {

		 
	}

	static ListNode reverseLinkedList(ListNode head) {
		ListNode prev = null;
		ListNode curr = head;
		
		while (curr != null) {
			ListNode nextNode = curr.next;
			curr.next = prev;
			prev = curr;
			curr = nextNode;
		}
		
		return prev;
	}
	
	static void showLinkedList(ListNode head) {
		ListNode curr = head;
		
		while (curr != null) {
			System.out.print(curr.data + ",");
			curr = curr.next;
		}
		System.out.println();
		
	}

}
