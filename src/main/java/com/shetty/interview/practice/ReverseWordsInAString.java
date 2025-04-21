package com.shetty.interview.practice;

/**
 * Given an input string s, reverse the order of the words.
 * 
 * A word is defined as a sequence of non-space characters. The words in s will
 * be separated by at least one space.
 * 
 * Return a string of the words in reverse order concatenated by a single space.
 * 
 * Note that s may contain leading or trailing spaces or multiple spaces between
 * two words. The returned string should only have a single space separating the
 * words. Do not include any extra spaces.
 */
public class ReverseWordsInAString {

	public static void main(String[] args) {
		ReverseWordsInAString solution = new ReverseWordsInAString();
		String s = "the sky is blue";
		String expected = "blue is sky the";
		String actual = solution.reverseWords(s);
		System.out.println(String.format("Expected %s, actual %s, is equal %s", expected, actual, expected.equals(actual)));

		String s1 = "    a good   example";
		String expected1 = "example good a";
		String actual1 = solution.reverseWords(s1);
		System.out.println(String.format("Expected %s, actual %s, is equal %s", expected1, actual1, expected1.equals(actual1)));

	}

	public String reverseWords(String s) {
		s = s.trim();
		String[] words = s.split("\\s+");
		
		int left = 0;
		int right = words.length - 1;
		
		while (left < right) {
			String temp = words[left];
			words[left] = words[right];
			words[right] = temp;
			left++;
			right--;
		}
		
		return String.join(" ", words);
	}

}
