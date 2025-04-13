package com.shetty.interview;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class RevenueMilestones {

	public static void main(String[] args) {
		int[] revenues = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 };
		int[] milestones = { 100, 200, 500 };
		int[] result = getMilestoneDays(revenues, milestones);
		System.out.println("Output: [4, 6, 10], actual:" + Arrays.toString(result)); // Output: [4, 6, 10]

		int revenues_2[] = { 700, 800, 600, 400, 600, 700 };
		int milestones_2[] = { 3100, 2200, 800, 2100, 1000 };
		int expected_2[] = { 5, 4, 2, 3, 2 };
		int[] output_2 = getMilestoneDays(revenues_2, milestones_2);
		System.out.println("Output: [5, 4, 2, 3, 2], actual:" + Arrays.toString(result)); // Output: [4, 6, 10]

		int[] revenues2 = { 10, 20, 30, 40, 50 };
		int[] milestones2 = { 150, 300 };
		int[] result2 = getMilestoneDays(revenues2, milestones2);
		System.out.println("Output: [-1, -1], actual:" + Arrays.toString(result2)); // Output: [-1, -1]
	}

	static int[] getMilestoneDays0(int[] revenues, int[] milestones) {

		// **** initialization ****
		int[] ans = Arrays.stream(new int[milestones.length]).map(i -> -1).toArray();

		int revenue = 0;

		PriorityQueue<String> pq = new PriorityQueue<String>(new Comparator<String>() {
			public int compare(String str1, String str2) {
				String s1 = str1.substring(0, str1.indexOf(","));
				String s2 = str2.substring(0, str2.indexOf(","));
				Integer v1 = Integer.parseInt(s1);
				Integer v2 = Integer.parseInt(s2);
				if (v1 > v2)
					return 1;
				if (v1 == v2)
					return 0;
				else
					return -1;
			}
		});

		for (int i = 0; i < milestones.length; i++) {
			String s = "" + milestones[i] + "," + i;
			pq.add(s);
		}

		// **** traverse revenue array ****
		for (int r = 0; r < revenues.length; r++) {

			// **** update revenue ****
			revenue += revenues[r];

			// **** update the ans array with milestones that have been reached ****
			while (!pq.isEmpty()) {

				// **** extract milestone and index ****
				String[] strs = pq.peek().split(",");
				int milestone = Integer.parseInt(strs[0]);
				int m = Integer.parseInt(strs[1]);

				// **** check if done ****
				if (revenue < milestone)
					break;

				// **** ****
				ans[m] = (r + 1);

				// **** remove lowest value milestone ****
				pq.remove();
			}
		}

		// **** return answer ****
		return ans;
	}

	public static int[] getMilestoneDays2(int[] revenues, int[] milestones) {
		int[] milestoneDays = new int[milestones.length];
		Arrays.fill(milestoneDays, -1);
		long cumulativeRevenue = 0;
		int milestoneIndex = 0;

		for (int day = 0; day < revenues.length; day++) {
			cumulativeRevenue += revenues[day];

			while (milestoneIndex < milestones.length && cumulativeRevenue >= milestones[milestoneIndex]) {
				milestoneDays[milestoneIndex] = day + 1;
				milestoneIndex++;
			}
		}
		return milestoneDays;
	}

	int[] getMilestoneDays1(int[] revenues, int[] milestones) {
		int days[] = new int[milestones.length];
		int sum = 0;

		int milestoneIndex = 0;

		for (int i = 0; i < revenues.length && milestoneIndex < milestones.length; i++) {
			sum += revenues[i];
			System.out.println("Sum:" + sum + " cur " + revenues[i]);

			int nextMilestone = milestones[milestoneIndex];

			while (sum >= nextMilestone) {
				System.out
						.println("Milestone:" + nextMilestone + " at day " + (i + 1) + " mls index:" + milestoneIndex);
				days[milestoneIndex] = i + 1;
				milestoneIndex++;

				if (milestoneIndex == milestones.length) {
					break;
				}

				nextMilestone = milestones[milestoneIndex];
			}
		}

		System.out.println(Arrays.toString(days));

		if (milestoneIndex == 0)
			Arrays.fill(days, -1);
		return days;
	}
	
	static int[] getMilestoneDays(int[] revenues, int[] milestones) {
		int days[] = new int[milestones.length];
		int sum = 0;

		int milestoneIndex = 0;

		for (int i = 0; i < revenues.length && milestoneIndex < milestones.length; i++) {
			sum += revenues[i];

			int nextMilestone = milestones[milestoneIndex];

			while (sum >= nextMilestone) {
				days[milestoneIndex] = i + 1;
				milestoneIndex++;

				if (milestoneIndex == milestones.length) {
					break;
				}

				nextMilestone = milestones[milestoneIndex];
			}
		}

		System.out.println(Arrays.toString(days));

		if (milestoneIndex == 0)
			Arrays.fill(days, -1);
		return days;
	}

	public static int binarySearch(int[] array, int target) {
		if (array == null || array.length == 0) {
			return -1; // Handle empty or null array
		}
		Arrays.sort(array);
		int low = 0;
		int high = array.length - 1;
		int closestValue = array[0];
		int minDifference = Math.abs(array[0] - target);

		while (low <= high) {
			int mid = low + (high - low) / 2;
			int currentDifference = Math.abs(array[mid] - target);
			if (currentDifference < minDifference) {
				minDifference = currentDifference;
				closestValue = array[mid];
			}
			if (array[mid] == target) {
				return array[mid];
			} else if (array[mid] < target) {
				low = mid + 1;
			} else {
				high = mid - 1;
			}
		}
		if (high >= 0 && Math.abs(array[high] - target) < minDifference) {
			closestValue = array[high];
		}
		return closestValue;
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
		} else {
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
		for (int i = 0; i < len; i++) {
			if (i != 0) {
				System.out.print(", ");
			}
			System.out.print(arr[i]);
		}
		System.out.print("]");
	}

	public void run() {
//	    int revenues_1[] = {100, 200, 300, 400, 500};
//	    int milestones_1[] = {300, 800, 1000, 1400};
//	    int expected_1[] = {2, 4, 4, 5};
//	    int[] output_1 = getMilestoneDays(revenues_1, milestones_1);
//	    check(expected_1, output_1);

		int revenues_2[] = { 700, 800, 600, 400, 600, 700 };
		int milestones_2[] = { 3100, 2200, 800, 2100, 1000 };
		int expected_2[] = { 5, 4, 2, 3, 2 };
		int[] output_2 = getMilestoneDays(revenues_2, milestones_2);
		check(expected_2, output_2);

//	    int revenues_3[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
//	    int milestones_3[] = {100, 200, 500};
//	    int expected_3[] = {4, 6, 10};
//	    int[] output_3 = getMilestoneDays(revenues_3, milestones_3);
//	    check(expected_3, output_3);
	}

//	  public static void main(String[] args) {
//	    new RevenueMilestones().run();
//	  }

}
