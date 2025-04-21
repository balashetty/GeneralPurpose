package com.shetty.interview.practice;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class TopKFrequentElements {

	public static void main(String[] args) {
		TopKFrequentElements solution = new TopKFrequentElements();
		int[] nums = { 1,1,1,2,2,3 };
		int k = 2;
		int[] expected = {1,2};
		System.out.println(String.format("Input %s %s ", Arrays.toString(nums), k));
		int[] actual = solution.topKFrequent(nums, k);
		System.out.println(String.format("Should be %s, actaul %s", Arrays.toString(expected), Arrays.toString(actual)));
		
	}
	
	Comparator<int[]> comparator = new Comparator<int[]>() {
		@Override
		public int compare(int[] a, int[] b) {
			return Integer.compare(b[1], a[1]);
		}
	};

	public int[] topKFrequent(int[] nums, int k) {
		HashMap<Integer, Integer> counts = new HashMap<>();
		
		for (int num : nums) {
			counts.put(num,  counts.getOrDefault(num, 0) + 1);
		}
		
		PriorityQueue<int[]> pq = new PriorityQueue<int[]>(comparator);
		
		for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
			pq.add(new int[]{entry.getKey(), entry.getValue()});
		}
		
		int[] res = new int[k];

		for (int i=0; i< k && !pq.isEmpty(); i++) {
			int[] value = pq.poll();
			res[i] = value[0];
		}
		
		return res;
	}
}