package com.shetty.interview.practice;

import java.util.Arrays;

public class KthElementInArray2 {

	public static void main(String[] args) {
		KthElementInArray2 solution = new KthElementInArray2();
		System.out.println((0 + 2) >> 1);
		
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

	private int partition(int[] nums, int left, int right) {
		int mid = (left + right) >> 1;
		swap(nums, mid, left + 1);

		if (nums[left] < nums[right])
			swap(nums, left, right);
		if (nums[left + 1] < nums[right])
			swap(nums, left + 1, right);
		if (nums[left] < nums[left + 1])
			swap(nums, left, left + 1);

		int pivot = nums[left + 1];
		int i = left + 1;
		int j = right;

		while (true) {
			while (nums[++i] > pivot)
				;
			while (nums[--j] < pivot)
				;
			if (i > j)
				break;
			swap(nums, i, j);
		}

		nums[left + 1] = nums[j];
		nums[j] = pivot;
		return j;
	}

	private void swap(int[] nums, int i, int j) {
		int temp = nums[i];
		nums[i] = nums[j];
		nums[j] = temp;
	}

	private int quickSelect(int[] nums, int k) {
		int left = 0;
		int right = nums.length - 1;
		
		while (true) {
			if (right <= left + 1) {
				if (right == left + 1 && nums[right] > nums[left])
					swap(nums, left, right);
				return nums[k];
			}

			int j = partition(nums, left, right);

			if (j > k) {
				right = j - 1;
			} else if (j < k) {
				left = j + 1;
			} else {
				return nums[k];
			}
		}
	}

	public int findKthLargest(int[] nums, int k) {
		return quickSelect(nums, k - 1);
	}

}
