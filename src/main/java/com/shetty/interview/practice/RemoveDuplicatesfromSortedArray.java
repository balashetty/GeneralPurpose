package com.shetty.interview.practice;

import java.util.Arrays;

/**
 * Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
 * such that each unique element appears only once. The relative order of the elements should be kept the same.
 *  Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they 
were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
 * 
 */
public class RemoveDuplicatesfromSortedArray {

	public static void main(String[] args) {
		RemoveDuplicatesfromSortedArray solution = new RemoveDuplicatesfromSortedArray();
		int[] nums = {0,0,1,1,1,2,2,3,3,4 };
		int expected = 5;
		System.out.println(String.format("Input arr=%s", Arrays.toString(nums)));
		int actual = solution.removeDuplicates(nums);
		System.out.println(String.format("Should be %d, actaul %d and the nums=%s", expected, actual, Arrays.toString(nums)));
	}

	public int removeDuplicates(int[] nums) {
		int wp=1;
		
		for (int rp=1; rp < nums.length; rp++) {
			if (nums[rp -1] != nums[rp]) {
				nums[wp] = nums[rp];
				wp++;
			}
		}
		
		return wp;
	}
}
