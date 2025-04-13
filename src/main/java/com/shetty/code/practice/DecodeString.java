package com.shetty.code.practice;

import java.util.Stack;
import java.util.StringJoiner;

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
	
				
	String decodeStringx(String s) {
		Stack<Integer> countStack = new Stack<>();
		Stack<StringBuilder> stringStack = new Stack<>();
		StringBuilder currentString = new StringBuilder();
		
		int k = 0;
		for (char ch : s.toCharArray()) {
			if (Character.isDigit(ch)) {
				k = k * 10 + ch; // - '0';
			} else if (ch == '[') {
				// push the number k to countStack
				countStack.push(k);
				// push the currentString to stringStack
				stringStack.push(currentString);
				// reset currentString and k
				currentString = new StringBuilder();
				k = 0;
			} else if (ch == ']') {
				StringBuilder decodedString = stringStack.pop();
				// decode currentK[currentString] by appending currentString k times
				for (int currentK = countStack.pop(); currentK > 0; currentK--) {
					decodedString.append(currentString);
				}
				currentString = decodedString;
			} else {
				currentString.append(ch);
			}
		}
		return currentString.toString();

	}

	public String decodeString3s(String s) {
		int[] index = { 0 };
		return decodeString(s, index);
	}

	public String decodeString(String s, int[] index) {
		StringBuilder result = new StringBuilder();
		while (index[0] < s.length() && s.charAt(index[0]) != ']') {
			if (!Character.isDigit(s.charAt(index[0])))
				result.append(s.charAt(index[0]++));
			else {
				int k = 0;
				// build k while next character is a digit
				while (index[0] < s.length() && Character.isDigit(s.charAt(index[0])))
					k = k * 10 + s.charAt(index[0]++) - '0';
				// ignore the opening bracket '['
				index[0]++;
				String decodedString = decodeString(s, index);
				// ignore the closing bracket ']'
				index[0]++;
				// build k[decodedString] and append to the result
				while (k-- > 0)
					result.append(decodedString);
			}
		}
		return new String(result);
	}

	public String decodeString2(String s) {
		Stack<String> stack = new Stack<>();
		StringBuffer stringToRepeat = new StringBuffer();
		StringBuffer howManyTimes = new StringBuffer();

		boolean isInRepeat = false;

		for (int i = 0; i < s.length(); i++) {
			char curr = s.charAt(i);

			if (Character.isDigit(curr)) {
				howManyTimes.append(curr);

				if (!stringToRepeat.isEmpty()) {
					stack.push(stringToRepeat.toString());
					stringToRepeat = new StringBuffer();
				}

			} else if (curr == '[') {
				isInRepeat = true;
			} else if (curr == ']' && isInRepeat) {
				StringBuffer decodedStr = new StringBuffer();
				int repeat = Integer.parseInt(howManyTimes.toString());
				String append = stringToRepeat.toString();

				while (repeat > 0) {
					decodedStr.append(append);
					repeat--;
				}

				stack.push(decodedStr.toString());

				howManyTimes = new StringBuffer();
				stringToRepeat = new StringBuffer();
				isInRepeat = false;
			} else if (Character.isLetter(curr)) {
				stringToRepeat.append(curr);
			}
		}

		if (!stringToRepeat.isEmpty()) {
			stack.push(stringToRepeat.toString());
		}

		// StringBuffer res = new StringBuffer();
		StringJoiner joiner = new StringJoiner("");

		for (String element : stack) {
			joiner.add(element);
		}

		return joiner.toString();
	}
}
