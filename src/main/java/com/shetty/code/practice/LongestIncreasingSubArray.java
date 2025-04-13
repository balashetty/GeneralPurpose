package com.shetty.code.practice;

import java.util.Arrays;

public class LongestIncreasingSubArray {

	public static void main(String[] args) {
		LongestIncreasingSubArray s = new LongestIncreasingSubArray();
		int nums[] =  {10,9,2,5,3,7,101,18};
	//	int nums[] = {0,1,0,3,2,3};
	//	int nums[] = {7,7,7,7,7,7,7};
		System.out.println(Arrays.toString(nums));
		System.out.println("LongestIncreasingSubArray:" + s.lengthOfLIS(nums));
	}

	public int lengthOfLIS1(int[] nums) {
		int[] dp = new int[nums.length];
		Arrays.fill(dp, 1);

		for (int i = 1; i < nums.length; i++) {
			for (int j = 0; j < i; j++) {
				if (nums[i] > nums[j]) {
					dp[i] = Math.max(dp[i], dp[j] + 1);
				}
			}
		}

		int longest = 0;

		for (int curr : dp) {
			longest = Math.max(longest, curr);
		}

		return longest;
	}
	
	public int lengthOfLIS(int[] nums) {
		int dp[] = new int[nums.length];
		Arrays.fill(dp,  1);
		
		for (int i=1; i < nums.length; i++) {
			for (int j=0; j < i; j++) {
				if (nums[i] > nums[j]) {
					dp[i] = Math.max(dp[i], dp[j] + 1);
				}
			}
		}
		
		int longest = 0;
		
		for (int curr : dp) {
			longest = Math.max(longest, curr);
		}
		
		return longest;
	}
	
}
