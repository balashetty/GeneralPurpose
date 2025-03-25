package com.shetty;

public class Sample {

	public static void main(String[] args) {
		System.out.println(letterCapitalize("heLLo wOrLd")); //Hello World
	    System.out.println(letterCapitalize("i rAn thEre")); //I Ran There
	}

	private static String letterCapitalize(String string) {
		char [] chars = string.toCharArray();
		
		boolean isNewWord = true;
		
		for (int i=0; i < chars.length; i++) {
			if (Character.isSpaceChar(chars[i])) {
				isNewWord = true;
				continue;
			}
				
			if (isNewWord) {
				chars[i] = Character.toUpperCase(chars[i]); // or ask add
				isNewWord = false;
			} else {
				chars[i] = Character.toLowerCase(chars[i]);
			}
		}
		
		return new String(chars);
	}

}
