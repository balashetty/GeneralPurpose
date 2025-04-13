package com.shetty.code;

import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {

	public static void main(String[] args) {
		ValidParentheses vp = new ValidParentheses();
	//	String s = "(((((((()"; //"()[]{}";
	//	System.out.println("isValid ? " + s + " should be false " + vp.isValid(s));

		String s = "((()(())))";
		System.out.println("isValid ? " + s + " should be true " + vp.isValid(s));
	}

	private HashMap<Character, Character> mappings;

	public ValidParentheses() {
		this.mappings = new HashMap<Character, Character>();
		this.mappings.put(')', '(');
		this.mappings.put('}', '{');
		this.mappings.put(']', '[');
	}

	public boolean isValid(String s) {
		Stack<Character> stack = new Stack<>();

		for (int i = 0; i < s.length(); i++) {
			Character c = s.charAt(i);
			
			if (this.mappings.containsKey(c)) {
				char top = stack.pop();

				if (this.mappings.get(c) != top) {
					return false;
				}
			} else if (this.mappings.containsValue(c)) {
				stack.push(c);
			}
		}

		return stack.isEmpty();
	}

	public static boolean isValid1(String s) {
		Stack<Character> stack = new Stack<>();

		for (int i = 0; i < s.length(); i++) {
			Character c = s.charAt(i);
			stack.push(c);
		}

		char prev = '\0';

		for (Character curr : stack) {
			if (!(prev == '\0')) {
				if ((prev == '(' && curr != ')') || (prev == '{' && curr != '}') || (prev == '[' && curr != ']')) {
					return false;
				}
			}

			prev = curr;
		}

		return true;
	}
}
