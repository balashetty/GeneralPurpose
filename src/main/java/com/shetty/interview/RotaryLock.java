package com.shetty.interview;

import java.util.Arrays;

public class RotaryLock {

	public static void main(String[] args) {
		RotaryLock solution = new RotaryLock();
		int N = 3;
		int M = 3;
		int[] C = { 1, 2, 3 };
		long expected = 2;
		System.out.println(String.format("Input N %d, M %d C " + Arrays.toString(C), N, M));
		long actual = solution.getMinCodeEntryTime(N, M, C);
		System.out.println(String.format("Should be %d, actaul %d", expected, actual));

		int N1 = 10;
		int M1 = 4;
		int[] C1 = { 9, 4, 4, 8 };
		long expected1 = 11;
		System.out.println(String.format("Input N %d, M %d C " + Arrays.toString(C1), N1, M1));
		long actual1 = solution.getMinCodeEntryTime(N1, M1, C1);
		System.out.println(String.format("Should be %d, actaul %d", expected1, actual1));

	}

	public long getMinCodeEntryTime(int N, int M, int[] C) {
		int codeEntryTime = rotationTime(1, C[0], N);

		for (int i = 0; i < C.length - 1; i++) {
			codeEntryTime += rotationTime(C[i], C[i + 1], N);
		}

		return codeEntryTime;
	}

	private int rotationTime(int c1, int c2, int N) {
		int distance = Math.abs(c1 - c2);
		return Math.min(distance, N - distance);
	}
}
