package com.paloaltonetworks.itbi;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
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

public class SFDCSchemaCleanUp {
	private static final Logger log = LogManager.getLogger(SFDCSchemaCleanUp.class);
	//knowledgearticleversion_archived
	
	public static void main(String[] args) throws IOException {
		String[] objects = { "accounthistory	","accountshare	","accountteammember	","account_change_request__c	","account_competitors__c	","account_customchangehistory__c	","account_plan__c	","account_stakeholder_contacts__c	","account_stakeholder_details__c	","account_stakeholder_partners__c	","account_strategy_answer__c	","account_strategy_question__c	","account_strategy_scoring__c	","accreditations__c	","acv_error__c	","apttus__agreementlineitem__c	","apttus__agreement_document__c	","apttus__apts_agreement__c	","apttus__apts_related_agreement__c	","apttus__cycletimegroupdata__c	","apttus__cycletimegroup__c	","aqi_ltng_mng__articlequality_index__c	","aqi_ltng_mng__article_quality__c	","aqi_ltng_mng__article_quality__feed	","aqi_ltng_mng__article_quality__history	","aqi_ltng_mng__article_quality__share	","asset	","asset_summary__c	","asset__c	","assignmentrule	","assignment_rule__c	","atr_record__c	","atr_record__history	","blng__billingschedule__c	","blng__billingtransaction__c	","blng__invoiceline__c	","blng__invoicerun__c	","blng__invoice__c	","blng__paymentallocationinvoiceline__c	","blng__paymenttransaction__c	","blng__usagesummary__c	","blng__usage__c	","briefing_request_attendee__c	","bsource__briefing_attendee__c	","bsource__briefing_topic__c	","bsource__bs_deal_support_request__c	","bsource__deal_support_request_relationship__c	","bsource__dsr_account__c	","campaign	","campaignhistory	","campaignmember	","canadadepot__c	","cap_actionplanhistory__c	","cap_case__c	","cap_contact__c	","cap_event__c	","cap_nominationreasons__c	","cap_nominationreasons__history	","cap_note__c	","case	","casearticle	","casecomment	","casehistory	","casemilestone	","caserelatedissue	","caseshare	","casesolution	","case_comment_cc_email_list__c	","case_creation_cc_list__c	","case_customchangehistory__c	","case_dimension_mapping__c	","case_escalation_prediction_feedback__c	","case_escalation_prediction__c	","case_escalation__c	","case_escalation__history	","case_integration__c	","case_intent_mapping__c	","case_live_community_mapping__c	","case_priority_routing__c	","case_questionnaire__c	","case_skills_routing__c	","case_sme__c	","cbr_member__c	","cbr_member__history	","cbr_node__c	","cbr__c	","cbr__history	","ccrz__e_cartitem__c	","ccrz__e_cart__c	","ccrz__e_invoiceitem__c	","ccrz__e_invoice__c	","ccrz__e_orderitem__c	","ccrz__e_order__c	","ccrz__e_subscription__c	","ce_request__c	","clzv6bp__clarizen_milestone__c	","clzv6bp__clarizen_project__c	","collaborationroom	","competitor__c	","contact	","contacthistory	","contactshare	","contract	","contracthistory	","contract_relation__c	","countrystate__c	","countrytheatre__c	","country__c	","coveov2__coveocaseattachedresult__c	","coveov2__dynamicresources__c	","cpq_quote_line_item__c	","cpq_quote__c	","cpq_quote__history	","cpq_user__c	","csat_gs_response__c	","ctf__c	","customer_success_engagement__c	","custom_contract__c	","dashboard	","dealreg_approval__c	","deal_registration__c	","deal__c	","depotmap__c	","ea_token_consumption_allocation__c	","ea_token_consumption__c	","ea_token__c	","ela_esa_tp_uplift_percentage__c	","email_subscription_preference__c	","email_subscription_preference__history	","engagementcontact__c	","engagementcontact__history	","engagement_account__c	","engagement_account__history	","engagement_cycle_status__c	","engagement_resource__c	","engagement_resource__history	","engagement_update__c	","engagement_update__feed	","engagement_update__history	","engagement__c	","engagement__history	","engineer_profile_mapping__c	","enterprise_agreement__c	","entitlement	","entitlementcontact	","entitymilestone	","error_record__c	","eval_comment__c	","eval_extn_request__c	","eval_inventory__c	","eval_product__c	","eval_request__c	","eval_request__history	","eval_serial_number__c	","eval_shipment__c	","event	","event_job__c	","event_slot_job__c	","event_slot__c	","fund_request__c	","genesys_cloud_routing__c	","group	","groupmember	","incident	","incidenthistory	","incident_account__c	","incident_contact__c	","incident_customchangehistory__c	","incident_management__c	","indiadepot__c	","industry_naics__c	","industry__c	","influence_map__c	","insightsexternaldata	","insightsexternaldatapart	","intent_cta_mapping__c	","interaction_profile_log__c	","invoice_schedule__c	","ioinsight__c	","iso_country__c	","kcsknowledgesettings__c	","knowledgeableuser	","knowledgearticle	","knowledgearticleversion	","knowledgearticleversionhistory	","knowledgearticleversion_archived	","KnowledgeArticleVersion_draft	","knowledgearticleviewstat	","knowledgearticlevotestat	","knowledgearticle_rating__c	","knowledgearticle_rating__history	","knowledge__datacategoryselection	","knowledge__ka	","knowledge__kav	","knowledge__kav_archived	","knowledge__kav_draft	","knowledge__viewstat	","knowledge__votestat	","lead	","leadhistory	","leadstatus	","license_association__c	","linked_opportunity__c	","list__c	","loginhistory	","ltv_account__c	","ltv_opportunity__c	","marketplace_account_mapping__c	","medalliainvitationdata__c	","medallia_feedback__c	","migration_data__c	","milestonetype	","mktp_exception_log__c	","note	","objectpermissions	","objectterritory2assignmentrule	","objectterritory2assignmentruleitem	","objectterritory2association	","opportunitycontactrole	","opportunityfieldhistory	","opportunityshare	","opportunityteammember	","opportunity_customchangehistory__c	","opportunity_extension__c	","opportunity__hd	","order	","orderhistory	","orderitem	","pan_outboundmail__c	","partner	","partnerrole	","partner_compliance_activity_group__c	","partner_compliance_activity_requirement__c	","partner_compliance_manual_activity__c	","partner_compliance__c	","partner_product_specialization_map__c	","permissionset	","permissionsetassignment	","picklistvalueinfo	","poc_engineers__c	","poc_product__c	","poc_request_opportunities__c	","poc_request__c	","pql__c	","pricebook2	","pricebook2history	","pricebookentry	","price_realization_capture_change__c	","prisma_access_data__c	","prisma_saas_data__c	","processdefinition	","processinstance	","processinstancehistory	","processinstancenode	","processinstancestep	","processinstanceworkitem	","processnode	","process_request__c	","product_detail__c	","product_evaluation_request__c	","product_relation__c	","profile	","promotions__c	","psregionmapping__c	","purchase_request_form__c	","queuesobject	","quote_line_detail__c	","quote__c	","ratio_for_ea_coverage__c	","recordtype	","redlock_customer_log__c	","region__c	","reimbursement_claim__c	","resource_request_attendees__c	","resource_request__c	","risk_report_audit__c	","rma_country_depot__c	","rma_depot__c	","rma_outgoingitem__c	","rma_outgoingitem__history	","rma_returnitem__c	","rma_returnitem__history	","rma__c	","rma__history	","ruleterritory2association	","saas_deal_referral__c	","salespath_mapping__c	","salespath_process__c	","salespath_transaction__c	","sap_depot_map__c	","sap_orders__c	","sbaa__approvalchain__c	","sbaa__approvalrule__c	","sbaa__approval__c	","sbaa__approver__c	","sbqq__discounttier__c	","sbqq__productfeature__c	","sbqq__productoption__c	","sbqq__quoteline__c	","sbqq__quote__c	","sbqq__quote__history	","sbqq__subscription__c	","sbqq__subscription__history	","sb_ela_esa_extension__c	","serialnumber_relation__c	","service_deliverable__c	","service_engagement_customer_contact__c	","service_engagement_questionnaire__c	","service_engagement__c	","service_implementation_plan__c	","service_request__c	","service_team__c	","service_team__history	","setupaudittrail	","setup_audit_trail__c	","se_outreach_combined_pan_os_certificate__c	","short_url__c	","sizingrequest__c	","slack_transcript_data__c	","slack_user_mapping__c	","slack_user_mapping__history	","solution	","speaker_request__c	","specialist_forecast__c	","special_supportinstruction__c	","subscription_detail__c	","support_case_audit__c	","survey_ticket__c	","swarm	","swarmhistory	","swarmmember	","swarmmemberhistory	","tam__c	","task	","technology_alliance_partner__c	","territory2model	","territory2opportunity_junction__c	","territory2type	","training_session__c	","tspc__accountmapnode__c	","tspc__accountmap__c	","tspc__ap_ws_competitor__c	","tspc__ap_ws_item__c	","tspc__ap__c	","tspc__businessunit__c	","tspc__competitor__c	","tspc__dealstakeholder__c	","tspc__deal__c	","userlicense	","userrole	","userterritory2association	","user_permission__c	","user_profile__c	","user_profile__history	","use_case__c	","utm_change_history__c	","vramppartnerapplication__c	","vtmconfig__c	","vtmindustry__c	","zvc__zoom_meeting__c	","account	","bideleted_account__c	","bideleted_object__c	","bideleted_object__c__60	","opportunity	","opportunitylineitem	","opportunitysplit	","pan_distributors__c	","product2	","territory2	","user	",};
		
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
		"/Users/bshetty/workspace/git/GeneralPurpose/src/main/resources/sfdc.json")));
		
		JSONTokener tokener = new JSONTokener(str);
		JSONObject json = new JSONObject(tokener);
		JSONTokener tokener1 = new JSONTokener(json.getString("schema").replace("\\", ""));
		JSONArray schema = new JSONArray(tokener1);
		log.info ("Current schema total objects  {}", (schema.length() - 2));
		
		JSONArray newSchema = new JSONArray();

		CopyOnWriteArrayList<String> objectList = new CopyOnWriteArrayList<String>();
		CopyOnWriteArrayList<String> unusedObjectList = new CopyOnWriteArrayList<String>();
		CopyOnWriteArrayList<String> usedList = new CopyOnWriteArrayList<String>();


		for (String obj : objects) {
			objectList.add(obj.trim());
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
		
		log.info("New schema objects {}, which are  {}", usedList.size(), usedList);
		log.info("Current schema unused objects in new schema {}, which are {}", unusedObjectList.size(), unusedObjectList);
		log.info("New schema unused scheduler objects {}, which are {}", schedulerNotUsed.size(), schedulerNotUsed);
		
		JSONObject xsfdcEventJo = newSchema.getJSONObject(newSchema.length() - 1);

		xsfdcEventJo.getJSONArray("fields").getJSONObject(1).remove("type");
		xsfdcEventJo.getJSONArray("fields").getJSONObject(1).put("type", usedList.toArray(new String[0]));
		// newSchema.put(xsfdcEventJo);

		FileWriter newFile = new FileWriter("new_sfdc_json.json");
		newFile.write(newSchema.toString());
		newFile.close();

		String schemaStr = "{\"schema\":\"" + newSchema.toString().replace("\"", "\\\"") + "\"}";

		log.info("SFDC new schema with object size {}, removed  {} unused objects", (usedList.size()),
				unusedObjectList.size());
		File file =  new File("new_sfdc.json");
		FileWriter newFile1 = new FileWriter(file);
		newFile1.write(schemaStr);
		newFile1.close();
		log.info("Schema file :" + file.getAbsolutePath());
		
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
