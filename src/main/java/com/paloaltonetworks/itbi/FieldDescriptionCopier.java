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

public class FieldDescriptionCopier {

	public static void main(String[] args) throws IOException, JSONException {
		
		
//		File csvFile = new File(
//				"/Users/bshetty/workspace/git/OneTrustProducer/datasets/target/onetrust_landing/vendors_custom_fields.csv");
//		CSVParser csvParser = CSVParser.parse(csvFile, Charset.defaultCharset(),
//				CSVFormat.DEFAULT.withFirstRecordAsHeader().withIgnoreHeaderCase().withTrim());
		Map<String, String> customFieldNames = new HashMap<String, String>();

		
//		for (CSVRecord record : csvParser) {
//			String fieldName = record.get("fieldName");
//			String name = record.get("name");
//			String fl = name.substring(0, 1).toLowerCase();
//			name = fl + name.substring(1).replaceAll(" ", "");
//			customFieldNames.put(fieldName, name);
//		}
		
		
		File csvFile = new File(
				"/Users/bshetty/workspace/git/OneTrustProducer/datasets/target/onetrust_landing/entities_schema_data1.csv");
		CSVParser csvParser = CSVParser.parse(csvFile, Charset.defaultCharset(),
				CSVFormat.DEFAULT.withFirstRecordAsHeader().withIgnoreHeaderCase().withTrim());
		Map<String, String> fieldDescriptions = new HashMap<String, String>();

		
		for (CSVRecord record : csvParser) {
			String fieldName = record.get("fieldName");
			if (fieldName.startsWith("custom")) {
				fieldName = customFieldNames.get(fieldName);
			}
			fieldDescriptions.put(fieldName, record.get("Name") + ", " + record.get("description"));
			fieldDescriptions.put(fieldName + "_id", record.get("Name") + " ID, " + record.get("description"));
			fieldDescriptions.put(fieldName + "_value", record.get("Name") + " Value, " + record.get("description"));
			fieldDescriptions.put(fieldName + "_valueKey", record.get("Name") + " Value Key, " + record.get("description"));

		}

		File tableFile = new File(
				"/Users/bshetty/workspace/git/OneTrustProducer/datasets/target/onetrust/views/entities.json");
		String data = IOUtils.toString(new FileInputStream(tableFile));

		JSONTokener tokener = new JSONTokener(data);
		JSONArray fields = new JSONArray(tokener);

		for (Object o : fields) {
			JSONObject jo = (JSONObject) o;
			String fieldName = jo.getString("name");
			createDescription(fieldDescriptions, jo, fieldName);
		
		}

		//System.out.println(fields.toString(2));
		
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
				createDescription(fieldDescriptions, cjo, fieldName);
			}
		}
	}
}
