package com.shetty.interview.practice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Given an array of integers nums, return the length of the longest consecutive
 * sequence of elements that can be formed.
 * 
 * A consecutive sequence is a sequence of elements in which each element is
 * exactly 1 greater than the previous element. The elements do not have to be
 * consecutive in the original array.
 * 
 * You must write an algorithm that runs in O(n) time.
 */
public class LongestConsecutiveSequence {

	public static void main(String[] args) {
		LongestConsecutiveSequence solution = new LongestConsecutiveSequence();
		int[] nums = { 100,4,200,1,3,2 };
		int expected = 4;
		System.out.println(String.format("Input %s ", Arrays.toString(nums)));
		int actual = solution.longestConsecutive(nums);
		System.out.println(String.format("Should be %s, actaul %s", expected, actual));
	}

	
	public int longestConsecutive(int[] nums) {
		Set<Integer> numSet = new HashSet<>();
		
		for (int num : nums) {
			numSet.add(num);
		}
		
		int longest = 0;
		
		for (int num : numSet) {
			if (!numSet.contains(num - 1)) {
				int length = 1;
				
				while (numSet.contains(num  + length)) {
					length++;
				}
				
				longest = Math.max(length, longest);
			}
		}
		
		return longest;
	}
	
	public int longestConsecutive1(int[] nums) {
		Set<Integer> numSet = new HashSet<>();
		for (int num : nums) {
			numSet.add(num);
		}
		int longest = 0;

		for (int num : numSet) {
			if (!numSet.contains(num - 1)) {
				int length = 1;
				while (numSet.contains(num + length)) {
					length++;
				}
				longest = Math.max(longest, length);
			}
		}
		return longest;
	}
	
	public int longestConsecutiveMap(int[] nums) {
        Map<Integer, Integer> mp = new HashMap<>();
        int res = 0;

        for (int num : nums) {
            if (!mp.containsKey(num)) {
                mp.put(num, mp.getOrDefault(num - 1, 0) + mp.getOrDefault(num + 1, 0) + 1);
                mp.put(num - mp.getOrDefault(num - 1, 0), mp.get(num));
                mp.put(num + mp.getOrDefault(num + 1, 0), mp.get(num));
                res = Math.max(res, mp.get(num));
            }
        }
        return res;
    }

}
