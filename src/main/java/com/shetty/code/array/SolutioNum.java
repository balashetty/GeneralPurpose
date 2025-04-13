package com.shetty.code.array;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class SolutioNum {

	public static void main(String[] args) {
		SolutioNum nunmSolution = new SolutioNum();
		//int [] arr = {1, 2, 3, 3, 4, 5, 6};
		//int [] arr = {1,1,2};
		int arr[] = {0,0,1,1,1,2,2,3,3,4};

		System.out.println("before:" + Arrays.toString(arr));
		int howMany = nunmSolution.removeDuplicates(arr);
		System.out.println("after: " + Arrays.toString(arr));
		System.out.println(Arrays.toString(Arrays.copyOfRange(arr, 0, howMany))
				+ " unique num length :" + howMany);
	}

	/**
	 * Write a function to determine whether duplicate elements in each array are
	 * within a given distance of each other in java
	 */

	public boolean checkDuplicatesWithinDistance(int[] nums, int k) {
		Map<Integer, Integer> elementIndexMap = new HashMap<>();

		for (int i = 0; i < nums.length; i++) {
			if (elementIndexMap.containsKey(nums[i])) {
				if (i - elementIndexMap.get(nums[i]) <= k) {
					return true; // Duplicate found within distance k
				}
			}
			elementIndexMap.put(nums[i], i); // Update the index of the current element
		}
		return false; // No duplicate elements found within distance k
	}
	
	
    public int[] maxOfSubarrays(int[] arr, int k) {
    	if (arr == null || arr.length ==0 || k ==0 || k > arr.length) {
    		return new int[0];
    	}
    	
    	int[] res = new int[arr.length - k + 1];
    	
    	for (int i=0 ; i < arr.length; i++) {
    		int max = arr[i];
    		
    		for (int j=1; j< k; j++) {
    			int cur = arr[i + j];
    			
    			if (cur > max) {
    				max = cur;
    			}
    		}
    		res[i] = max;
    	}
    	
    	return res;
    }

	 /**
     * Given an array of integers, find the maximum for every contiguous subarray of size k.
     *
     * @param arr The input array.
     * @param k The size of the subarray.
     * @return An array containing the maximum of each subarray.
     */
    public int[] maxOfSubarrays1(int[] arr, int k) {
        if (arr == null || arr.length == 0 || k <= 0 || k > arr.length) {
            return new int[0];
        }

        int[] result = new int[arr.length - k + 1];
        for (int i = 0; i <= arr.length - k; i++) {
            int max = arr[i];
            for (int j = 1; j < k; j++) {
                if (arr[i + j] > max) {
                    max = arr[i + j];
                }
            }
            result[i] = max;
        }
        return result;
    }
   
    
	 public int removeDuplicates(int[] nums) {
	        int insertIndex = 1;

	        for (int i=1; i < nums.length; i++) {
	            if (nums[i -1] != nums[i]) {
	                nums[insertIndex] = nums[i];
	                insertIndex++;
	            }
	        }

	        return insertIndex;
	    }
	 
    public boolean checkDuplicatesWithinK(int[] nums, int k) {
    	HashMap<Integer, Integer> dists = new HashMap<>();
    	
    	for (int i=0; i < nums.length; i++) {
    		int num = nums[i];
    		
    		if (dists.containsKey(num)) {
    			if (i - dists.get(num) <= k) {
    				return true;
    			}
    		}
    		
    		dists.put(num, i);
    	}
    	
    	return false;
    }
    
    
}
