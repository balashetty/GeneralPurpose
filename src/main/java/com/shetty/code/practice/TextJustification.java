package com.shetty.code.practice;

import java.util.LinkedList;
import java.util.List;

/**
 * Given an array of strings words and a width maxWidth, format the text such that each line has exactly 
 * maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces
 ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line
 does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

 */
public class TextJustification {
	public static void main(String[] args) {
		TextJustification solution = new TextJustification();
		String[] words = {"This", "is", "an", "example", "of", "text", "justification."};
		int maxWidth = 16;
		List<String> expected = List.of( "This    is    an",
				    "example  of text", 
				    "justification.  ");
		List<String> actual = solution.fullJustify(words, maxWidth);
		System.out.println(String.format("Expected %s, actual %s, is equal %s", expected, actual, expected.equals(actual)));
	}
	
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> lines = new LinkedList<String>();
        
        StringBuilder line = new StringBuilder();
        
        for (String word : words) {
        	if (word.length() < maxWidth) {
        		lines.add(word.toString());
        	} else if (word.length() > maxWidth) {
        	    int lastIndex = 0;
        	    
        	    while(word.length() > maxWidth) {
        	    	line.append(word.substring(lastIndex, maxWidth - line.length()));
        	    	lines.add(line.toString());
        	    	lastIndex = lastIndex + maxWidth;
        	    	word = word.substring(lastIndex);
        	    }
        	    
        	    if (word.length() > 0 ) {
        	    	line = new StringBuilder(word);
        	    }
        	}
        }
        
        return lines;
    }

}
