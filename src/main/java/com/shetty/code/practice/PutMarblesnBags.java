package com.shetty.code.practice;

import java.util.Arrays;

public class PutMarblesnBags {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	 public long putMarbles(int[] weights, int k) {
	        int [] pairWeights = new int[weights.length - 1];

	        for (int i =0; i < weights.length - 1; i++) {
	            pairWeights[i] = weights[i] + weights[i + 1];
	        }

	        Arrays.sort(pairWeights, 0, weights.length - 1);

	        long res = 0;

	        for (int i=0; i < k - 1; i++) {
	            res += pairWeights[weights.length - 2 - i] - pairWeights[i];
	        }

	        return res;
	    }

}
