package com.shetty.interview.practice;

import java.util.Arrays;

public class KthElementInArray3 {

	public static void main(String[] args) {
		KthElementInArray3 solution = new KthElementInArray3();

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
	
	//{ 3, 2, 1, | 5, 6, 4 } k=2
	private int partition2(int[] nums, int left, int right) {
		int mid = left + right >> 2;
		swap(nums, mid, left+1);
		
		if (nums[left] < nums[right]) {
			swap(nums, left, right);
		}
		
		if (nums[left + 1] < nums[right]) {
			swap(nums, left+1, right);
		}
		
		if (nums[left] < nums[left + 1]) {
			swap(nums, left, left+1);
		}
		
		int pivot = nums[left+1];
		int i=left + 1;
		int j=right;
		
		while (true) {
			while(nums[++i] > pivot);
			while(nums[--j] < pivot);
			
			if (i > j) {
				break;
			}
			swap(nums, i, j);
		}
		
		nums[left+1] = nums[j];
		nums[j] = pivot;
		return j;
	}
	
	//{ 3, 2, 1,| 5, 6, 4 }, 0 , 5
	// { 3, 2, 1,| 5, 6, 4 }
	private int partition(int[] nums, int left, int right) {
		int mid = left + right >> 2;
		swap(nums, mid, left+1);
		
		//swap first half
		if (nums[left] < nums[right]) {
			swap(nums, left, right);
		}
		if (nums[left + 1] < nums[right]) {
			swap(nums, left+1, right);
		}
		if (nums[left] < nums[left+1]) {
			swap(nums, left, left+1);
		}
		
		int pivot = nums[left+1];
		int i = left + 1;
		int j = right;
		
		//increment i,  decriment j such they pass piovot
		while (true) {
			while (nums[++i] > pivot);
			while (nums[--j] < pivot);
			
			if (i > j) {
				break;
			}
			
			swap(nums, i , j);
		}
		
		//swap pivot left+1 and j
		nums[left+1] = nums[j];
		nums[j] = pivot;
		
		return j;
	}
	
	private int partition1(int[] nums, int left, int right) {
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

	private void swap1(int[] nums, int i, int j) {
		int temp = nums[i];
		nums[i] = nums[j];
		nums[j] = temp;
	}

	// [6, 5, 4 | 3, 2 , 1], k= 1
	// j = 2, right = j-1, 2-1, 1
	// 1 <=  0 + 1 = 1
	// yes && nums[1] > nums[0], 5 > 6 false
	// return nums[k
	private int quickSelect1(int[] nums, int k) {
		int left = 0;
		int right = nums.length - 1;
		
		
		while (true) {
			if (right <= left + 1) {
				if (right == left + 1 && nums[right] > nums[left])
					swap(nums, left, right);
				return nums[k];
			}

			int j = partition1(nums, left, right);

			if (j > k) {
				right = j - 1;
			} else if (j < k) {
				left = j + 1;
			} else {
				return nums[k];
			}
		}
	}

	private int quickSelect(int[] nums, int k) {
		int left = 0;
		int right = nums.length - 1;
		
		while (true) {
			if (right <= left+1) {
				if (right == left+1 && nums[right] > nums[left]) {
					swap(nums, left+1, right);
				}
				return nums[k];
			}
			
			int j = this.partition(nums, left, right);
			
			if (j >= k) {
				right = j - 1;
			} else if (j <= k) {
				left = j + 1;
			}
		}
	}
	
	public int findKthLargest(int[] nums, int k) {
		return quickSelect(nums, k - 1);
	}
	
	public int findKthLargest1(int[] nums, int k) {
		return quickSelect1(nums, k - 1);
	}

}
