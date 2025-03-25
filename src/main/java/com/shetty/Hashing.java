package com.shetty;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Hashing {
	 public static class ListNode {
	        int val;
	        ListNode next;
	        ListNode (int val) {
	            this.val = val;
	        }
	    }
	 
	public static void main(String[] args) {
//		int[] arr1 = {1,2,3};
//		System.out.println(String.format("%d, %d", 2, countElements(arr1)));
//		
//		int[] arr = {1,1,3,3,5,5,7,7};
//		System.out.println(String.format("%d, %d", 0, countElements(arr)));
//		
//		String s = "eceba";
//		int k = 2;
//		System.out.println(String.format("%d, %d", 3, findLongestSubstring(s, k)));
		
		//int[][] nums = {{3,1,2,4,5,6},{1,2,3,4,6},{3,4,5,6}};
//		int[][] nums = {{0,1,2,7,5},{1,2,3,4},{3,4,5}};
//		System.out.println(String.format("intersection : %s, %s", "[]", intersection(nums).toString()));
		
		ListNode n1 = new ListNode(1);
		ListNode n2 = new ListNode(2);
		ListNode n3 = new ListNode(3);
		ListNode n4 = new ListNode(4);
		ListNode n5 = new ListNode(5);
		n1.next = n2;
		n2.next = n3;
		n3.next = n4;
		n4.next = n5;
		System.out.println(String.format("findNode : %s, %s", "4", findNode(n1, 2).val));
	}

	static ListNode findNode(ListNode head, int k) {
		ListNode fast = head;
		ListNode slow = head;
		
		for (int i=0; i < k; i++) {
			fast = fast.next;
		}
		
		while (fast != null) {
			slow = slow.next;
			fast = fast.next;
		}
		
		return slow;
	}
	
	public static List<Integer> intersection(int[][] nums) {
		Map<Integer, Integer> counts = new HashMap<> ();
		
		for (int[] num : nums) {
			for (int i : num) {
				counts.put(i, counts.getOrDefault(i, 0) + 1);
			}
		}
		
		int n = nums.length;
		List<Integer> res = new ArrayList<>();
		
		for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
			if (entry.getValue() == n) {
				res.add(entry.getKey());
			}
		}
		
		Collections.sort(res);
		
		return res;
	}
	
	public static int findLongestSubstring(String s, int k) {
		int res = 0;
		char left = 0;
		Map<Character, Integer> counts = new HashMap<>();
		
		for (int right = 0; right < s.length(); right++) {
			char c = s.charAt(right);
			counts.put(c, counts.getOrDefault(c, 0) + 1);
			
			if (counts.size() > k) {
				char toRemove = s.charAt(left);
				counts.put(c, counts.getOrDefault(c, 0) - 1);
				
				if (counts.get(toRemove) == 0) {
					counts.remove(toRemove);
				}
				
				left++;
			}
			
			res = Math.max(res, right - left + 1);
		}
		
		return res;
	}
	
	 public static int countElements(int[] arr) {
	        Set<Integer> numSet = new HashSet<Integer>();

	        for (int num: arr) {
	            numSet.add(num);
	        }
	        
	        int count = 0;
	        
	        for (int i=0 ; i < arr.length; i++) {
	            int j = arr[i]+1;
	            
	            if (numSet.contains(j)) {
	                count++;
	            }
	        }

	        return count;
	    }
	 
	 public boolean checkIfPangram(String sentence) {
	        Set<Character> chars = new HashSet<Character>();
	        
	        for (char c : sentence.toCharArray()) {
	            chars.add(c);
	           
	            if (chars.size() == 26) {
	                break;
	            }
	        }
	        
	        for (char c = 97; c <= 122; c++) {
	           if (!chars.contains(c)) {
	               return false;
	           }
	        }
	  
	        return true;
	    }
}
