package com.shetty.interview.practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
 */
public class Combinations {

	public static void main(String[] args) {
		Combinations solution = new Combinations();
		int n = 4;
		int k = 2;
		System.out.println(String.format("Input %d %d ",n, k));
		List<List<Integer>> result = solution.combine(n, k);
		System.out.println(String.format("Should be %s", result));

	}

	
    public List<List<Integer>> combine(int n, int k) {
    	List<List<Integer>> result = new ArrayList<>();
    	backtrack(n, k, 1, new ArrayList<>(), result);
    	return result;
    }
    
    private void backtrack(int n, int k, int start, List<Integer> combination, List<List<Integer>> result) {
    	if (combination.size() == k) {
    		result.add(new ArrayList<>(combination));
            return;
    	}
    	
    	for (int i = start; i <= n; i++) {
    		combination.add(i);
    		backtrack(n, k, i + 1, combination, result);
    		combination.remove(combination.size() - 1);
    	}
    }
    
}
