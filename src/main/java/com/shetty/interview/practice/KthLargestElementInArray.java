package com.shetty.interview.practice;

import java.util.Arrays;
import java.util.Random;

public class KthLargestElementInArray {

	public static void main(String[] args) {
		KthLargestElementInArray solution = new KthLargestElementInArray();

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

	private void swap(int[] nums, int i, int j) {
		int temp = nums[i];
		nums[i] = nums[j];
		nums[j] = temp;
	}

	private int partition(int[] nums, int left, int right) {
		Random random = new Random();
		int pivotIndex = left + random.nextInt(right - left);
		int pivot = nums[pivotIndex];
		swap(nums, pivotIndex, right);
        // when we find an element less than pivot_value, move it left of pivot_index and increment the swap position
		int i = left;
		
		for (int j=left; j < right; j++) {
			if (nums[j] > pivot) {
				swap(nums, i, j);
				i++;
			}
		}
		
		// move pivot to its final place
		swap(nums, right, i);
		return i;
	}
	
	/**
	 * 
	 * Each element less than the pivot in the array are mocved to the left
	 * Each element more than the pivot in the array are mocved to the right
	 * After each step in the partition, pivot elements remains in the  correct position
	 * If the pivot  element index is greater than the index k -1 then partiion in the left sid
	 * If the pivot element index is less  than the index k -1 then partiion in the right side
	 * In this iteration if the pivot element index equal to k-1 then return the return the pivot elemtn itself
	 */
	private int quickSelect(int[] nums, int left, int right, int kthIndex) {
		if (left == right) {
			return nums[kthIndex];
		}
		
		int pivotIndex = partition(nums, left, right);
		
		if (pivotIndex > kthIndex) {
			return quickSelect(nums, left, pivotIndex - 1, kthIndex);
		} else if (pivotIndex < kthIndex) {
			return quickSelect(nums, pivotIndex + 1, right, kthIndex);
		} else {
			return nums[kthIndex];
		}
	}

	public int findKthLargest(int[] nums, int k) {
		return quickSelect(nums, 0, nums.length - 1, k-1);
	}
}