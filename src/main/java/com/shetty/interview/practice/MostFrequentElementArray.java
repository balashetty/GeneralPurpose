package com.shetty.interview.practice;

import java.util.HashMap;
import java.util.Map;

public class MostFrequentElementArray {

	public static void main(String[] args) {
		MostFrequentElementArray solution = new MostFrequentElementArray();
		int[] arr = {1, 2, 3, 3};
	    System.out.println(" Output: 3: solution:" + solution.findMostFrequent(arr)); 
		int[] arr1 = {1, 2, 3};
	    System.out.println(" Output: 1: solution:" + solution.findMostFrequent(arr1)); 
		int[] arr2 = {1, 2, 4, 23, 4, 2, 2};
	    System.out.println(" Output: 2: solution:" + solution.findMostFrequent(arr2)); 

	}

	int findMostFrequent(int[] nums) {
		Map<Integer, Integer> freq = new HashMap<>();
		int mostFrequent=nums[0];
		int maxFrequentCount=0;
		
		for (int num: nums) {
			Integer count = freq.put(num, freq.getOrDefault(num, 0) + 1);
			
			if (count != null && count > maxFrequentCount) {
				maxFrequentCount = count;
				mostFrequent = num;
			}
		}
		
		return mostFrequent;
	}
}

