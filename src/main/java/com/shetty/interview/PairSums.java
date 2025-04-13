package com.shetty.interview;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class PairSums {

//	public static void main(String[] args) {
//	new PairSums().run();
//	}

public static void findPair(int A[], int sum) {
		
		Map<Integer, Integer> map = new HashMap<>();
		
		for(int i = 0; i< A.length; i++) {
			
			//if complement is already in map, print the pair
			if(map.containsKey(sum-A[i])) {
				System.out.println("Pair found at " + map.get(sum-A[i]) + " and " + i);
			}
			
			map.put(A[i], i);
			
		}//end of for
		
	}//end for function
	

	public static void main(String[] args) {
		int ar[] = {3, 20, 5, 6,1,9, 7, 22};
		int sum = 29;
//		  int[] ar = {1, 5, 3, 3, 3};
//		    int sum = 6;
		    int res = numberOfWays(ar, sum);
		    System.out.println("Pairs expected 4,  actual " + res);
	}
	
	
	static int numberOfWays(int[] arr, int k) {
		
		int res = 0;
	
		for(int i = 0; i< arr.length-1; i++) {
			
			//loop until the last element
			for(int j = i+1; j < arr.length; j++) {
				
				//if given sum is found, print the indexes
				if(arr[i] + arr[j] == k) {
					System.out.println("Pair found at " + arr[i] + " and " + arr[j]);
					res++;
				}
			}
		}
		
//		Map<Integer, Integer> counts = new HashMap<>();
		
//		for (int num: arr) {
//			counts.put(num, counts.getOrDefault(num, 0) + 1);
//		}
//
//
//		for (int num: arr) {
//			
//			int complement = k - num;
//
//			Integer count = counts.get(complement);
//			
//			if (count != null && count > 0) {
//				System.out.println("Pair found: (" + num + ", " + complement + ")");
//				res++;
//				//counts.put(num, counts.getOrDefault(num, 0) - 1);
//				//counts.put(complement, counts.getOrDefault(complement, 0) - 1);
//			}
//			
//			counts.put(num, counts.getOrDefault(num, 0) + 1);
//		}
//		
		
//
//        for (int i = 0; i < nums.length; i++) {
//            int complement = target - nums[i];
//            if (numMap.containsKey(complement)) {
//				System.out.println("Pair found: (" + nums[i] + ", " + complement + ")");
//				res++;
//            }
//            numMap.put(nums[i], i);
//        }
//        
		return res;
	}











		  // These are the tests we use to determine if the solution is correct.
		  // You can add your own at the bottom.
		  int test_case_number = 1;
		  
		  void check(int expected, int output) {
		    boolean result = (expected == output);
		    char rightTick = '\u2713';
		    char wrongTick = '\u2717';
		    if (result) {
		      System.out.println(rightTick + " Test #" + test_case_number);
		    }
		    else {
		      System.out.print(wrongTick + " Test #" + test_case_number + ": Expected ");
		      printInteger(expected); 
		      System.out.print(" Your output: ");
		      printInteger(output);
		      System.out.println();
		    }
		    test_case_number++;
		  }
		  
		  void printInteger(int n) {
		    System.out.print("[" + n + "]");
		  }
		  
		  public void run() {
		    int k_1 = 6;
		    int[] arr_1 = {1, 2, 3, 4, 3};
		    int expected_1 = 2;
		    int output_1 = numberOfWays(arr_1, k_1);
		    check(expected_1, output_1);

		    int k_2 = 6;
		    int[] arr_2 = {1, 5, 3, 3, 3};
		    int expected_2 = 4;
		    int output_2 = numberOfWays(arr_2, k_2);
		    check(expected_2, output_2);

		    // Add your own test cases here
//			  int[] arr = {1, 2, 3, 4, 5, 6};
//		        int target = 7;
//				  int[] arr = {1, 5, 3, 3, 3};
//			        int target = 6;
//		        System.out.println(Arrays.toString(arr) + ", target:" + target);
//		        System.out.println("\nHash Set Approach:");
//		        findPairsHashSet(arr, target);
		  }
		  
		  public static void findPairsHashSet(int[] arr, int target) {
		        HashSet<Integer> set = new HashSet<>();
		        for (int num : arr) {
		            int complement = target - num;
		            if (set.contains(complement)) {
		                System.out.println("Pair found: (" + num + ", " + complement + ")");
		            }
		            set.add(num);
		        }
		    }
		

}
