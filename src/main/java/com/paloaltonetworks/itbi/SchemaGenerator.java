package com.paloaltonetworks.itbi;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.Charset;
import java.util.LinkedList;
import java.util.List;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

public class SchemaGenerator {

	public static void main(String[] args) throws IOException {
		File file = new File ("onetrust-producer_landing_views.csv");
		CSVParser csvParser = CSVParser.parse(file,
				Charset.defaultCharset(), CSVFormat.DEFAULT.withFirstRecordAsHeader().withIgnoreHeaderCase().withTrim());
		List<String> headers = csvParser.getHeaderNames();
		List<CSVRecord> reportRecordList = new LinkedList<CSVRecord>();
		int baseIndex = 1;
		int otherIndex = 11;
		
		
		for (CSVRecord record : csvParser) {
			String fileName = record.get(0);
			String schema = record.get(1);
			
			String baseName = "/Users/bshetty/workspace/git/onetrust-producerProducer/datasets/target/onetrust-producer_landing/views/";
			String name = "";
			
			if (fileName.contains("base")) {
				name = baseName + baseIndex++ + "-" + fileName;
			} else {
				name = baseName + otherIndex++ + "-"  + fileName;
			}
			
			FileWriter schemaFile = new FileWriter(name);
			schemaFile.write("onetrust-producer_landing\n");
			schemaFile.write("----\n");
			schemaFile.write(schema);
			schemaFile.close();
		}
		
		csvParser.close();

	}

}
