package com.paloaltonetworks.itbi;

/**
* @author gkumargaur
* Oct 7, 2022
*/
public class DescriptionValidation {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
//		try {
//			try (Stream<Path> paths = Files.walk(Paths.get("/Users/gkumargaur/workspace/java/office/test/pub-sub-to-bq-dataflow/datasets/target"))) {
//				paths.filter(Files::isRegularFile).forEach(path -> {
//					String jsonFile = path.toAbsolutePath().toString();///Users/gkumargaur/workspace/java/gitprojects/poc/gs-messaging-gcp-pubsub/src/main/resources/json/a018.json
//					System.out.println(jsonFile);
//					if(jsonFile.endsWith(".json")) {
//						ObjectMapper mapper = new ObjectMapper();
//						ArrayNode arrayNode = null;
//						try {
//							arrayNode = (ArrayNode) mapper.readTree(new File(jsonFile));
//							 if(arrayNode != null && arrayNode.isArray()) {
//								 for(JsonNode jsonNode : arrayNode) {
//									 //System.out.println(jsonNode);
//									 //System.out.println(jsonNode.get("name").asText());
//									 String bizText = jsonNode.get("description").asText().trim();
//									 bizText = bizText.substring(bizText.indexOf("Biz:")+4, bizText.indexOf(";"));
//									 if(bizText.length()<=30) {
//										 System.out.println(bizText);
//										 System.out.println(jsonNode);
//										 System.exit(0);
//									 }
//									 
//								 }
//							 }
//						 //String jsonInString = mapper.writeValueAsString(arrayNode);
//						 //System.out.println(jsonInString);
//						} catch (IOException e) {
//							e.printStackTrace();
//						}
//					}
//				});
//			} 
//			
//			
//		} catch (IOException e) {
//			e.printStackTrace();
//		}

	}

}







