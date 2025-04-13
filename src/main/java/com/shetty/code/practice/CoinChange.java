package com.shetty.code.practice;

import java.util.Arrays;

public class CoinChange {

	public static void main(String[] args) {
		CoinChange solution = new CoinChange();
		int [] coins = {1,2,5};
		int amount = 11;
		int expexted = 3;
		int actual = solution.coinChange(coins, amount);
		System.out.println("Matrix:" + Arrays.toString(coins) + " seatch for no coins to make amount "
				+ amount + " expected " + expexted + " actual " + actual); 
		int [] coins1 = {2};
		int amount1 = 3;
		int expexted1 = -1;
		int actual1 = solution.coinChange(coins1, amount1);
		System.out.println("Matrix:" + Arrays.toString(coins1) + " seatch for no coins to make amount "
				+ amount1 + " expected " + expexted1 + " actual " + actual1); 
	}
/*
	Step 1: Define dp[i]
			dp[i] represents the minimum number of coins required to make the amount i.
			Step 2: Initialization
			dp[0] = 0 → It takes 0 coins to make amount 0.

			Fill the dp array with a large value (amount + 1), as we want to find the minimum.

			Step 3: Transition Formula
			For each amount i, check all possible coin denominations:

			If i - coin is non-negative (i ≥ coin), update dp[i]:
			dp[i]=min(dp[i],dp[i−coin]+1)

			This means:

			If we don't take the coin, dp[i] remains the same.

			If we take the coin, we add 1 coin to dp[i - coin].

			Step 4: Final Answer
			If dp[amount] is still the large value (amount + 1), return -1 (no valid solution).

			Otherwise, return dp[amount].
*/
	 
	public int coinChange(int[] coins, int amount) {
		int max = amount + 1;
		int[] dp = new int[max];
		Arrays.fill(dp, max);
		
		dp[0] = 0;
		
		for (int currAmount=1 ; currAmount <= amount; currAmount++) {
			 for(int coin : coins) {
				 if (currAmount - coin >= 0) {
					dp[currAmount] = Math.min(dp[currAmount], dp[currAmount - coin] + 1);
				 }
			}
		}
		
		int numberOfCoins = dp[amount];
		
		return numberOfCoins > amount ? -1 : numberOfCoins;
	}
}
