package com.shetty.code;

import java.util.Stack;

public class DecodeString {
	public static void main(String[] args) {
		DecodeString solution = new DecodeString();
		String s = "bala2[abc]3[cd]ef"; //"3[a]2[bc]";
		String ds = solution.decodeString(s);
		String es = "balaabcabccdcdcdef"; //"accaccacc";
		System.out.println("Solution:encoded string " + s + " and decoded string " + ds + " is true? " + es.equals(ds)
				+ " should be " + es);
	}

	String decodeString(String s) {
		Stack<StringBuilder> countStack = new Stack<>();
		Stack<StringBuilder> stringStack = new Stack<>();
		StringBuilder currentString = new StringBuilder("");
		StringBuilder currentCount = new StringBuilder("");
	
		for (char curr : s.toCharArray()) {
			if (Character.isDigit(curr)) {
				currentCount.append(curr);
			} else if (Character.isLetter(curr)) {
				currentString.append(curr);
			} else if (curr == '[') {
				countStack.push(currentCount);
				stringStack.push(currentString);
				currentString = new StringBuilder();
				currentCount = new StringBuilder();;
			} else if (curr == ']') {
				StringBuilder decodedString = stringStack.pop();
				int repeat = Integer.parseInt(countStack.pop().toString());

				while (repeat > 0) {
					decodedString.append(currentString);
					repeat--;
				}
				
				currentString = decodedString;
			}			
		}
		
		return currentString.toString();
	}
}
