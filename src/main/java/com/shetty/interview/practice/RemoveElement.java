package com.shetty.interview.practice;

import java.util.Arrays;

/**
 * Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
 * The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
 The remaining elements of nums are not important as well as the size of nums.
Return k.
 */
public class RemoveElement {
					
	public static void main(String[] args) {
		RemoveElement solution = new RemoveElement();
		int[] nums = { 3,2,2,3 };
		int val = 3;
		int expected = 2;
		System.out.println(String.format("Input arr=%s  val=%d", Arrays.toString(nums), val));
		int actual = solution.removeElement(nums, val);
		System.out.println(String.format("Should be %d, actaul %d and the nums=%s", expected, actual, Arrays.toString(nums)));
	}
	
	public int removeElement(int[] nums, int val) {
		int wp = 0;
		
		for (int rp = 0; rp < nums.length; rp++) {
			if (nums[rp] != val) {
				nums[wp] = nums[rp];
				wp++;
			}
		}
		
		return wp;
	}
}
