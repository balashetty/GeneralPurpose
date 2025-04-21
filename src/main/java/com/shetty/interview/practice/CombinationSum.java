package com.shetty.interview.practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given an array of distinct integers candidates and a target integer target,
 * return a list of all unique combinations of candidates where the chosen
 * numbers sum to target. You may return the combinations in any order.
 * 
 * The same number may be chosen from candidates an unlimited number of times.
 * Two combinations are unique if the frequency of at least one of the chosen
 * numbers is different.
 * 
 * The test cases are generated such that the number of unique combinations that
 * sum up to target is less than 150 combinations for the given input.
 */
public class CombinationSum {

	public static void main(String[] args) {
		CombinationSum solution = new CombinationSum();
		int[] nums = {2,3,6,7};
		int target = 7;
		System.out.println(String.format("Input %s %d ", Arrays.toString(nums), target));
		List<List<Integer>> results = solution.combinationSum(nums, target);
		System.out.println(String.format("Should be %s", results));
	}

	public List<List<Integer>> combinationSum(int[] candidates, int target) {
		List<List<Integer>> results = new ArrayList<List<Integer>>();
		List<Integer> combination = new ArrayList<Integer>();
		backtrack(candidates, target, 0, combination, results);
		return results;
	}

	void backtrack(int[] candidates, int remain, int start, List<Integer> combination, List<List<Integer>> results) {
		if (remain == 0) {
			results.add(new ArrayList<Integer>(combination));
			return;
		} else if (remain < 0) {
			return;
		}

		for (int i = start; i < candidates.length; i++) {
			combination.add(candidates[i]);
			backtrack(candidates, remain - candidates[i], i, combination, results);
			combination.removeLast();
		}
	}
}