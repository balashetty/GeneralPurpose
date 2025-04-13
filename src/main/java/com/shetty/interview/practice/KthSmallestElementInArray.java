package com.shetty.interview.practice;

import java.util.Arrays;
import java.util.Random;

public class KthSmallestElementInArray {

	public static void main(String[] args) {
		KthSmallestElementInArray solution = new KthSmallestElementInArray();

		int[] nums = { 3, 2, 1, 5, 6, 4 };
		int k = 2;
		int expected = 2;
		System.out.println(String.format("Input %s %d ", Arrays.toString(nums), k));
		int actual = solution.findKthSmallest(nums, k);
		System.out.println(String.format("Should be %d, actaul %d", expected, actual));

		int[] nums1 = { 3, 2, 3, 1, 2, 4, 5, 5, 6 };
		int k1 = 4;
		int expected1 = 3;
		System.out.println(String.format("Input %s %d ", Arrays.toString(nums1), k1));
		int actual1 = solution.findKthSmallest(nums1, k1);
		System.out.println(String.format("Should be %d, actaul %d", expected1, actual1));
	}

	private void swap(int[] nums, int i, int j) {
		int temp = nums[i];
		nums[i] = nums[j];
		nums[j] = temp;
	}
	
	/**
	 * Each element less than the pivot in the array are moved to the left
	 * Each element more than the pivot in the array are moved to the right
	 * After each step in the partition, pivot elements remains in the  correct position
	 */
	
	private int partition(int[] nums, int left, int right) {
		Random random = new Random();
		int pivotIndex = left + random.nextInt(right - left);
		int pivot = nums[pivotIndex];
		swap(nums, pivotIndex, right);
        // when we find an element less than pivot_value, move it left of pivot_index and increment the swap position
		int i = left;
		
		for (int j=left; j < right; j++) {
			if (nums[j] < pivot) {
				swap(nums, i, j);
				i++;
			}
		}
		
		// move pivot to its final place
		swap(nums, right, i);
		return pivotIndex;
	}
	
	/**
	 * Left = right return the kthIndex value
	 * Partition the array using left, right and kthIndex
	 * If the pivot element index is greater than the index k -1 then partition in the left side 
	 * If the pivot element index is less than the index k -1 then partition in the right side
	 * If the pivot element index equal to k-1 then return the return the pivot element itself
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

	/**
	 * quick select with left 0 and right length-1 with kth index k - 1
	 */
	public int findKthSmallest(int[] nums, int k) {
		return quickSelect(nums, 0, nums.length - 1, k-1);
	}
}