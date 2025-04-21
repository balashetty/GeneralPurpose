package com.shetty.interview.practice;

import java.util.Arrays;

public class MinimumSizeSubarraySum {

	public static void main(String[] args) {
		MinimumSizeSubarraySum solution = new MinimumSizeSubarraySum();
		int[] nums = { 2,3,1,2,4,3 };
		int target = 7;
		int expected = 2;
		System.out.println(String.format("Input %s ", Arrays.toString(nums)));
		int actual = solution.minSubArrayLen(target, nums);
		System.out.println(String.format("Should be %s, actaul %s is %s", expected, actual, expected == actual));
	}

	public int minSubArrayLen(int target, int[] nums) {
		int left = 0;
		int sumOfCurrentWindow = 0;
		int length = Integer.MAX_VALUE;

		for (int right = 0; right < nums.length; right++) {
			sumOfCurrentWindow += nums[right];

			while (sumOfCurrentWindow >= target) {
				length = Math.min(length, right - left + 1);
				sumOfCurrentWindow -= nums[left];
				left++;
			}
		}

		return length == Integer.MAX_VALUE ? 0 : length;
	}
}
