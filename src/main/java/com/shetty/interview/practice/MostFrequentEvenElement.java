package com.shetty.interview.practice;

import java.util.HashMap;
import java.util.Map;

public class MostFrequentEvenElement {

	public static void main(String[] args) {
		MostFrequentEvenElement solution = new MostFrequentEvenElement();
		int[] arr = {0,1,2,2,4,4,1 };
		System.out.println(" Output: 2: solution:" + solution.findMostFrequent(arr));
		int[] arr1 = {4,4,4,9,2,4 };
		System.out.println(" Output: 4: solution:" + solution.findMostFrequent(arr1));
		int[] arr2 = { 29,47,21,41,13,37,25,7 };
		System.out.println(" Output: -1: solution:" + solution.findMostFrequent(arr2));

	}

	int findMostFrequent(int[] nums) {
		Map<Integer, Integer> freq = new HashMap<>();
		int mostFrequent = -1;
		int maxFrequentCount = 0;

		for (int num : nums) {
			if (num % 2 == 0) {
				Integer count = freq.put(num, freq.getOrDefault(num, 0) + 1);

				if (count != null && count > maxFrequentCount) {
					maxFrequentCount = count;
					mostFrequent = num;
				}
			}
		}

		return mostFrequent;
	}
}
