package com.shetty.code.practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ThreeSum {

	public static void main(String[] args) {
		ThreeSum solution = new ThreeSum();
		int[] nums = {-1,0,1,2,-1,-4};
		int[][] array = {{-1,-1,2},{-1,0,1}};
		List<List<Integer>> expected = solution.convertToList(array);
		List<List<Integer>> actual = solution.threeSum(nums);
		System.out.println("Nums:" + Arrays.toString(nums) + " three sum "
				 + " expected " + expected + " actual " + actual); 

		int[] nums1 =  {0,1,1};
		int[][] array1 = {{}};
		List<List<Integer>> expected1 = solution.convertToList(array1);
		List<List<Integer>> actual1 = solution.threeSum(nums1);
		System.out.println("Nums:" + Arrays.toString(nums1) + " three sum "
				 + " expected " + expected1 + " actual " + actual1); 

	}
	
	public  List<List<Integer>> convertToList(int[][] array) {
        return Arrays.stream(array)
                .map(row -> Arrays.stream(row)
                        .boxed()
                        .collect(Collectors.toList()))
                .collect(Collectors.toList());
    }
	
	public List<List<Integer>> threeSum(int[] nums) {
		Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
       
        for (int i=0; i< nums.length && nums[i] <= 0; i++) {
        	if (i == 0 || nums[i -1] != nums[i]) {
        		twoSum(nums, i, res);
        	}
        }
        
        return res;
	}

	public List<List<Integer>> threeSum1(int[] nums) {
	        Arrays.sort(nums);
	        List<List<Integer>> res = new ArrayList<>();
	        for (int i = 0; i < nums.length && nums[i] <= 0; ++i) 
	        	if (
	            i == 0 || nums[i - 1] != nums[i]
	        ) {
	            twoSumII(nums, i, res);
	        }
	        return res;
	    }

	void twoSumII(int[] nums, int i, List<List<Integer>> res) {
		int lo = i + 1, hi = nums.length - 1;
		while (lo < hi) {
			int sum = nums[i] + nums[lo] + nums[hi];
			if (sum < 0) {
				++lo;
			} else if (sum > 0) {
				--hi;
			} else {
				res.add(Arrays.asList(nums[i], nums[lo++], nums[hi--]));
				while (lo < hi && nums[lo] == nums[lo - 1])
					++lo;
			}
		}
	}
	
	void twoSum(int [] nums, int i, List<List<Integer>> res) {
		int low = 0;
		int high = nums.length - 1;
		
		while (low < high) {
			int sum = nums[i] + nums[low] + nums[high];
			
			if (sum < 0) {
				low++;
			} else if (sum > 0) {
				high--;
			} else {
				res.add(Arrays.asList(nums[i], nums[low++], nums[high--]));
				
				while (low < high && nums[low++] == nums[low -1]) {
					low++;
				}
			}
		}
	}
}
