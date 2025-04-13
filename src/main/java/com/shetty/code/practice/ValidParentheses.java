package com.shetty.code.practice;

import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {

	public static void main(String[] args) {
		ValidParentheses vp = new ValidParentheses();
		String s = "(((((((()"; //"()[]{}";
		System.out.println("isValid ? " + s + " should be false " + vp.isValid(s));

		String s1 = "(]"; 
		System.out.println("isValid ? " + s1 + " should be false " + vp.isValid(s1));
		
		String s2 = "((()(())))";
		System.out.println("isValid ? " + s2 + " should be true " + vp.isValid(s2));

	}

	public boolean isValid(String s) {
		Stack<Character> stack = new Stack<>();

		for (char curr : s.toCharArray()) {
			if (curr == '(' || curr == '{' || curr == '[') {
				stack.push(curr);
			} else if (curr == ')' || curr == '}' || curr == ']') {
				char top = stack.isEmpty() ? '\0' : stack.pop();

				if ((curr == ')' && top != '(') 
						|| (curr == '}' && top != '{')
						|| (curr == ']' && top != '[')) {
					return false;
				}
			} else {}
		}

		return stack.isEmpty();
	}
}
