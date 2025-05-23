package com.shetty.interview.practice;

import java.util.Arrays;

/**
 * You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
 *  and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
 To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
  and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 */
public class MergeSortedArray {

	public static void main(String[] args) {
		MergeSortedArray solution = new MergeSortedArray();
		int[] nums1 = { 1,2,3,0,0,0 };
		int m = 3;
		int[] nums2 = { 2,5,6 };
		int n = 3;
		int[] expected = { 1,2,2,3,5,6 };
		System.out.println(String.format("Input arr1=%s m=%d,arr2=%s m=%d", Arrays.toString(nums1), m, Arrays.toString(nums2), n));
		solution.merge(nums1, m, nums2, n);
		System.out.println(String.format("Should be %s, actaul %s",  Arrays.toString(expected),  Arrays.toString(nums1)));
	}
	
	// Can you come up with an algorithm that runs in O(m + n) time?
	// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
	// Output: [1,2,2,3,5,6]
	public void merge(int[] nums1, int m, int[] nums2, int n) {
		int p1 = m - 1;
		int p2 = n - 1;
		
		for (int p = m + n - 1; p >= 0; p--) {
			if (p2 < 0) {
				break;
			}
			
			if (p1 >= 0 && nums1[p1] > nums2[p2]) {
				nums1[p] = nums1[p1--];
			} else {
				nums1[p] = nums2[p2--];
			}
		}
	}
}