package com.shetty.interview.practice;

import java.util.Arrays;

public class KthElementInArray1 {

	public static void main(String[] args) {
		KthElementInArray1 solution = new KthElementInArray1();
		int[] nums = { 3, 2, 1, 5, 6, 4 };
		int k = 2;
		int expected = 5;
		System.out.println(String.format("Input %s %d ", Arrays.toString(nums), k));
		int actual = solution.findKthLargest(nums, k);
		System.out.println(String.format("Should be %d, actaul %d", expected, actual));

		int[] nums1 = { 3, 2, 3, 1, 2, 4, 5, 5, 6 };
		int k1 = 4;
		int expected1 = 4;
		System.out.println(String.format("Input %s %d ", Arrays.toString(nums1), k1));
		int actual1 = solution.findKthLargest(nums1, k1);
		System.out.println(String.format("Should be %d, actaul %d", expected1, actual1));

	}

	public int findKthLargest(int[] nums, int k) {
		k = nums.length - k;

		return quickSelect(nums, 0, nums.length - 1, k);
	}

	private int quickSelect(int[] nums, int left, int right, int k) {
		int pivot = nums[right];
		int p = left;

		for (int i = left; i < right; i++) {
			if (nums[i] <= pivot) {
				int temp = nums[p];
				nums[p] = nums[i];
				nums[i] = temp;
				p++;
			}
		}

		int temp = nums[p];
		nums[p] = nums[right];
		nums[right] = temp;

		if (p > k) {
			return quickSelect(nums, left, p - 1, k);
		} else if (p < k) {
			return quickSelect(nums, p + 1, right, k);
		} else {
			return nums[p];
		}
	}

	public int findSecondLargest(int[] nums, int k) {
		int[] largest = { Integer.MIN_VALUE, Integer.MIN_VALUE };
		int n = nums.length;

		for (int i = 0; i < n; i++) {
			int curr = nums[i];

			if (curr > largest[0]) {
				largest[1] = largest[0];
				largest[0] = curr;
			} else if (curr > largest[1]) {
				largest[1] = curr;
			}

			System.out.println(Arrays.toString(largest));
		}

		return largest[1];
	}

}
