package com.paloaltonetworks.itbi;

//@Service
public class SchemaRegistryService {
//	private final static Logger log = LoggerFactory.getLogger(SchemaRegistryService.class);
//
//	private RestTemplate restTemplate = new RestTemplate();
//	private Gson gson = new GsonBuilder().create();
//	private Schema.Parser schemaParser = new Schema.Parser();
//	private Constants Constants = new Constants();
//
//	public SchemaRegistryService() {
//		init();
//	}
//
//	// @EventListener(ApplicationReadyEvent.class)
//	private void init() {
//		try {
//			Constants.setKAFKA_SCHEMA_REGISTRY_URL("http://localhost:8081");
//
//			if (Constants.KAFKA_SCHEMA_REGISTRY_URL.contains("https")) {
//				SSLContext sslContext = new SSLContextBuilder()
//						.loadTrustMaterial(new File(Constants.KAFKA_TRUSTSTORE_LOCATION),
//								Constants.KAFKA_TRUSTSTORE_PASSWORD.toCharArray())
//						.build();
//				SSLConnectionSocketFactory socketFactory = new SSLConnectionSocketFactory(sslContext);
//				HttpClient httpClient1 = HttpClients.custom().setSSLSocketFactory(socketFactory).build();
//				HttpComponentsClientHttpRequestFactory factory = new HttpComponentsClientHttpRequestFactory(
//						httpClient1);
//
//				restTemplate = new RestTemplate(factory);
//			} else {
//				restTemplate = new RestTemplate();
//			}
//		} catch (Exception e) {
//			log.error("Failed to initialize SchemaRegistryService", e);
//			throw new RuntimeException(e);
//		}
//	}
//
//	public SchemaRegistryResponse process(SchemaRegistryRequest request) {
//		SchemaRegistryResponse response = null;
//
//		if (request.isGet_subject_latest_version()) {
//			response = getSubject(request);
//		} else if (request.isNew_object()) {
//			response = addSubjectObject(request);
//		} else if (request.isNew_object_fields()) {
//
//		} else if (request.isDelete_object()) {
//
//		} else if (request.isDelete_object_fields()) {
//
//		}
//
//		return response;
//
//	}
//
//	private SchemaRegistryResponse<AvroSchema> getSubject(SchemaRegistryRequest request) {
//		SchemaRegistryResponse<AvroSchema> response = new SchemaRegistryResponse<AvroSchema>();
//		StringBuilder urlBuilder = new StringBuilder(Constants.KAFKA_SCHEMA_REGISTRY_URL);
//		urlBuilder.append("/subjects/{0}/versions/latest");
//
//		ResponseEntity<String> restResponse = getRestResponse(urlBuilder.toString(), request.getSubject_name());
//
//		if (HttpUtils.isOk(restResponse)) {
//			JSONTokener tokener = new JSONTokener(restResponse.getBody());
//			JSONObject json = new JSONObject(tokener);
//			AvroSchema avroSchema = new AvroSchema();
//			avroSchema.setSchema(json.getString("schema").replace("\\", ""));
//			avroSchema.setId(json.getInt("id"));
//			avroSchema.setVersion(json.getInt("version"));
//			response.setResult(avroSchema);
//			response.setSuccess(true);
//			response.setMessage(
//					String.format("Got latest schema with id {}, version {} for subject {} from schema registry {}",
//							avroSchema.getId(), avroSchema.getVersion(), request.getSubject_name(),
//							Constants.KAFKA_SCHEMA_REGISTRY_URL));
//			log.info("Got latest schema with id {}, version {} for subject {} from schema registry {} is \n{}",
//					avroSchema.getId(), avroSchema.getVersion(), request.getSubject_name(),
//					Constants.KAFKA_SCHEMA_REGISTRY_URL, avroSchema.getSchema());
//		} else {
//			log.error("Unable to get the schema for subject {} from schema registry {}", request.getSubject_name(),
//					Constants.KAFKA_SCHEMA_REGISTRY_URL);
//			response.setError_message(
//					String.format("Unable to get the subject %s schema at schema registry %s , cause %s",
//							request.getSubject_name(), Constants.KAFKA_SCHEMA_REGISTRY_URL, restResponse.getBody()));
//		}
//
//		return response;
//	}
//
//	private SchemaRegistryResponse<AvroSchema> updateSubject(SchemaRegistryRequest request,
//			SchemaRegistryResponse<AvroSchema> response) {
//		StringBuilder urlBuilder = new StringBuilder(Constants.KAFKA_SCHEMA_REGISTRY_URL);
//		urlBuilder.append("/subjects/{0}/versions");
//
//		ResponseEntity<String> restResponse = updateRestResponse(urlBuilder.toString(),
//				response.getResult().getSchema(), request.getSubject_name());
//
//		if (HttpUtils.isOk(restResponse)) {
//			JSONTokener tokener = new JSONTokener(restResponse.getBody());
//			JSONObject json = new JSONObject(tokener);
//			AvroSchema avroSchema = response.getResult();
//			avroSchema.setId(json.getInt("id"));
//			avroSchema.setVersion(avroSchema.getVersion() + 1);
//			avroSchema.setSchema(request.getJsonSchema());
//			response.setResult(avroSchema);
//
//			log.info("Updated id {}, version {} for subject {} at schema registry {} is \n {}", avroSchema.getId(),
//					avroSchema.getVersion(), request.getSubject_name(), Constants.KAFKA_SCHEMA_REGISTRY_URL,
//					avroSchema.getSchema());
//			response.setSuccess(true);
//			response.setMessage(String.format("Updated id %s, version %s for subject %s at schema registry %s is \n %s",
//					avroSchema.getId(), avroSchema.getVersion(), request.getSubject_name(),
//					Constants.KAFKA_SCHEMA_REGISTRY_URL, avroSchema.getSchema()));
//		} else {
//			log.error("Unable updated id {}, version {} for subject {} at schema registry {} is \n {}",
//					response.getResult().getId(), response.getResult().getVersion(), request.getSubject_name(),
//					Constants.KAFKA_SCHEMA_REGISTRY_URL, response.getResult().getSchema());
//			response.setSuccess(false);
//			response.setError_message(
//					String.format("Unable updated id {}, version {} for subject {} at schema registry {}",
//							response.getResult().getId(), response.getResult().getVersion(), request.getSubject_name(),
//							Constants.KAFKA_SCHEMA_REGISTRY_URL));
//		}
//
//		return response;
//	}
//
//	private SchemaRegistryResponse addSubjectObject(SchemaRegistryRequest request) {
//		SchemaRegistryResponse<AvroSchema> response = new SchemaRegistryResponse<AvroSchema>();
//		JSONTokener schemJsonForObjectTokener = new JSONTokener(request.getJsonSchema());
//		JSONObject schemJsonForObject = new JSONObject(schemJsonForObjectTokener);
//
//		String objectType = schemJsonForObject.optString("type");
//
//		if (StringUtils.isEmpty(objectType)) {
//			objectType = "record";
//			schemJsonForObject.put("type", objectType);
//		}
//
//		String objectName = schemJsonForObject.optString("name");
//
//		if (StringUtils.isEmpty(objectName)) {
//			objectName = request.getObject_name();
//			schemJsonForObject.put("name", objectName);
//		}
//
//		String namespace = schemJsonForObject.optString("namespace");
//
//		if (StringUtils.isEmpty(namespace)) {
//			namespace = request.getNamespace();
//			schemJsonForObject.put("namespace", namespace);
//		}
//
//		JSONArray fields = schemJsonForObject.optJSONArray("fields");
//
//		if (fields == null) {
//			response.setError_message(
//					"Failed to add new object schema, invalid request for add object either specifiy the complete object as avro json or just fieds as avro json schema, this avor json input is not valid "
//							+ request.getJsonSchema());
//			return response;
//		}
//
//		response = getSubject(request);
//		AvroSchema avroSchema = response.getResult();
//		JSONTokener tokener = new JSONTokener(avroSchema.getSchema());
//		JSONArray jsonObjects = new JSONArray(tokener);
//
//		Map<String, JSONObject> jsonObjectsMap = Collections.synchronizedMap(new LinkedHashMap());
//
//		jsonObjects.forEach(new Consumer<Object>() {
//			@Override
//			public void accept(Object t) {
//				JSONObject jsonObject = (JSONObject) t;
//				jsonObjectsMap.put(jsonObject.getString("name"), jsonObject);
//			}
//		});
//
//		jsonObjectsMap.put(objectName, schemJsonForObject);
//
//		JSONObject eventJson = jsonObjectsMap.get(request.getEvent_name());
//		JSONArray eventFields = eventJson.getJSONArray("fields");
//
//		Map<String, JSONObject> eventFieldsMap = Collections.synchronizedMap(new LinkedHashMap());
//
//		eventFields.forEach(new Consumer<Object>() {
//			@Override
//			public void accept(Object t) {
//				JSONObject jsonObject = (JSONObject) t;
//				eventFieldsMap.put(jsonObject.getString("name"), jsonObject);
//			}
//		});
//
//		JSONObject eventBodyJson = eventFieldsMap.get("body");
//		JSONArray eventBodyTypes = (JSONArray) eventBodyJson.remove("type");
//		eventBodyTypes.put(objectName);
//		eventBodyJson.put("type", eventBodyTypes);
//
//		jsonObjects.put(schemJsonForObject);
//
//		updateSubject(request, response);
//
//		if (response.isSuccess()) {
//			SchemaRegistryResponse<AvroSchema> updatedGetResponse = getSubject(request);
//			AvroSchema updatedAvroSchema = updatedGetResponse.getResult();
//
//			if (updatedGetResponse.isSuccess()) {
//				if (updatedAvroSchema.getId() == response.getResult().getId()
//						&& updatedAvroSchema.getId() == response.getResult().getVersion()) {
//					log.info(
//							"Get updated latest schema with id {}, version {} for subject {} at schema registry {} validation has failed. Previous id {}, version {}",
//							avroSchema.getId(), updatedAvroSchema.getVersion(), request.getSubject_name(),
//							Constants.KAFKA_SCHEMA_REGISTRY_URL, response.getResult().getId(),
//							response.getResult().getVersion());
//					response.setValidationSuccess(false);
//					response.setValidation_error_message(String.format(
//							"Updated get latest schema with id %s, version %s for subject %s at schema registry %s validation has failed. Previous id %s, version %s",
//							avroSchema.getId(), updatedAvroSchema.getVersion(), request.getSubject_name(),
//							Constants.KAFKA_SCHEMA_REGISTRY_URL, response.getResult().getId(),
//							response.getResult().getVersion()));
//				} else {
//					log.info(
//							"Got updated latest schema with id {}, version {} for subject {} from schema registry {} is \n{}",
//							updatedAvroSchema.getId(), updatedAvroSchema.getVersion(), request.getSubject_name(),
//							Constants.KAFKA_SCHEMA_REGISTRY_URL, updatedAvroSchema.getSchema());
//					response.setValidationSuccess(true);
//					response.setValidationMessage(String.format(
//							"Succefully validated that the id {}, version {} for subject {} from schema registry {} is updated from previous id %s and version %s",
//							updatedAvroSchema.getId(), updatedAvroSchema.getVersion(), request.getSubject_name(),
//							Constants.KAFKA_SCHEMA_REGISTRY_URL, response.getResult().getId(),
//							response.getResult().getVersion()));
//					response.setResult(updatedAvroSchema);
//				}
//			} else {
//				log.error("Failed to get updted latest schema for subject {} from registry {}",
//						request.getSubject_name(), Constants.KAFKA_SCHEMA_REGISTRY_URL);
//				response.setError_message(
//						String.format("Failed to get updted latest for subject %s at schema registry %s , cause %s",
//								request.getSubject_name(), Constants.KAFKA_SCHEMA_REGISTRY_URL,
//								updatedGetResponse.getError_message()));
//			}
//		}
//
//		return response;
//	}
//
//	private SchemaRegistryResponse deleteSubject(SchemaRegistryRequest request) {
//		SchemaRegistryResponse response = new SchemaRegistryResponse();
//		StringBuilder urlBuilder = new StringBuilder(Constants.KAFKA_SCHEMA_REGISTRY_URL);
//		urlBuilder.append("/subjects/{0}?");
//		urlBuilder.append("permanent=" + request.isHard_delete());
//		ResponseEntity<String> restResponse = deleteRestResponse(urlBuilder.toString(), request.getSubject_name());
//
//		if (HttpUtils.isOk(restResponse)) {
//			response.setMessage(String.format("Deleted versions %s for subject %s at schema registry %s",
//					restResponse.getBody(), request.getSubject_name(), Constants.KAFKA_SCHEMA_REGISTRY_URL));
//		} else {
//			log.error("Unable to delete the subject {} schema at schema registry {}", request.getSubject_name(),
//					Constants.KAFKA_SCHEMA_REGISTRY_URL);
//			response.setError_message(
//					String.format("Unable to delete the subject %s schema at schema registry %s , cause %s",
//							request.getSubject_name(), Constants.KAFKA_SCHEMA_REGISTRY_URL, restResponse.getBody()));
//		}
//
//		return response;
//	}
//
//	protected ResponseEntity<String> updateRestResponse(String url, String schemaJson, String... uriVariables) {
//		ResponseEntity<String> httpResponse = null;
//		int retry = 0;
//		String errorMessage = null;
//
//		do {
//			HttpHeaders headers = new HttpHeaders();
//			//headers.setContentType(new MediaType("application", "vnd.schemaregistry.v1+json"));
//		//	headers.setContentType(MediaType.APPLICATION_JSON);
//			headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
//			headers.set("Content-Type", "application/vnd.schemaregistry.v1+json");
//
//			String schema = "{\"schema\":\"" + schemaJson.replace("\"", "\\\"") + "\"}" ;
//			HttpEntity<String> httpRequest = new HttpEntity<String>(schema, headers);
//
//			try {
//				log.info(httpRequest.toString());
//				httpResponse = restTemplate.exchange(url, HttpMethod.POST, httpRequest, String.class, uriVariables);
//				break;
//			} catch (HttpServerErrorException se) {
//				log.error("Failed to get url {} with retry {}, cause {}", url, retry, se.toString());
//				errorMessage = se.toString();
//				HttpUtils.wait(1000);
//			} catch (HttpClientErrorException nfe) {
//				log.error("Failed to get url {}  with retry {}, cause {}", url, retry, nfe.toString());
//				errorMessage = nfe.toString();
//				HttpUtils.wait(1000);
//			} catch (Exception ex) {
//				log.error("Failed to get url {}, cause {}", url, ex.toString());
//				throw ex;
//			}
//
//			if (retry == 3) {
//				throw new RuntimeException(errorMessage);
//			}
//
//			try {
//				Thread.currentThread().sleep(1000);
//			} catch (Exception e) {
//			}
//		} while (retry++ < 4);
//
//		return httpResponse;
//	}
//
//	protected ResponseEntity<String> deleteRestResponse(String url, String... uriVariables) {
//		ResponseEntity<String> httpResponse = null;
//		int retry = 0;
//		String errorMessage = null;
//
//		do {
//			HttpHeaders headers = new HttpHeaders();
//			headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
//			HttpEntity httpRequest = new HttpEntity(headers);
//
//			try {
//				httpResponse = restTemplate.exchange(url, HttpMethod.DELETE, httpRequest, String.class, uriVariables);
//				break;
//			} catch (HttpServerErrorException se) {
//				log.error("Failed to get url {} with retry {}, cause {}", url, retry, se.toString());
//				errorMessage = se.toString();
//				HttpUtils.wait(1000);
//			} catch (HttpClientErrorException nfe) {
//				log.error("Failed to get url {}  with retry {}, cause {}", url, retry, nfe.toString());
//				errorMessage = nfe.toString();
//				HttpUtils.wait(1000);
//			} catch (Exception ex) {
//				log.error("Failed to get url {}, cause {}", url, ex.toString());
//				throw ex;
//			}
//
//			if (retry == 3) {
//				throw new RuntimeException(errorMessage);
//			}
//
//			try {
//				Thread.currentThread().sleep(1000);
//			} catch (Exception e) {
//			}
//		} while (retry++ < 4);
//
//		return httpResponse;
//	}
//
//	protected ResponseEntity<String> getRestResponse(String url, String... uriVariables) {
//
//		ResponseEntity<String> httpResponse = null;
//
//		int retry = 0;
//		String errorMessage = null;
//
//		do {
//			HttpHeaders headers = new HttpHeaders();
//			// headers.setAccept(Collections.singletonList(new
//			// MediaType("application/vnd.schemaregistry.v1+json")));
//
//			headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
//
//			HttpEntity httpRequest = new HttpEntity(headers);
//
//			try {
//				httpResponse = restTemplate.exchange(url, HttpMethod.GET, null, String.class, uriVariables);
////				httpResponse = restTemplate.exchange(url, HttpMethod.GET, httpRequest, String.class,
////						uriVariables);
//				break;
//			} catch (HttpServerErrorException se) {
//				log.error("Failed to get url {} with retry {}, cause {}", url, retry, se.toString());
//				errorMessage = se.toString();
//				HttpUtils.wait(1000);
//			} catch (HttpClientErrorException nfe) {
//				log.error("Failed to get url {}  with retry {}, cause {}", url, retry, nfe.toString());
//				errorMessage = nfe.toString();
//				HttpUtils.wait(1000);
//			} catch (Exception ex) {
//				log.error("Failed to get url {}, cause {}", url, ex.toString());
//				throw ex;
//			}
//
//			if (retry == 3) {
//				throw new RuntimeException(errorMessage);
//			}
//
//			try {
//				Thread.currentThread().sleep(1000);
//			} catch (Exception e) {
//			}
//		} while (retry++ < 4);
//
//		return httpResponse;
//	}
//
//	public static void main(String[] args) {
//		SchemaRegistryService service = new SchemaRegistryService();
//		String testObject = "{\n" + "    \"type\": \"record\",\n" + "    \"name\": \"test_object\",\n"
//				+ "    \"namespace\": \"com.paloaltonetworks.sfdc\",\n" + "    \"fields\": [\n" + "      {\n"
//				+ "        \"name\": \"filed1\",\n" + "        \"type\": [\n" + "          \"null\",\n"
//				+ "          \"string\"\n" + "        ]\n" + "      },\n" + "      {\n"
//				+ "        \"name\": \"filed2\",\n" + "        \"type\": [\n" + "          \"null\",\n"
//				+ "          \"double\"\n" + "        ]\n" + "      },\n" + "      {\n"
//				+ "        \"name\": \"field3\",\n" + "        \"type\": [\n" + "          \"null\",\n"
//				+ "          \"string\"\n" + "        ]\n" + "      }\n" + "  ]\n" + "}";
//		String testSubject = "test_subject";
//		String namespace = "com.paloaltonetworks.sfdc";
//		SchemaRegistryRequest request = new SchemaRegistryRequest();
//		request.setNew_object(true);
//		request.setSubject_name(testSubject);
//		request.setJsonSchema(testObject);
//		SchemaRegistryResponse response = service.process(request);
//		log.info(response.toString());
//	}

}