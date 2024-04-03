package com.paloaltonetworks.itbi;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.commons.lang3.StringUtils;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONTokener;

import io.micrometer.core.instrument.util.IOUtils;

public class FieldDescriptionDefault {
	static Pattern WORD_FINDER = Pattern.compile("(([A-Z]?[a-z]+)|([A-Z]))");

	public static void main(String[] args) throws IOException, JSONException {
		File tableFile = new File(
				"/Users/bshetty/workspace/git/secret_fix/OneTrustProducer/datasets/target/onetrust/views/inventory_relations.json");
		String data = IOUtils.toString(new FileInputStream(tableFile));

		JSONTokener tokener = new JSONTokener(data);
		JSONArray fields = new JSONArray(tokener);

		for (Object o : fields) {
			JSONObject jo = (JSONObject) o;
			//String fieldName = jo.getString("name");
			createDescription(jo, "name" , "");
		
		}

	//	System.out.println(fields.toString(4));
		
		PrintWriter writer = new PrintWriter(tableFile);
		writer.write(fields.toString(2));
		writer.flush();
		writer.close();
		
	}

	static void createDescription(JSONObject jo, String fieldName, String parentName) {
		String name = toWords(jo.getString(fieldName));
		String desc =  parentName + name + " of the onetrust inventory relations";

		if (desc != null && desc.length() > 0) {
			String lenDesc = StringUtils.rightPad(desc, 30, " ").replaceAll("\"", "");
			String descritpion = String.format("Biz: %s;Tech: %s;", lenDesc, lenDesc);

			jo.put("description", descritpion);
			
			JSONArray childFields = jo.getJSONArray("fields");
			
			for (Object co : childFields) {
				JSONObject cjo = (JSONObject) co;
				createDescription(cjo,  "name", name + " ");
			}
		}
	}
	
	static String toWords(String text) {
	    Matcher matcher = WORD_FINDER.matcher(text);
	    StringBuilder words = new StringBuilder();
	 
	    while (matcher.find()) {
	    	if (words.length() > 0)
	    		words.append(" ");
	    	String word = matcher.group(0);
	    	words.append(word.substring(0, 1).toUpperCase() + word.substring(1));
	    }
	    
	    return words.toString();
	}
	
	static List<String> findWordsInMixedCase(String text) {
	    Matcher matcher = WORD_FINDER.matcher(text);
	    List<String> words = new ArrayList<>();
	    while (matcher.find()) {
	        words.add(matcher.group(0));
	    }
	    return words;
	}
}
