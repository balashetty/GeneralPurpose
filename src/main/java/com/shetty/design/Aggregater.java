package com.shetty.design;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Aggregater {

	public static void main(String[] args) {
		if (args.length < 3) {
			System.out.println ("Usage Sample: Aggregater --aggregate max 4 8 3");
			throw new RuntimeException("Invalid arguments");
		} 
		
		System.out.println ("Arguments:" + Arrays.toString(args));
		
		String funcName = args[1];
		int[] arr = new int[args.length - 2];
		
		for (int i=2; i < args.length; i++) {
			arr[i - 2] = Integer.valueOf(args[i]);
		}
		
		int res = 0;
		
		switch(funcName) {
		case "max": 
			res = max(arr);
			break;
		case "sum":
			res = sum(arr);
			break;
		default:
			System.err.println("Unknown Aggregater frunction");
			throw new RuntimeException("Invalid arguments");
		}
		
		System.out.println("Aggregater function name:" + funcName +" and result: " + res);
	}
	
	private static int sum(int[] nums) {
		int res = 0;
		
		for (int num : nums) {
			res += num;
		}
		
		return res;
	}
	
	private static int max(int[] nums) {
		int res = 0;
		
		for (int num : nums) {
			res = Math.max(num, res);
		}
		
		return res;
	}

}
