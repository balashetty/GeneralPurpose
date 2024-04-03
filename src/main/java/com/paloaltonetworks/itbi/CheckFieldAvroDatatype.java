package com.paloaltonetworks.itbi;

import java.util.List;
import java.util.AbstractMap.SimpleEntry;
import java.util.Map.Entry;

import org.apache.avro.Schema;
import org.apache.avro.Schema.Field;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CheckFieldAvroDatatype {
	private final static Logger log = LoggerFactory.getLogger(CheckFieldAvroDatatype.class);

	public static void main(String[] args) {
		Schema.Parser parser = new Schema.Parser();
		parser.setValidate(true);
		Schema schema = parser.parse("{\n"
				+ "    \"type\": \"record\",\n"
				+ "    \"name\": \"psregionmapping__c\",\n"
				+ "    \"namespace\": \"com.paloaltonetworks.sfdc.calculated\",\n"
				+ "    \"fields\": [\n"
				+ "      {\n"
				+ "        \"name\": \"id\",\n"
				+ "        \"type\": \"string\"\n"
				+ "      },\n"
				+ "      {\n"
				+ "        \"name\": \"stard__c\",\n"
				+ "        \"type\": [\n"
				+ "          \"float\",\n"
				+ "          \"null\"\n"
				+ "        ]\n"
				+ "      }\n"
				+ "    ]\n"
				+ "  }");
		log.info(schema.toString());
		
		List<Field> fieldList = schema.getFields();
		fieldList.forEach(field -> {
			String name = field.name();
			boolean isKey = ("id".equalsIgnoreCase(name)) ? true : false;
			Schema.Type type = field.schema().getType();
			int typeValue = type.compareTo(Schema.Type.UNION);
			
			if (typeValue == 0) {
				List<Schema> types = field.schema().getTypes();
				Schema.Type dataType = types.get(0).getType();
				if (types.size() == 2 && dataType == Schema.Type.NULL)
					dataType = types.get(1).getType();
				log.info("Union dataType:" + dataType.getName() + ", key:" + isKey);
			} else {
				log.info("dataType:" + type.getName() + ", key:" + isKey);
			}
		});
	}
	
}
