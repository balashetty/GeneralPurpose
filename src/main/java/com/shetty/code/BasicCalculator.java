package com.shetty.code;

import java.util.Stack;

public class BasicCalculator {

	public static void main(String[] args) {
		BasicCalculator bc = new BasicCalculator();
		String s = "5-3+7*2-6/3";
		System.out.println("14=" + bc.calculate(s));
		s = "2*(5+5*2)/3+(6/2+8)";
		System.out.println("21=" + bc.calculate(s));
		s = "5 - 3+7*  2-6/   3";
		System.out.println("14=" + bc.calculate(s));
	}

	private int calculate(char operator, int x, int y) {
		if (operator == '+') {
			return x;
		} else if (operator == '-') {
			return -x;
		} else if (operator == '*') {
			return x * y;
		} else if (operator == '/') {
			return x / y;
		} else {
			System.err.println("Invalid operator " + operator + " for x=" + x + ", y=" + y);
			throw new RuntimeException("Invalid operator " + operator + " for x=" + x + ", y=" + y);
		}
	}

	private int calculate(String s, int[] i) {
		Stack<Integer> stack = new Stack<>();
		int curr = 0;
		char prevOper = '+';

		while (i[0] < s.length()) {
			char c = s.charAt(i[0]);
			
			if (c == '(') {
				i[0]++;
				curr = calculate(s, i);
			} else if (Character.isDigit(c)) {
				curr = curr * 10 + Character.getNumericValue(c);
			} else {
				if (prevOper == '*' || prevOper == '/') {
					stack.push(calculate(prevOper, stack.pop(), curr));
				} else {
					stack.push(calculate(prevOper, curr, 0));
				}

				if (c == ')') {
					break;
				}
				
				curr = 0;
				prevOper = c;
			}

			i[0]++;
		}

		int ans = 0;
		
		for (int num : stack) {
			ans += num;
		}

		return ans;
	}

	public int calculate(String s) {
		s = s.replaceAll("\\s+", "") + "@";
		int[] i = new int[1];
		return calculate(s, i);
	}
}
