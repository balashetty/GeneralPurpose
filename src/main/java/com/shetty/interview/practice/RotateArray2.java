package com.shetty.interview.practice;

import java.util.Arrays;

public class RotateArray2 {

	public static void main(String[] args) {
		RotateArray2 solution = new RotateArray2();
		int[] nums = { 1, 2, 3, 4, 5, 6, 7 };
		int k = 2;
		System.out.println(String.format("Input %s %d ", Arrays.toString(nums), k));
		solution.rotate(nums, k);
		System.out.println(String.format("Should be %s", Arrays.toString(nums)));

//		int[] nums1 = { 3, 2, 3, 1, 2, 4, 5, 5, 6 };
//		int k1 = 4;
//		int expected1 = 4;
//		System.out.println(String.format("Input %s %d ", Arrays.toString(nums1), k1));
//		int actual1 = solution.findKthLargest(nums1, k1);
//		System.out.println(String.format("Should be %d, actaul %d", expected1, actual1));

	}

	//rotate 1 steps to the right: [7,1,2,3,4,5,6]
	//rotate 2 steps to the right: [6,7,1,2,3,4,5]
	//rotate 3 steps to the right: [5,6,7,1,2,3,4]
	public void rotate(int[] nums, int k) {
		while (k-- > 0) {
			int last = nums[nums.length - 1];

			for (int p = nums.length - 1; p > 0 ; p--) {
				nums[p] = nums[p - 1];
			}
			nums[0] = last;
		}
	}
	
	
}
