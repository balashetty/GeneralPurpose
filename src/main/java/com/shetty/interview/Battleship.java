package com.shetty.interview;

public class Battleship {

	public static void main(String[] args) {
		int R = 2;
		int C = 3;
		int[][] G = { { 0, 0, 1 }, { 1, 0, 1 } };
		Battleship battleship = new Battleship();
		double actual = battleship.getHitProbability(R, C, G);
		double expected = 0.5;
		System.out.println(String.format("Should be %f, actaul %f", expected, actual));
		
		int R1 = 2;
		int C1 = 2;
		int[][] G1 = {{1, 1},{1, 1}};
		double actual1 = battleship.getHitProbability(R1, C1, G1);
		double expected1 = 1.0;
		System.out.println(String.format("Should be %f, actaul %f", expected1, actual1));

	}

	public double getHitProbability1(int R, int C, int[][] G) {
		int totalCells = R * C;
		double battleShipCount = 0;

		for (int row = 0; row < R; row++) {
			for (int col = 0; col < C; col++) {
				if (G[row][col] == 1) {
					battleShipCount++;
				}
			}
		}

		return battleShipCount / totalCells;

	}

	public double getHitProbability2(int R, int C, int[][] G) {
		int totalCells = R * C;

		double battleShipCount = 0;

		for (int row = 0; row < R; row++) {
			int colLow = 0;
			int colHigh = C - 1;

			while (colLow <= colHigh) {
				if (G[row][colLow] == 1) {
					battleShipCount++;
				}

				if ((colLow != colHigh) && G[row][colHigh] == 1) {
					battleShipCount++;
				}
				colLow++;
				colHigh--;
			}
		}

		return battleShipCount / totalCells;
	}

	public double getHitProbability(int R, int C, int[][] G) {
		int totalCells = G.length * G[0].length;

		int rowLow = 0;
		int rowHigh = G.length - 1;
		double battleShipCount = 0;

		while (rowLow <= rowHigh) {
			int colLow = 0;
			int colHigh = G[0].length - 1;

			while (colLow <= colHigh) {
				if (G[rowLow][colLow] == 1) {
					battleShipCount++;
				}
				if ((colLow != colHigh) && G[rowLow][colHigh] == 1) {
					battleShipCount++;
				}
				if (G[rowHigh][colLow] == 1) {
					battleShipCount++;
				}
				if ((colLow != colHigh) && G[rowHigh][colHigh] == 1) {
					battleShipCount++;
				}
				colLow++;
				colHigh--;
			}
			rowLow++;
			rowHigh--;
		}

		return battleShipCount / totalCells;
	}
}
