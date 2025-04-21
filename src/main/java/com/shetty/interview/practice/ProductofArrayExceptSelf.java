package com.shetty.interview.practice;

import java.util.Arrays;

/**
 * Given an integer array nums, return an array answer such that answer[i] is equal to the 
 * product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


 */
public class ProductofArrayExceptSelf {

	public static void main(String[] args) {
		ProductofArrayExceptSelf solution = new ProductofArrayExceptSelf();
		int[] nums = {1,2,3,4};
		int[] expected = {24,12,8,6};
		System.out.println(String.format("Input arr=%s", Arrays.toString(nums)));
		int[] actual = solution.productExceptSelf(nums);
		System.out.println(
				String.format("Should be %s, actaul %s", Arrays.toString(expected), Arrays.toString(actual)));

	}

	 public int[] productExceptSelf(int[] nums) {
		 int n = nums.length;
		 int products[] = new int[n];
		 
		 products[0] = 1;
		 
		 for (int i = 1; i < n; i++) {
			 products[i] = products[i - 1] * nums[i - 1];
		 }
		 
		 int rp = 1;
		 
		 for (int i = n - 2; i >= 0; i--) {
			 rp  *= nums[i + 1];
			 products[i] = rp;
		 }
		 
		 return products;
	 }
	 
	 public int[] productExceptSelfn2(int[] nums) {
		 int n = nums.length;
		 int products[] = new int[n];
		 
		 for (int i = 0; i < n; i++) {
			 int prod = 1;
			 
			 for (int j = 0; j < n; j++) {
				 if ( i != j) {
					 prod *= nums[j];
				 }
			 }
			 
			 products[i] = prod; 
		 }
		 return products;
	 }

    public int[] productExceptSelf1(int[] nums) {
        // The length of the input array
        int length = nums.length;

        // Final answer array to be returned
        int[] answer = new int[length];

        // answer[i] contains the product of all the elements to the left
        // Note: for the element at index '0', there are no elements to the left,
        // so the answer[0] would be 1
        answer[0] = 1;
        for (int i = 1; i < length; i++) {
            // answer[i - 1] already contains the product of elements to the left of 'i - 1'
            // Simply multiplying it with nums[i - 1] would give the product of all
            // elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1];
        }

        // R contains the product of all the elements to the right
        // Note: for the element at index 'length - 1', there are no elements to the right,
        // so the R would be 1
        int R = 1;
        for (int i = length - 1; i >= 0; i--) {
            // For the index 'i', R would contain the
            // product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R;
            R *= nums[i];
        }

        return answer;
    }

	 public int[] productExceptSelf2(int[] nums) {
	        int[] products = new int[nums.length];
	        
	        int productOfAll = 1;
	        
	        for (int num : nums) {
	        	productOfAll *= num;
	        }
	        
	        for (int p = 0; p < nums.length; p++) {
	        	products[p] = productOfAll / nums[p];
	        }
	        
	        return products;
	 }
}
