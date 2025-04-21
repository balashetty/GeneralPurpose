package com.shetty.interview.practice;

import java.util.Arrays;

public class FindDuplicate {

	public static void main(String[] args) {
		FindDuplicate solution = new FindDuplicate();
		//int[] nums = { 1, 2, 3, 2, 2 };
		int[] nums = { 1, 2, 3};
		int expected = 2;
		System.out.println(String.format("Input %s ", Arrays.toString(nums)));
		int actual = solution.findDuplicate1(nums);
		System.out.println(String.format("Should be %d, actaul %d", expected, actual));

	}

	// slow 1, fast 2
	// slow 2 fast 2
	// slow 3 slow2 1
	// slow 2 slow2 2
	
	public int findDuplicate1(int[] nums) {
		int slow =0;
		int fast = 0;
		
		while(true) {
			slow = nums[slow];
			fast = nums[nums[fast]];
			
			if (slow == fast ) {
				break;
			}
		}
		
		int slow2 = 0;
		
		while(true) {
			slow = nums[slow];
			slow2 = nums[slow2];
			
			if (slow == slow2) {
				return slow;
			}
		}
		
	}
	public int findDuplicate(int[] nums) {
		int slow = 0, fast = 0;
		while (true) {
			slow = nums[slow];
			fast = nums[nums[fast]];
			if (slow == fast) {
				break;
			}
		}

		int slow2 = 0;
		while (true) {
			slow = nums[slow];
			slow2 = nums[slow2];
			if (slow == slow2) {
				return slow;
			}
		}
	}

}
