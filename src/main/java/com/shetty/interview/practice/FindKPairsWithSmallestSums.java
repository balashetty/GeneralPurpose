package com.shetty.interview.practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.stream.IntStream;

/**
 * You are given two integer arrays nums1 and nums2 sorted in non-decreasing
 * order and an integer k.
 * 
 * Define a pair (u, v) which consists of one element from the first array and
 * one element from the second array.
 * 
 * Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
 * 
 */
public class FindKPairsWithSmallestSums {

	public static void main(String[] args) {
		FindKPairsWithSmallestSums solution = new FindKPairsWithSmallestSums();

		int[] nums1 = {1,7,11};
		int[] nums2 = {2,4,6};
		System.out.println(Arrays.toString(nums1) + "," + Arrays.toString(nums2));
		List<List<Integer>>  res = solution.kSmallestPairs(nums1, nums2, 3);
		System.out.println("Expected: [[1,2],[1,4],[1,6]], Output:" + res.toString());
		
		int[] nums3 = {1,1,2};
		int[] nums4 = {1,2,3};
		System.out.println(Arrays.toString(nums3) + "," + Arrays.toString(nums4));
		List<List<Integer>>  res1 = solution.kSmallestPairs(nums3, nums4, 2);
		System.out.println("Expected: [[1,1],[1,1]], Output:" + res1.toString());

		int[] nums5 = { 1, 2, 4, 5, 6 };
		int[] nums6 = { 3, 5, 7, 9 };
		System.out.println(Arrays.toString(nums5) + "," + Arrays.toString(nums6));
		List<List<Integer>> res2 = solution.kSmallestPairs(nums5, nums6, 3);
		System.out.println("Expected: [[[1,3],[2,3],[1,5]], Output:" + res2.toString());

		int[] nums7 = { 1,2,4,5,6 };
		int[] nums8 = { 3,5,7,9 };
		System.out.println(Arrays.toString(nums7) + "," + Arrays.toString(nums8));
		List<List<Integer>> res3 = solution.kSmallestPairs(nums7, nums8, 20);
		System.out.println("Output:" + res3.toString());
	}

	//    the value 0 if x == y; a value less than 0 if x < y; and a value greater than 0 if x > y

	Comparator<int[]> comparator = new Comparator<int[]>() {
		@Override
		public int compare(int[] a, int[] b) {
			int as = a[0] + a[1];
			int bs = b[0] + b[1];
			return Integer.compare(as, bs);
		}
	};

	public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
		List<List<Integer>> smallestSumPairs = new ArrayList<List<Integer>>();

		PriorityQueue<int[]> pq = new PriorityQueue<>(comparator);

		for (int i = 0; i < nums1.length; i++) {
			for (int j = 0; j < nums2.length; j++) {
				pq.offer(new int[] { nums1[i], nums2[j] });
			}
		}

		while (k-- > 0 && !pq.isEmpty()) {
			int[] pair = pq.poll();

			smallestSumPairs.add(IntStream.of(pair).boxed().toList());
		}

		return smallestSumPairs;
	}
}
