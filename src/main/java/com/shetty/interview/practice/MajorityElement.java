package com.shetty.interview.practice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
 You may assume that the majority element always exists in the array.
 */
public class MajorityElement {

	public static void main(String[] args) {
		MajorityElement solution = new MajorityElement();
		int[] nums = {2,2,1,1,1,2,1};
		int expected = 1;
		System.out.println(String.format("Input arr=%s", Arrays.toString(nums)));
		int actual = solution.majorityElement(nums);
		System.out.println(
				String.format("Should be %d, actaul %d and the nums=%s", expected, actual, Arrays.toString(nums)));
	}

	public int majorityElement(int[] nums) {
		HashMap<Integer, Integer> counts = new HashMap<Integer, Integer>();
		
		for (int num : nums) {
			counts.put(num, counts.getOrDefault(num, 0) + 1);
		}
		
		int n = nums.length / 2;
		int res = 0;
		
		for (Map.Entry<Integer, Integer> e : counts.entrySet()) {
			if (e.getValue() > n) {
				res = e.getKey();
				break;
			}
		}
		
		return res;
	}

}
