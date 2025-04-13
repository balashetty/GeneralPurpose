package com.shetty.interview;

import java.util.Arrays;

public class Cafeteria {

	public static void main(String[] args) {
		Cafeteria solution = new Cafeteria();

		int N = 10;
		int K = 1;
		int M = 2;
		long[] S = { 2, 6 };
		long expected = 3;
		System.out.println(String.format("Input N %d, K %d M %d S " + Arrays.toString(S), N, K, M));
		long actual = solution.getMaxAdditionalDinersCount(N, K, M, S);
		System.out.println(String.format("Should be %d, actaul %d", expected, actual));

		int N1 = 15;
		int K1 = 2;
		int M1 = 3;
		long[] S1 = { 11, 6, 14 };
		long expected1 = 1;

		System.out.println(String.format("Input N %d, K %d M %d S " + Arrays.toString(S1), N1, K1, M1));
		long actual1 = solution.getMaxAdditionalDinersCount(N1, K1, M1, S1);
		System.out.println(String.format("Should be %d, actaul %d", expected1, actual1));

	}
	// 1 - 10, 2, 6,  1
	// 1 = 1 + 1, 
	// 2 = 1 + 2 + 3  - 4  - 1
	// 6 = 5 + 6 + 7 - 8 9 10 1 1 
	public long getMaxAdditionalDinersCount(long N, long K, int M, long[] S) {
		
		return -1;
	}
	
	public long getMaxAdditionalDinersCount1(long N, long K, int M, long[] S) {

		long minSeats = K + 1;
		if (M == 0) {
			return N / minSeats + 1;
		}

		Arrays.sort(S);
		long result = 0L;

		long firstChair = S[0];
		long firstAvailableIndex = (firstChair - 1) - minSeats;
		if (firstAvailableIndex >= 0) {
			result += firstAvailableIndex / minSeats + 1;
		}

		for (int index = 0; index < M - 1; index++) {

			long leftFreeChair = S[index] + minSeats;
			long rightFreeChair = S[index + 1] - minSeats;
			long diffSpace = rightFreeChair - leftFreeChair;
			if (diffSpace >= 0) {
				result += diffSpace / minSeats + 1;
			}
		}

		long lastChair = S[M - 1];
		long lastAvailableIndex = (lastChair - 1) + minSeats;
		if (lastAvailableIndex <= N - 1) {
			result += (N - 1 - lastAvailableIndex) / minSeats + 1;
		}

		return result;
	}
}
