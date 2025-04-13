package com.shetty.code.practice;

import java.util.Arrays;

public class SearchMatrix {

	public static void main(String[] args) {
		SearchMatrix solution = new SearchMatrix();
		int [][] matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
		int target = 3;
		boolean expexted = true;
		boolean actual = solution.searchMatrix(matrix, target);
		System.out.println("Matrix:" + Arrays.deepToString(matrix) + " seatch for "
				+ target + " expected " + expexted + " actual " + actual); 
		
		int [][] matrix1 = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
		int target1 = 13;
		boolean expexted1 = false;
		boolean actual1 = solution.searchMatrix(matrix1, target1);
		System.out.println("Matrix:" + Arrays.deepToString(matrix1) + " seatch for "
				+ target1 + " expected " + expexted1 + " actual " + actual1); 
	}
	
	public boolean searchMatrix(int[][] matrix, int target) {
        for (int i=0; i < matrix.length; i++) {
        	int low = matrix[i][0];
        	int high = matrix[i][matrix[i].length - 1];
        	
        	if (target >= low && target <= high) {
                for (int j=0; j < matrix[i].length; j++) {
                	if (matrix[i][j] == target) {
                		return true;
                	}
                }
        	}
        }
		
		return false;
    }

}
