package com.shetty.interview.practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
 */
public class Permutations {

	public static void main(String[] args) {
		Permutations solution = new Permutations();
		int[] nums = {1,2,3};
		System.out.println(String.format("Input %s ", Arrays.toString(nums)));
		List<List<Integer>> result = solution.permute(nums);
		System.out.println(String.format("Should be %s", result));
	}

	
	 public List<List<Integer>> permute(int[] nums) {
	        List<List<Integer>> ans = new ArrayList<>();
	        backtrack(new ArrayList<>(), ans, nums);
	        return ans;
	    }

	    public void backtrack(
	        List<Integer> curr,
	        List<List<Integer>> ans,
	        int[] nums
	    ) {
	        if (curr.size() == nums.length) {
	            ans.add(new ArrayList<>(curr));
	            return;
	        }

	        for (int num : nums) {
	            if (!curr.contains(num)) {
	                curr.add(num);
	                backtrack(curr, ans, nums);
	                curr.remove(curr.size() - 1);
	            }
	        }
	    }
}
