package com.paloaltonetworks.itbi;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.function.Consumer;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONTokener;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

public class SFDCCalculatedSchemaCleanUp {
	private static final Logger log = LogManager.getLogger(SFDCCalculatedSchemaCleanUp.class);
	//knowledgearticleversion_archived
	
	public static void main(String[] args) throws IOException {
		String[] objects = { "account_competitors__c_calculated	","account_customchangehistory__c_calculated	","account_plan__c_calculated	","account_strategy_scoring__c_calculated	","apttus__apts_agreement__c_calculated	","asset__c_calculated	","atr_record__c_calculated	","blng__billingschedule__c_calculated	","blng__billingtransaction__c_calculated	","blng__invoiceline__c_calculated	","blng__invoicerun__c_calculated	","blng__invoice__c_calculated	","blng__paymentallocationinvoiceline__c_calculated	","campaignmember_calculated	","campaign_calculated	","cap_case__c_calculated	","cap_contact__c_calculated	","cap_nominationreasons__c_calculated	","case_calculated	","case_escalation_prediction__c_calculated	","case_escalation__c_calculated	","cbr_node__c_calculated	","cbr__c_calculated	","ccrz__e_cartitem__c_calculated	","ccrz__e_cart__c_calculated	","ccrz__e_invoice__c_calculated	","ccrz__e_orderitem__c_calculated	","ccrz__e_order__c_calculated	","ccrz__e_subscription__c_calculated	","clzv6bp__clarizen_milestone__c_calculated	","clzv6bp__clarizen_project__c_calculated	","contact_calculated	","contract_calculated	","contract_relation__c_calculated	","coveov2__coveocaseattachedresult__c_calculated	","cpq_quote__c_calculated	","csat_gs_response__c_calculated	","ctf__c_calculated	","customer_success_engagement__c_calculated	","dealreg_approval__c_calculated	","deal_registration__c_calculated	","ea_token_consumption__c_calculated	","ea_token__c_calculated	","enterprise_agreement__c_calculated	","entitlement_calculated	","eval_comment__c_calculated	","eval_extn_request__c_calculated	","eval_inventory__c_calculated	","eval_product__c_calculated	","eval_request__c_calculated	","eval_serial_number__c_calculated	","event_calculated	","event_job__c_calculated	","event_slot__c_calculated	","fund_request__c_calculated	","influence_map__c_calculated	","lead_calculated	","linked_opportunity__c_calculated	","list__c_calculated	","opportunity_customchangehistory__c_calculated	","orderitem_calculated	","order_calculated	","partner_compliance_activity_requirement__c_calculated","partner_compliance_manual_activity__c_calculated	","partner_compliance__c_calculated	","poc_engineers__c_calculated	","poc_product__c_calculated	","poc_request__c_calculated	","pql__c_calculated	","product_evaluation_request__c_calculated	","promotions__c_calculated	","psregionmapping__c_calculated	","quote_line_detail__c_calculated	","quote__c_calculated	","reimbursement_claim__c_calculated	","resource_request__c_calculated	","risk_report_audit__c_calculated	","rma_outgoingitem__c_calculated	","rma_returnitem__c_calculated	","rma__c_calculated	","saas_deal_referral__c_calculated	","salespath_transaction__c_calculated	","sbaa__approval__c_calculated	","sbaa__approver__c_calculated	","sbqq__productoption__c_calculated	","sbqq__quoteline__c_calculated	","sbqq__quote__c_calculated	","sbqq__subscription__c_calculated	","service_engagement__c_calculated	","service_implementation_plan__c_calculated	","service_request__c_calculated	","short_url__c_calculated	","speaker_request__c_calculated	","specialist_forecast__c_calculated	","subscription_detail__c_calculated	","support_case_audit__c_calculated	","survey_ticket__c_calculated	","swarm_calculated	","task_calculated	","tspc__ap_ws_item__c_calculated	","tspc__competitor__c_calculated	","tspc__dealstakeholder__c_calculated	","user_profile__c_calculated	","use_case__c_calculated	","vramppartnerapplication__c_calculated	","vtmconfig__c_calculated	","vtmindustry__c_calculated	","account_calculated	","opportunitylineitem_calculated	","opportunity_calculated	","pan_distributors__c_calculated	","product2_calculated	","territory2_calculated	","user_calculated" };
		
//		String url = "http://localhost:8081/subjects/sfdc/versions/latest";
//		ResponseEntity<String> restResponse = getRestResponse(url);
//
//		if (restResponse.getStatusCode() != HttpStatus.OK) {
//			log.error("Failed to get schema from :" + url);
//			System.exit(1);
//		} else {
//			log.info ("Got the schema from url:" + url);
//		}

	
		String str = new String(Files.readAllBytes(Paths.get(
		"/Users/bshetty/workspace/git/develop/SFDCProducer/src/main/resources/schemas/sfdc_prod_calculated_schema.json")));
		
		JSONTokener tokener = new JSONTokener(str);
		JSONObject json = new JSONObject(tokener);
		JSONTokener tokener1 = new JSONTokener(json.getString("schema").replace("\\", ""));
		JSONArray schema = new JSONArray(tokener1);
		log.info ("Current schema total calculated objects  {}", (schema.length() - 2));
		
		JSONArray newSchema = new JSONArray();

		CopyOnWriteArrayList<String> objectList = new CopyOnWriteArrayList<String>();
		CopyOnWriteArrayList<String> unusedObjectList = new CopyOnWriteArrayList<String>();
		CopyOnWriteArrayList<String> usedList = new CopyOnWriteArrayList<String>();


		for (String obj : objects) {
			objectList.add(obj.trim().replaceAll("_calculated", "").replaceAll("_calcula...", ""));
		}

		schema.forEach(new Consumer<Object>() {

			@Override
			public void accept(Object o) {
				try {
					JSONObject jo = (JSONObject) o;
					String name = jo.getString("name");

					if (objectList.contains(name) || name.equalsIgnoreCase("metadata")
							|| name.equalsIgnoreCase("sfdc_event")) {
						newSchema.put(jo);
					} else {
						unusedObjectList.add(name);
					}
					
					if (objectList.contains(name)) {
						usedList.add(name);
					}
				} catch (Exception e) {
					log.error("error for {} is {}",  o, e.getMessage());
				}
			}
		});

		List<String> schedulerNotUsed = new ArrayList<String>();
		for (String name : objectList) {
			if (!usedList.contains(name))  {
				schedulerNotUsed.add(name);
			}
		}
		
		log.info("New schema calculated objects {}, which are  {}", usedList.size(), usedList);
		log.info("Current schema unused calculated objects in new schema {}, which are {}", unusedObjectList.size(), unusedObjectList);
		log.info("New schema unused scheduler objects {}, which are {}", schedulerNotUsed.size(), schedulerNotUsed);

		JSONObject xsfdcEventJo = newSchema.getJSONObject(newSchema.length() - 1);

		xsfdcEventJo.getJSONArray("fields").getJSONObject(1).remove("type");
		xsfdcEventJo.getJSONArray("fields").getJSONObject(1).put("type", usedList.toArray(new String[0]));
		// newSchema.put(xsfdcEventJo);

		FileWriter newFile = new FileWriter("new_sfdc_calculated_json.json");
		newFile.write(newSchema.toString());
		newFile.close();

		String schemaStr = "{\"schema\":\"" + newSchema.toString().replace("\"", "\\\"") + "\"}";

		log.info("SFDC new schema with calculated object size {}, removed  {} unused objects", (usedList.size()),
				unusedObjectList.size());
		File file =  new File("new_sfdc_calculated.json");
		FileWriter newFile1 = new FileWriter(file);
		newFile1.write(schemaStr);
		newFile1.close();
		log.info("Calculated schema file :" + file.getAbsolutePath());
		
	}

	protected  static ResponseEntity<String> getRestResponse(String url, String... uriVariables) {
		RestTemplate restTemplate = new RestTemplate();
		ResponseEntity<String> httpResponse = null;

			HttpHeaders headers = new HttpHeaders();
			// headers.setAccept(Collections.singletonList(new
			// MediaType("application/vnd.schemaregistry.v1+json")));

			headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));

			HttpEntity httpRequest = new HttpEntity(headers);

			try {
				httpResponse = restTemplate.exchange(url, HttpMethod.GET, null, String.class, uriVariables);
			} catch (Exception ex) {
				log.error("Failed to get url {}, cause {}", url, ex.toString());
				throw ex;
			}
			return httpResponse;
		}
}
