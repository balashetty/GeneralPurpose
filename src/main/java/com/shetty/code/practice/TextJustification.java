package com.shetty.code.practice;

import java.util.LinkedList;
import java.util.List;

public class TextJustification {

	/*
	 * Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
	 */
	public static void main(String[] args) {
		
	}
	
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> lines = new LinkedList<String>();
        
        StringBuilder line = new StringBuilder();
        
        for (String word : words) {
        	if (word.length() < maxWidth) {
        		
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
