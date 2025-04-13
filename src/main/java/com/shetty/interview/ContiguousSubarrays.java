package com.shetty.interview;

/*
 * Contiguous Subarrays
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
1. The value at index i must be the maximum element in the contiguous subarrays, and
2. These contiguous subarrays must either start from or end on index i.

Signature
int[] countSubarrays(int[] arr)
Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) at index 0 with the maximum value in the subarray being 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]
 */
public class ContiguousSubarrays {

	public static void main(String[] args) {
		ContiguousSubarrays cs = new ContiguousSubarrays();
		 int[] array = {3, 4, 1, 6, 2};
	    // printContiguousSubarrays(array);

//		int [] res = cs.countSubarrays(array);
//		System.out.println(Arrays.toString(array));
//		System.out.println(Arrays.toString(res));
		 
		 cs.run();
	}

	public  void printContiguousSubarrays(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                System.out.print("[");
                for (int k = i; k <= j; k++) {
                    System.out.print(arr[k]);
                    if (k < j) {
                        System.out.print(", ");
                    }
                }
                System.out.println("]");
            }
        }
    }
	

	 int[] countSubarrays(int[] arr) {
		int n = arr.length;
		int[] res = new int[n];
		
		
		for (int i=0; i < n; i++) {
			int left = 0;
			int right = 0;
			
			for (int j= i -1; j >= 0; j--) {
				if (arr[j] < arr[i]) {
					left++;
				} else {
					break;
				}
			}
			
			for (int k= i+1; k < n; k++) {
				if (arr[k] < arr[i]) {
					right++;
				} else {
					break;
				}
			}
			
			res[i] = ( left + right + 1);
		}
		
		return res;
	}

	// These are the tests we use to determine if the solution is correct.
	  // You can add your own at the bottom.
	  int test_case_number = 1;
	  void check(int[] expected, int[] output) {
	    int expected_size = expected.length; 
	    int output_size = output.length; 
	    boolean result = true; 
	    if (expected_size != output_size) {
	      result = false;
	    }
	    for (int i = 0; i < Math.min(expected_size, output_size); i++) {
	      result &= (output[i] == expected[i]);
	    }
	    char rightTick = '\u2713';
	    char wrongTick = '\u2717';
	    if (result) {
	      System.out.println(rightTick + " Test #" + test_case_number);  
	    }
	    else {
	      System.out.print(wrongTick + " Test #" + test_case_number + ": Expected ");
	      printIntegerArray(expected); 
	      System.out.print(" Your output: ");
	      printIntegerArray(output);
	      System.out.println();
	    }
	    test_case_number++;
	  }
	  void printIntegerArray(int[] arr) {
	    int len = arr.length; 
	    System.out.print("[");
	    for(int i = 0; i < len; i++) {
	      if (i != 0) {
	        System.out.print(", ");
	      }
	      System.out.print(arr[i]);
	    }
	    System.out.print("]");
	  }
	  public void run() {
	    int[] test_1 = {3, 4, 1, 6, 2};
	    int[] expected_1 = {1, 3, 1, 5, 1};
	    int[] output_1 = countSubarrays(test_1);
	    check(expected_1, output_1);
	    
	    int[] test_2 = {2, 4, 7, 1, 5, 3};
	    int[] expected_2 = {1, 2, 6, 1, 3, 1};
	    int[] output_2 = countSubarrays(test_2);
	    check(expected_2, output_2);
	  
	    // Add your own test cases here
	    
	  }
	
}
