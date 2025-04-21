package com.shetty;

import java.util.Arrays;

public class ProductExceptSelf {

	public static void main(String[] args) {
		System.out.println(productExceptSelf(new int[] {1,3,4})); // 12-4-3
	    System.out.println(productExceptSelf(new int[] {3,1,2,6})); // 12-36-18-6
	    System.out.println(productExceptSelf(new int[] {1, 2, 3, 4, 5})); //120-60-40-30-24
	    System.out.println(productExceptSelf(new int[] {1, 2, 3, 0, 4})); //0-0-0-24-0
	    System.out.println(productExceptSelf(new int[] {1000, 10000, 100000})); //1000000000-100000000-10000000
	}

	private static String productExceptSelf(int[] is) {

		Integer[] p = new Integer[is.length];
		
		for (int i=0; i<is.length; i++) {
			p[i] = 1;
			for (int j=0; j< is.length; j++) {
				if ( i != j) {
					p[i] *= is[j];
				}
			}
		}
		return Arrays.toString(p);
	}

}
