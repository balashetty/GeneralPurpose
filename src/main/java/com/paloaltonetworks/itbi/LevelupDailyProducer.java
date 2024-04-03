package com.paloaltonetworks.itbi;

import java.time.LocalDate;
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
public class LevelupDailyProducer implements CommandLineRunner {
	private static final Logger log = LogManager.getLogger(LevelupDailyProducer.class);
//	private String[] objects = "abc__c,Account,AccountBrand,Asset,AssetRelationship,Campaign,CampaignInfluence,CampaignMember,Case,ChannelProgram,ChannelProgramLevel,ChannelProgramMember,iseeit__Checklist_Type_Value_Mapping__c,CommSubscription,CommSubscriptionChannelType,CommSubscriptionConsent,CommSubscriptionTiming,Contact,ContactPointConsent,ContactPointEmail,ContactPointPhone,ContactPointTypeConsent,ContactRequest,Contract,ContractLineItem,rkpi2__Country__c,rkpi2__County__c,Entitlement,Lead,Opportunity,OpportunityContactRole,OpportunityLineItem,iseeit__Opportunity_Role__c,Order,OrderItem,Pricebook2,PricebookEntry,Product2,Quote,rkpi2__State__c,User"
//			.split(",");

	// @Autowired
	// AppConfig appConfig;
	RestTemplate restTemplate = new RestTemplate();
	//final Map<Integer, Integer> failedPages = new java.util.concurrent.ConcurrentHashMap<>();
	List<LocalDate> failedDates = new java.util.concurrent.CopyOnWriteArrayList();
	
	public static void main(String[] args) {
		SpringApplication.run(LessonThree.class, args);
	}

	@Override
	public void run(String... args) {
	
		try {
			int threadPoolSize = 5;
			LocalDate start = LocalDate.of(2024, 1, 1);
			LocalDate end = LocalDate.of(2024, 2, 28);

			
				ExecutorService executorService = Executors.newFixedThreadPool(threadPoolSize);
				List<FutureTask<Boolean>> futureResults = new LinkedList<FutureTask<Boolean>>();
				List<ExecutorTask> taskList = new LinkedList<ExecutorTask>();
				
				long startTime = System.currentTimeMillis();
				
				for (LocalDate dt=start; dt.isBefore(end); dt = dt.plusDays(1)) {
					ExecutorTask task = new ExecutorTask(dt);
					FutureTask<Boolean> futureTask = new FutureTask<Boolean>(task);
					executorService.submit(futureTask);
					futureResults.add(futureTask);
					taskList.add(task);
				}
	
				log.info("Completed Calculated Task executor submission");
	
				boolean isComplete = true;
	
				do {
					isComplete = true;
					for (FutureTask<Boolean> futureResult : futureResults) {
						isComplete &= futureResult.isDone();
					}
	
					log.info("Future task:" + isComplete);
					
					for (ExecutorTask task : taskList) {
						isComplete &= task.isDone();
					}
					
					log.info("Task:" + isComplete);
					if (!isComplete) {
						Thread.sleep(10000);
					}
				} while(!isComplete);
	
				log.info("Completed Calculated jobs");
	
				executorService.shutdown();
				
				long endTime = System.currentTimeMillis();
				log.info("Total time taken for processing :" +  (endTime - startTime) / (1000 * 60) + " Minutes");
			} catch (Exception e) {
				log.error("Failed to run calculated jobs", e);
			} 

		
		log.info("failedDates:" + failedDates);
		System.exit(0);

	}
	

	class ExecutorTask implements Callable<Boolean> {
		AtomicBoolean done = new AtomicBoolean(false);
		LocalDate dt = null;

		public ExecutorTask(LocalDate dt) {
			this.dt = dt;
		}

		@Override
		public Boolean call() {
			try {
				int retry = 3;
				boolean success = false;

				while (retry-- > 0) {
					try {
						MultiValueMap<String, String> headers = new LinkedMultiValueMap<>();
						headers.add("Content-Type", "application/json");
						JSONObject request = new JSONObject();
						request.put("object_name", "enrollment");
						request.put("last_runtime", dt.toString() + "T00:00:00");
						request.put("source", "levelup");
						request.put("search_field", "updated_on_from");
						
						
						log.info("Request  " + "enrollment" + ": " + request.toString());
						HttpEntity<String> sfdcProducerRequest = new HttpEntity<String>(request.toString(), headers);

						ResponseEntity<String> jobResponse = null;
						jobResponse = restTemplate.exchange(
								"http://aiap-dp.paloaltonetworks.local/beacon-producer-service/sync", HttpMethod.POST,
								sfdcProducerRequest, String.class);

						JSONObject response = new JSONObject(jobResponse.getBody());

						log.info("Beacon Response body for enrollment for date:" +  dt.toString());
						retry = 0;
						success = true;
					} catch (Exception e) {
						log.error("Failed to execute task", e);
					}
				}
				if (!success) {
					failedDates.add(dt);
					log.error("Failed dates:" + dt);
				}
			} finally {
				done.set(true);
			}
			return true;
		}

		public boolean isDone() {
			return done.get();
		}
	}
//	class SFDCCalculatedTask implements Callable<Boolean> {
//		AtomicBoolean done = new AtomicBoolean(false);
//		int startPage;
//		int endPage;
//		
//		public SFDCCalculatedTask(int startPage, int endPage) {
//			this.startPage = startPage;
//			this.endPage = endPage;
//		}
//
//		@Override
//		public Boolean call() {
//			try {
//				MultiValueMap<String, String> headers = new LinkedMultiValueMap<>();
//				headers.add("Content-Type", "application/json");
//				JSONObject request = new JSONObject();
//				request.put("object_name", "course");
//				//request.put("start_date", "2005-05-25T00:00:00");
//				//request.put("end_date", "2020-05-25T00:00:00");
//				request.put("last_runtime", "2005-05-25T00:00:00");
//				request.put("source", "levelup");
//				request.put( "search_field", "updated_on_from");
//				request.put("start_page", startPage);
//				request.put("end_page", endPage);
//				
//				log.info("Request  " + "enrollment" + ": " + request.toString());
//				HttpEntity<String> sfdcProducerRequest = new HttpEntity<String>(request.toString(), headers);
//
//				ResponseEntity<String> jobResponse = null;
//				jobResponse = restTemplate.exchange(
//						"http://aiap-dp.paloaltonetworks.local/levelup-producer-service/sync",
//						HttpMethod.POST, sfdcProducerRequest, String.class);
//
//				JSONObject response = new JSONObject(jobResponse.getBody());
//
//				log.info("Response body " + "enrollment" + ": " + response.toString());
//			} catch (Exception e) {
//				log.error("Failed to execute task", e);
//				failedPages.put(startPage, endPage);
//			} finally {
//				done.set(true);
//			}
//			return true;
//		}
//		
//		public boolean isDone() {
//			return done.get();
//		}
//	}
}