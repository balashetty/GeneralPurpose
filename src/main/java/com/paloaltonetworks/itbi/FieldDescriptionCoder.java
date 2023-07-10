package com.paloaltonetworks.itbi;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.Map;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.apache.commons.lang3.StringUtils;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONTokener;

import io.micrometer.core.instrument.util.IOUtils;

public class FieldDescriptionCoder {

	public static void main(String[] args) throws IOException, JSONException {
		File csvFile = new File(
				"/Users/bshetty/workspace/git/OneTrustProducer/datasets/target/onetrust_landing/entities_schema_data.csv");
		CSVParser csvParser = CSVParser.parse(csvFile, Charset.defaultCharset(),
				CSVFormat.DEFAULT.withFirstRecordAsHeader().withIgnoreHeaderCase().withTrim());
		Map<String, String> fieldDescriptions = new HashMap<String, String>();

		for (CSVRecord record : csvParser) {
			fieldDescriptions.put(record.get("fieldName"), record.get("Name") + ", " + record.get("description"));
			fieldDescriptions.put(record.get("fieldName") + ".id", record.get("Name")  + " ID, " + record.get("description"));
			fieldDescriptions.put(record.get("fieldName") + ".value", record.get("Name")  + " Value, " + record.get("description"));
			fieldDescriptions.put(record.get("fieldName") + ".valueKey", record.get("Name")  + " Value Key, " + record.get("description"));

		}

		File tableFile = new File(
				"/Users/bshetty/workspace/git/OneTrustProducer/datasets/target/onetrust_landing/tables/entities.json");
		String data = IOUtils.toString(new FileInputStream(tableFile));

		JSONTokener tokener = new JSONTokener(data);
		JSONArray fields = new JSONArray(tokener);

		for (Object o : fields) {
			JSONObject jo = (JSONObject) o;
			String fieldName = jo.getString("name");
			createDescription(fieldDescriptions, jo, fieldName);
		
		}

		System.out.println(fields.toString(2));
		
		PrintWriter writer = new PrintWriter(tableFile);
		writer.write(fields.toString(2));
		writer.flush();
		writer.close();
		
	}

	static void createDescription(Map<String, String> fieldDescriptions, JSONObject jo, String fieldName) {
		
		String desc = fieldDescriptions.get(fieldName);

		if (desc != null && desc.length() > 0) {
			String lenDesc = StringUtils.rightPad(desc, 30, " ").replaceAll("\"", "");
			String descritpion = String.format("Biz: %s;Tech: %s;", lenDesc, lenDesc);

			jo.put("description", descritpion);
			
			JSONArray childFields = jo.getJSONArray("fields");
			
			for (Object co : childFields) {
				JSONObject cjo = (JSONObject) co;
				createDescription(fieldDescriptions, cjo, fieldName + "." + cjo.getString("name"));
			}
		}
	}
}
