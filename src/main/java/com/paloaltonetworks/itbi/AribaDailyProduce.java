package com.paloaltonetworks.itbi;

import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.FutureTask;
import java.util.concurrent.atomic.AtomicBoolean;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.json.JSONObject;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class AribaDailyProduce implements CommandLineRunner {
	private static final Logger log = LogManager.getLogger(AribaDailyProduce.class);
//	private String[] objects = "abc__c,Account,AccountBrand,Asset,AssetRelationship,Campaign,CampaignInfluence,CampaignMember,Case,ChannelProgram,ChannelProgramLevel,ChannelProgramMember,iseeit__Checklist_Type_Value_Mapping__c,CommSubscription,CommSubscriptionChannelType,CommSubscriptionConsent,CommSubscriptionTiming,Contact,ContactPointConsent,ContactPointEmail,ContactPointPhone,ContactPointTypeConsent,ContactRequest,Contract,ContractLineItem,rkpi2__Country__c,rkpi2__County__c,Entitlement,Lead,Opportunity,OpportunityContactRole,OpportunityLineItem,iseeit__Opportunity_Role__c,Order,OrderItem,Pricebook2,PricebookEntry,Product2,Quote,rkpi2__State__c,User"
//			.split(",");

	// @Autowired
	// AppConfig appConfig;
	RestTemplate restTemplate = new RestTemplate();
	final Map<Integer, Integer> failedPages = new java.util.concurrent.ConcurrentHashMap<>();

	public static void main(String[] args) {
		SpringApplication.run(AribaDailyProduce.class, args);
	}

	@Override
	public void run(String... args) {
	
		try {
			long startTime = System.currentTimeMillis();
			
			try {
				MultiValueMap<String, String> headers = new LinkedMultiValueMap<>();
				headers.add("Content-Type", "application/json");
				JSONObject request = new JSONObject();
				request.put("object_name", "SavingsForm");
				// request.put("start_date", "2005-05-25T00:00:00");
				// request.put("end_date", "2020-05-25T00:00:00");
				request.put("last_runtime", "2005-05-25T00:00:00");
				request.put("to_runtime", "2005-05-25T00:00:00");
				request.put("source", "ariba");
				request.put("search_field", "updatedDateFrom");

				log.info("Request  " + "enrollment" + ": " + request.toString());
				HttpEntity<String> sfdcProducerRequest = new HttpEntity<String>(request.toString(), headers);

				ResponseEntity<String> jobResponse = null;
				jobResponse = restTemplate.exchange(
						"http://aiap-dp.paloaltonetworks.local/beacon-producer-service/sync", HttpMethod.POST,
						sfdcProducerRequest, String.class);

				JSONObject response = new JSONObject(jobResponse.getBody());

			} catch (Exception e) {
				log.error("Failed to execute task", e);
			}
	
			long endTime = System.currentTimeMillis();
			log.info("Total time taken for processing :" +  (endTime - startTime) / (1000 * 60) + " Minutes");
		} catch (Exception e) {
			log.error("Failed to run calculated jobs", e);
		} 
		
		log.info("FailedPages:" + failedPages);
		System.exit(0);

	}
	

}