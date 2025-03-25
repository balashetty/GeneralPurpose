from datetime import timedelta, datetime
import json
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCheckOperator

default_args = {
'owner': 'Datapipeline Team',
'depends_on_past': False,
'start_date': datetime(2019, 6, 25),
'email': ['Data-Pipeline-Team@paloaltonetworks.com'],
'email_on_failure': True,
'email_on_retry': False,
'retries': 1,
'retry_delay': timedelta(minutes=5),
}

schedule_interval_4 = "25 */4 * * *"
schedule_interval_2 = "40 */2 * * *"

dag2 = DAG('dedup_sfdc_landing_2', default_args=default_args, schedule_interval=schedule_interval_2)
dag4 = DAG('dedup_sfdc_landing_4', default_args=default_args, schedule_interval=schedule_interval_4)

list__c= BigQueryExecuteQueryOperator(
	task_id='list__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.list__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.list__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

entitlementcontact= BigQueryExecuteQueryOperator(
	task_id='entitlementcontact',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.entitlementcontact` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.entitlementcontact` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

redlock_customer_log__c= BigQueryExecuteQueryOperator(
	task_id='redlock_customer_log__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.redlock_customer_log__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.redlock_customer_log__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

pendo_account_log__c= BigQueryExecuteQueryOperator(
	task_id='pendo_account_log__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.pendo_account_log__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.pendo_account_log__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

pendo_account__c= BigQueryExecuteQueryOperator(
	task_id='pendo_account__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.pendo_account__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.pendo_account__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

briefing_request_attendee__c= BigQueryExecuteQueryOperator(
	task_id='briefing_request_attendee__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.briefing_request_attendee__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.briefing_request_attendee__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

casearticle= BigQueryExecuteQueryOperator(
	task_id='casearticle',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.casearticle` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.casearticle` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

user_profile__c= BigQueryExecuteQueryOperator(
	task_id='user_profile__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.user_profile__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.user_profile__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

kcsknowledgesettings__c= BigQueryExecuteQueryOperator(
	task_id='kcsknowledgesettings__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.kcsknowledgesettings__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.kcsknowledgesettings__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

entitlement= BigQueryExecuteQueryOperator(
	task_id='entitlement',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.entitlement` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.entitlement` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ccrz__e_order__c= BigQueryExecuteQueryOperator(
	task_id='ccrz__e_order__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ccrz__e_order__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ccrz__e_order__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ccrz__e_subscription__c= BigQueryExecuteQueryOperator(
	task_id='ccrz__e_subscription__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ccrz__e_subscription__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ccrz__e_subscription__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ccrz__e_orderitem__c= BigQueryExecuteQueryOperator(
	task_id='ccrz__e_orderitem__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ccrz__e_orderitem__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ccrz__e_orderitem__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ccrz__e_invoice__c= BigQueryExecuteQueryOperator(
	task_id='ccrz__e_invoice__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ccrz__e_invoice__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ccrz__e_invoice__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ccrz__e_invoiceitem__c= BigQueryExecuteQueryOperator(
	task_id='ccrz__e_invoiceitem__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ccrz__e_invoiceitem__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ccrz__e_invoiceitem__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

clzv6bp__clarizen_milestone__c= BigQueryExecuteQueryOperator(
	task_id='clzv6bp__clarizen_milestone__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.clzv6bp__clarizen_milestone__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.clzv6bp__clarizen_milestone__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

clzv6bp__clarizen_project__c= BigQueryExecuteQueryOperator(
	task_id='clzv6bp__clarizen_project__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.clzv6bp__clarizen_project__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.clzv6bp__clarizen_project__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagementcontact__history= BigQueryExecuteQueryOperator(
	task_id='engagementcontact__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagementcontact__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagementcontact__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

leadhistory= BigQueryExecuteQueryOperator(
	task_id='leadhistory',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.leadhistory` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.leadhistory` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

apttus__cycletimegroup__c= BigQueryExecuteQueryOperator(
	task_id='apttus__cycletimegroup__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.apttus__cycletimegroup__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.apttus__cycletimegroup__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunityfieldhistory= BigQueryExecuteQueryOperator(
	task_id='opportunityfieldhistory',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunityfieldhistory` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunityfieldhistory` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

enterprise_agreement__c= BigQueryExecuteQueryOperator(
	task_id='enterprise_agreement__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.enterprise_agreement__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.enterprise_agreement__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cbr_member__history= BigQueryExecuteQueryOperator(
	task_id='cbr_member__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cbr_member__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cbr_member__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

leadstatus= BigQueryExecuteQueryOperator(
	task_id='leadstatus',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.leadstatus` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.leadstatus` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement_account__history= BigQueryExecuteQueryOperator(
	task_id='engagement_account__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement_account__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement_account__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

contacthistory= BigQueryExecuteQueryOperator(
	task_id='contacthistory',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.contacthistory` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.contacthistory` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

email_subscription_preference__history= BigQueryExecuteQueryOperator(
	task_id='email_subscription_preference__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.email_subscription_preference__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.email_subscription_preference__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

training_session__c= BigQueryExecuteQueryOperator(
	task_id='training_session__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.training_session__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.training_session__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

apttus__apts_related_agreement__c= BigQueryExecuteQueryOperator(
	task_id='apttus__apts_related_agreement__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.apttus__apts_related_agreement__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.apttus__apts_related_agreement__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

case_escalation__c= BigQueryExecuteQueryOperator(
	task_id='case_escalation__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.case_escalation__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.case_escalation__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunityteammember= BigQueryExecuteQueryOperator(
	task_id='opportunityteammember',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunityteammember` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunityteammember` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

processinstance= BigQueryExecuteQueryOperator(
	task_id='processinstance',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.processinstance` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.processinstance` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cap_contact__c= BigQueryExecuteQueryOperator(
	task_id='cap_contact__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cap_contact__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cap_contact__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

speaker_request__c= BigQueryExecuteQueryOperator(
	task_id='speaker_request__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.speaker_request__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.speaker_request__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

service_deliverable__c= BigQueryExecuteQueryOperator(
	task_id='service_deliverable__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.service_deliverable__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.service_deliverable__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cap_case__c= BigQueryExecuteQueryOperator(
	task_id='cap_case__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cap_case__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cap_case__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

dscorgpkg__trigger__c= BigQueryExecuteQueryOperator(
	task_id='dscorgpkg__trigger__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.dscorgpkg__trigger__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.dscorgpkg__trigger__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

permissionsetassignment= BigQueryExecuteQueryOperator(
	task_id='permissionsetassignment',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.permissionsetassignment` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.permissionsetassignment` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

product_detail__c= BigQueryExecuteQueryOperator(
	task_id='product_detail__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.product_detail__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.product_detail__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

countrystate__c= BigQueryExecuteQueryOperator(
	task_id='countrystate__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.countrystate__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.countrystate__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

recordtype= BigQueryExecuteQueryOperator(
	task_id='recordtype',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.recordtype` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.recordtype` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement_update__feed= BigQueryExecuteQueryOperator(
	task_id='engagement_update__feed',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement_update__feed` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement_update__feed` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

groupmember= BigQueryExecuteQueryOperator(
	task_id='groupmember',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.groupmember` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.groupmember` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

pricebook2= BigQueryExecuteQueryOperator(
	task_id='pricebook2',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.pricebook2` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.pricebook2` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

eval_shipment__c= BigQueryExecuteQueryOperator(
	task_id='eval_shipment__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.eval_shipment__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.eval_shipment__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement__history= BigQueryExecuteQueryOperator(
	task_id='engagement__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

coveov2__coveocaseattachedresult__c= BigQueryExecuteQueryOperator(
	task_id='coveov2__coveocaseattachedresult__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.coveov2__coveocaseattachedresult__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.coveov2__coveocaseattachedresult__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cap_note__c= BigQueryExecuteQueryOperator(
	task_id='cap_note__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cap_note__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cap_note__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

eval_request__history= BigQueryExecuteQueryOperator(
	task_id='eval_request__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.eval_request__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.eval_request__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

accreditations__c= BigQueryExecuteQueryOperator(
	task_id='accreditations__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.accreditations__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.accreditations__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

assignment_rule__c= BigQueryExecuteQueryOperator(
	task_id='assignment_rule__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.assignment_rule__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.assignment_rule__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

pan_outboundmail__c= BigQueryExecuteQueryOperator(
	task_id='pan_outboundmail__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.pan_outboundmail__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.pan_outboundmail__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

lead= BigQueryExecuteQueryOperator(
	task_id='lead',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.lead` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.lead` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

fund_request__c= BigQueryExecuteQueryOperator(
	task_id='fund_request__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.fund_request__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.fund_request__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

fcrm__fcr_influence_detail__c= BigQueryExecuteQueryOperator(
	task_id='fcrm__fcr_influence_detail__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.fcrm__fcr_influence_detail__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.fcrm__fcr_influence_detail__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cpq_quote_line_item__c= BigQueryExecuteQueryOperator(
	task_id='cpq_quote_line_item__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cpq_quote_line_item__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cpq_quote_line_item__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cbr__c= BigQueryExecuteQueryOperator(
	task_id='cbr__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cbr__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cbr__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

event= BigQueryExecuteQueryOperator(
	task_id='event',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.event` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.event` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

apttus__cycletimegroupdata__c= BigQueryExecuteQueryOperator(
	task_id='apttus__cycletimegroupdata__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.apttus__cycletimegroupdata__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.apttus__cycletimegroupdata__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

atr_record__c= BigQueryExecuteQueryOperator(
	task_id='atr_record__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.atr_record__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.atr_record__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

competitor__c= BigQueryExecuteQueryOperator(
	task_id='competitor__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.competitor__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.competitor__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

campaignhistory= BigQueryExecuteQueryOperator(
	task_id='campaignhistory',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.campaignhistory` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.campaignhistory` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

service_team__c= BigQueryExecuteQueryOperator(
	task_id='service_team__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.service_team__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.service_team__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

accountshare= BigQueryExecuteQueryOperator(
	task_id='accountshare',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.accountshare` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.accountshare` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

rma_depot__c= BigQueryExecuteQueryOperator(
	task_id='rma_depot__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.rma_depot__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.rma_depot__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

quote__c= BigQueryExecuteQueryOperator(
	task_id='quote__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.quote__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.quote__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement__c= BigQueryExecuteQueryOperator(
	task_id='engagement__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

apttus__agreement_document__c= BigQueryExecuteQueryOperator(
	task_id='apttus__agreement_document__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.apttus__agreement_document__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.apttus__agreement_document__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement_account__c= BigQueryExecuteQueryOperator(
	task_id='engagement_account__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement_account__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement_account__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

rma__c= BigQueryExecuteQueryOperator(
	task_id='rma__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.rma__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.rma__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

slack_transcript_data__c= BigQueryExecuteQueryOperator(
	task_id='slack_transcript_data__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.slack_transcript_data__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.slack_transcript_data__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

user= BigQueryExecuteQueryOperator(
	task_id='user',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.user` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.user` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cap_actionplanhistory__c= BigQueryExecuteQueryOperator(
	task_id='cap_actionplanhistory__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cap_actionplanhistory__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cap_actionplanhistory__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement_update__c= BigQueryExecuteQueryOperator(
	task_id='engagement_update__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement_update__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement_update__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

pql__c= BigQueryExecuteQueryOperator(
	task_id='pql__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.pql__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.pql__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

case= BigQueryExecuteQueryOperator(
	task_id='case',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.case` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.case` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

dealreg_approval__c= BigQueryExecuteQueryOperator(
	task_id='dealreg_approval__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.dealreg_approval__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.dealreg_approval__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunitylineitem= BigQueryExecuteQueryOperator(
	task_id='opportunitylineitem',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunitylineitem` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunitylineitem` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

product2= BigQueryExecuteQueryOperator(
	task_id='product2',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.product2` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.product2` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

apttus__agreementlineitem__c= BigQueryExecuteQueryOperator(
	task_id='apttus__agreementlineitem__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.apttus__agreementlineitem__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.apttus__agreementlineitem__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

contact= BigQueryExecuteQueryOperator(
	task_id='contact',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.contact` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.contact` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledgearticlevotestat= BigQueryExecuteQueryOperator(
	task_id='knowledgearticlevotestat',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledgearticlevotestat` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledgearticlevotestat` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

iso_country__c= BigQueryExecuteQueryOperator(
	task_id='iso_country__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.iso_country__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.iso_country__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

userrole= BigQueryExecuteQueryOperator(
	task_id='userrole',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.userrole` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.userrole` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledgearticle= BigQueryExecuteQueryOperator(
	task_id='knowledgearticle',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledgearticle` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledgearticle` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

assignmentrule= BigQueryExecuteQueryOperator(
	task_id='assignmentrule',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.assignmentrule` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.assignmentrule` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

campaign= BigQueryExecuteQueryOperator(
	task_id='campaign',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.campaign` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.campaign` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

product_evaluation_request__c= BigQueryExecuteQueryOperator(
	task_id='product_evaluation_request__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.product_evaluation_request__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.product_evaluation_request__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledgearticleversion= BigQueryExecuteQueryOperator(
	task_id='knowledgearticleversion',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledgearticleversion` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledgearticleversion` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cpq_quote__c= BigQueryExecuteQueryOperator(
	task_id='cpq_quote__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cpq_quote__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cpq_quote__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

eval_request__c= BigQueryExecuteQueryOperator(
	task_id='eval_request__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.eval_request__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.eval_request__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

poc_request__c= BigQueryExecuteQueryOperator(
	task_id='poc_request__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.poc_request__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.poc_request__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

depotmap__c= BigQueryExecuteQueryOperator(
	task_id='depotmap__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.depotmap__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.depotmap__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunitycontactrole= BigQueryExecuteQueryOperator(
	task_id='opportunitycontactrole',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunitycontactrole` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunitycontactrole` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement_resource__history= BigQueryExecuteQueryOperator(
	task_id='engagement_resource__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement_resource__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement_resource__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

eval_serial_number__c= BigQueryExecuteQueryOperator(
	task_id='eval_serial_number__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.eval_serial_number__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.eval_serial_number__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

account_customchangehistory__c= BigQueryExecuteQueryOperator(
	task_id='account_customchangehistory__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.account_customchangehistory__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.account_customchangehistory__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

country__c= BigQueryExecuteQueryOperator(
	task_id='country__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.country__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.country__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledge__kav= BigQueryExecuteQueryOperator(
	task_id='knowledge__kav',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledge__kav` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledge__kav` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledge__kav_archived= BigQueryExecuteQueryOperator(
    task_id='knowledge__kav_archived',
    use_legacy_sql=False,
    allow_large_results=True,
    gcp_conn_id='bq-itq-aia-dp',
    labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
    sql='''delete `itq-aia-datalake.sfdc_landing.knowledge__kav_archived` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledge__kav_archived` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
    dag=dag4)

deal__c= BigQueryExecuteQueryOperator(
	task_id='deal__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.deal__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.deal__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

contactshare= BigQueryExecuteQueryOperator(
	task_id='contactshare',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.contactshare` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.contactshare` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

short_url__c= BigQueryExecuteQueryOperator(
	task_id='short_url__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.short_url__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.short_url__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cbr_member__c= BigQueryExecuteQueryOperator(
	task_id='cbr_member__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cbr_member__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cbr_member__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledge__ka= BigQueryExecuteQueryOperator(
	task_id='knowledge__ka',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledge__ka` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledge__ka` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

coveov2__dynamicresources__c= BigQueryExecuteQueryOperator(
	task_id='coveov2__dynamicresources__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.coveov2__dynamicresources__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.coveov2__dynamicresources__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunityshare= BigQueryExecuteQueryOperator(
	task_id='opportunityshare',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunityshare` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunityshare` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

bideleted_object__c= BigQueryExecuteQueryOperator(
	task_id='bideleted_object__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.bideleted_object__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.bideleted_object__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

objectterritory2association= BigQueryExecuteQueryOperator(
	task_id='objectterritory2association',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.objectterritory2association` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.objectterritory2association` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagementcontact__c= BigQueryExecuteQueryOperator(
	task_id='engagementcontact__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagementcontact__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagementcontact__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunitysplit= BigQueryExecuteQueryOperator(
	task_id='opportunitysplit',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunitysplit` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunitysplit` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

pan_distributors__c= BigQueryExecuteQueryOperator(
	task_id='pan_distributors__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.pan_distributors__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.pan_distributors__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

apttus__apts_agreement__c= BigQueryExecuteQueryOperator(
	task_id='apttus__apts_agreement__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.apttus__apts_agreement__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.apttus__apts_agreement__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledgearticleviewstat= BigQueryExecuteQueryOperator(
	task_id='knowledgearticleviewstat',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledgearticleviewstat` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledgearticleviewstat` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

tam__c= BigQueryExecuteQueryOperator(
	task_id='tam__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.tam__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.tam__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

salespath_mapping__c= BigQueryExecuteQueryOperator(
	task_id='salespath_mapping__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.salespath_mapping__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.salespath_mapping__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

rma_returnitem__c= BigQueryExecuteQueryOperator(
	task_id='rma_returnitem__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.rma_returnitem__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.rma_returnitem__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

deal_registration__c= BigQueryExecuteQueryOperator(
	task_id='deal_registration__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.deal_registration__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.deal_registration__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledge__datacategoryselection= BigQueryExecuteQueryOperator(
	task_id='knowledge__datacategoryselection',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledge__datacategoryselection` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledge__datacategoryselection` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

casehistory= BigQueryExecuteQueryOperator(
	task_id='casehistory',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.casehistory` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.casehistory` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

countrytheatre__c= BigQueryExecuteQueryOperator(
	task_id='countrytheatre__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.countrytheatre__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.countrytheatre__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cap_event__c= BigQueryExecuteQueryOperator(
	task_id='cap_event__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cap_event__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cap_event__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

utm_change_history__c= BigQueryExecuteQueryOperator(
	task_id='utm_change_history__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.utm_change_history__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.utm_change_history__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

risk_report_audit__c= BigQueryExecuteQueryOperator(
	task_id='risk_report_audit__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.risk_report_audit__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.risk_report_audit__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

industry_naics__c= BigQueryExecuteQueryOperator(
	task_id='industry_naics__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.industry_naics__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.industry_naics__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

accounthistory= BigQueryExecuteQueryOperator(
	task_id='accounthistory',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.accounthistory` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.accounthistory` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

case_escalation__history= BigQueryExecuteQueryOperator(
	task_id='case_escalation__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.case_escalation__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.case_escalation__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

medallia_feedback__c= BigQueryExecuteQueryOperator(
	task_id='medallia_feedback__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.medallia_feedback__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.medallia_feedback__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

email_subscription_preference__c= BigQueryExecuteQueryOperator(
	task_id='email_subscription_preference__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.email_subscription_preference__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.email_subscription_preference__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

rma_outgoingitem__c= BigQueryExecuteQueryOperator(
	task_id='rma_outgoingitem__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.rma_outgoingitem__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.rma_outgoingitem__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

asset__c= BigQueryExecuteQueryOperator(
	task_id='asset__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.asset__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.asset__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement_resource__c= BigQueryExecuteQueryOperator(
	task_id='engagement_resource__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement_resource__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement_resource__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

account= BigQueryExecuteQueryOperator(
	task_id='account',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.account` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.account` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

purchase_request_form__c= BigQueryExecuteQueryOperator(
	task_id='purchase_request_form__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.purchase_request_form__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.purchase_request_form__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunity= BigQueryExecuteQueryOperator(
	task_id='opportunity',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunity` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunity` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cbr__history= BigQueryExecuteQueryOperator(
	task_id='cbr__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cbr__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cbr__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

eval_comment__c= BigQueryExecuteQueryOperator(
	task_id='eval_comment__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.eval_comment__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.eval_comment__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

permissionset= BigQueryExecuteQueryOperator(
	task_id='permissionset',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.permissionset` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.permissionset` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

eval_inventory__c= BigQueryExecuteQueryOperator(
	task_id='eval_inventory__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.eval_inventory__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.eval_inventory__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

service_engagement_customer_contact__c= BigQueryExecuteQueryOperator(
	task_id='service_engagement_customer_contact__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.service_engagement_customer_contact__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.service_engagement_customer_contact__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

partnerrole= BigQueryExecuteQueryOperator(
	task_id='partnerrole',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.partnerrole` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.partnerrole` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

rma_returnitem__history= BigQueryExecuteQueryOperator(
	task_id='rma_returnitem__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.rma_returnitem__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.rma_returnitem__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

rma_outgoingitem__history= BigQueryExecuteQueryOperator(
	task_id='rma_outgoingitem__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.rma_outgoingitem__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.rma_outgoingitem__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

influence_map__c= BigQueryExecuteQueryOperator(
	task_id='influence_map__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.influence_map__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.influence_map__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

promotions__c= BigQueryExecuteQueryOperator(
	task_id='promotions__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.promotions__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.promotions__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

case_comment_cc_email_list__c= BigQueryExecuteQueryOperator(
	task_id='case_comment_cc_email_list__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.case_comment_cc_email_list__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.case_comment_cc_email_list__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledge__viewstat= BigQueryExecuteQueryOperator(
	task_id='knowledge__viewstat',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledge__viewstat` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledge__viewstat` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

group= BigQueryExecuteQueryOperator(
	task_id='group',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.group` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.group` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ce_request__c= BigQueryExecuteQueryOperator(
	task_id='ce_request__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ce_request__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ce_request__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

eval_product__c= BigQueryExecuteQueryOperator(
	task_id='eval_product__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.eval_product__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.eval_product__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

task= BigQueryExecuteQueryOperator(
	task_id='task',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.task` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.task` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

note= BigQueryExecuteQueryOperator(
	task_id='note',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.note` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.note` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

campaignmember= BigQueryExecuteQueryOperator(
	task_id='campaignmember',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.campaignmember` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.campaignmember` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cpq_user__c= BigQueryExecuteQueryOperator(
	task_id='cpq_user__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cpq_user__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cpq_user__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledge__votestat= BigQueryExecuteQueryOperator(
	task_id='knowledge__votestat',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledge__votestat` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledge__votestat` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

pricebookentry= BigQueryExecuteQueryOperator(
	task_id='pricebookentry',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.pricebookentry` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.pricebookentry` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sap_depot_map__c= BigQueryExecuteQueryOperator(
	task_id='sap_depot_map__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sap_depot_map__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sap_depot_map__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cap_nominationreasons__c= BigQueryExecuteQueryOperator(
	task_id='cap_nominationreasons__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cap_nominationreasons__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cap_nominationreasons__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

vtmconfig__c= BigQueryExecuteQueryOperator(
	task_id='vtmconfig__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.vtmconfig__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.vtmconfig__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledgearticleversionhistory= BigQueryExecuteQueryOperator(
	task_id='knowledgearticleversionhistory',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledgearticleversionhistory` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledgearticleversionhistory` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cap_nominationreasons__history= BigQueryExecuteQueryOperator(
	task_id='cap_nominationreasons__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cap_nominationreasons__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cap_nominationreasons__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

dscorgpkg__oppalert__c= BigQueryExecuteQueryOperator(
	task_id='dscorgpkg__oppalert__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.dscorgpkg__oppalert__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.dscorgpkg__oppalert__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

caseshare= BigQueryExecuteQueryOperator(
	task_id='caseshare',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.caseshare` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.caseshare` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement_update__history= BigQueryExecuteQueryOperator(
	task_id='engagement_update__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement_update__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement_update__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

territory2= BigQueryExecuteQueryOperator(
	task_id='territory2',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.territory2` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.territory2` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledgeableuser= BigQueryExecuteQueryOperator(
	task_id='knowledgeableuser',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledgeableuser` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledgeableuser` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

userterritory2association= BigQueryExecuteQueryOperator(
	task_id='userterritory2association',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.userterritory2association` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.userterritory2association` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

service_engagement__c= BigQueryExecuteQueryOperator(
	task_id='service_engagement__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.service_engagement__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.service_engagement__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

profile= BigQueryExecuteQueryOperator(
	task_id='profile',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.profile` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.profile` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

support_case_audit__c= BigQueryExecuteQueryOperator(
	task_id='support_case_audit__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.support_case_audit__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.support_case_audit__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cbr_node__c= BigQueryExecuteQueryOperator(
	task_id='cbr_node__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cbr_node__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cbr_node__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

salespath_process__c= BigQueryExecuteQueryOperator(
	task_id='salespath_process__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.salespath_process__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.salespath_process__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

cg__casefile__c= BigQueryExecuteQueryOperator(
	task_id='cg__casefile__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.cg__casefile__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.cg__casefile__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

salespath_transaction__c= BigQueryExecuteQueryOperator(
	task_id='salespath_transaction__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.salespath_transaction__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.salespath_transaction__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

casecomment= BigQueryExecuteQueryOperator(
	task_id='casecomment',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.casecomment` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.casecomment` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

accountteammember= BigQueryExecuteQueryOperator(
	task_id='accountteammember',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.accountteammember` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.accountteammember` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

slack_user_mapping__c= BigQueryExecuteQueryOperator(
	task_id='slack_user_mapping__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.slack_user_mapping__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.slack_user_mapping__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

slack_user_mapping__history= BigQueryExecuteQueryOperator(
	task_id='slack_user_mapping__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.slack_user_mapping__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.slack_user_mapping__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledgearticle_rating__c= BigQueryExecuteQueryOperator(
	task_id='knowledgearticle_rating__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledgearticle_rating__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledgearticle_rating__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

knowledgearticle_rating__history= BigQueryExecuteQueryOperator(
	task_id='knowledgearticle_rating__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.knowledgearticle_rating__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.knowledgearticle_rating__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)


psregionmapping__c= BigQueryExecuteQueryOperator(
	task_id='psregionmapping__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.psregionmapping__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.psregionmapping__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunity_territory__c= BigQueryExecuteQueryOperator(
	task_id='opportunity_territory__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunity_territory__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunity_territory__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

territory2opportunity_junction__c= BigQueryExecuteQueryOperator(
	task_id='territory2opportunity_junction__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.territory2opportunity_junction__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.territory2opportunity_junction__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

special_supportinstruction__c= BigQueryExecuteQueryOperator(
	task_id='special_supportinstruction__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.special_supportinstruction__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.special_supportinstruction__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

customer_success_engagement__c= BigQueryExecuteQueryOperator(
	task_id='customer_success_engagement__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.customer_success_engagement__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.customer_success_engagement__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engagement_cycle_status__c= BigQueryExecuteQueryOperator(
	task_id='engagement_cycle_status__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engagement_cycle_status__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engagement_cycle_status__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

vtmindustry__c= BigQueryExecuteQueryOperator(
	task_id='vtmindustry__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.vtmindustry__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.vtmindustry__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ccrz__e_cart__c= BigQueryExecuteQueryOperator(
	task_id='ccrz__e_cart__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ccrz__e_cart__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ccrz__e_cart__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ccrz__e_cartitem__c= BigQueryExecuteQueryOperator(
	task_id='ccrz__e_cartitem__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ccrz__e_cartitem__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ccrz__e_cartitem__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

order= BigQueryExecuteQueryOperator(
	task_id='order',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.order` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.order` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

orderitem= BigQueryExecuteQueryOperator(
	task_id='orderitem',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.orderitem` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.orderitem` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

casemilestone= BigQueryExecuteQueryOperator(
	task_id='casemilestone',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.casemilestone` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.casemilestone` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

aqi_ltng_mng__articlequality_index__c= BigQueryExecuteQueryOperator(
	task_id='aqi_ltng_mng__articlequality_index__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__articlequality_index__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__articlequality_index__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

aqi_ltng_mng__article_quality__c= BigQueryExecuteQueryOperator(
	task_id='aqi_ltng_mng__article_quality__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__article_quality__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__article_quality__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

aqi_ltng_mng__article_quality__feed= BigQueryExecuteQueryOperator(
	task_id='aqi_ltng_mng__article_quality__feed',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__article_quality__feed` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__article_quality__feed` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

aqi_ltng_mng__article_quality__share= BigQueryExecuteQueryOperator(
	task_id='aqi_ltng_mng__article_quality__share',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__article_quality__share` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__article_quality__share` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

aqi_ltng_mng__article_quality__history= BigQueryExecuteQueryOperator(
	task_id='aqi_ltng_mng__article_quality__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__article_quality__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, RANK() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.aqi_ltng_mng__article_quality__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

prisma_access_data__c= BigQueryExecuteQueryOperator(
	task_id='prisma_access_data__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.prisma_access_data__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.prisma_access_data__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

canadadepot__c= BigQueryExecuteQueryOperator(
	task_id='canadadepot__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.canadadepot__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.canadadepot__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

indiadepot__c= BigQueryExecuteQueryOperator(
	task_id='indiadepot__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.indiadepot__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.indiadepot__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

rma_country_depot__c= BigQueryExecuteQueryOperator(
	task_id='rma_country_depot__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.rma_country_depot__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.rma_country_depot__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

partner= BigQueryExecuteQueryOperator(
	task_id='partner',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.partner` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.partner` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

user_profile__history= BigQueryExecuteQueryOperator(
	task_id='user_profile__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.user_profile__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.user_profile__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

rma__history= BigQueryExecuteQueryOperator(
	task_id='rma__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.rma__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.rma__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

territory2type= BigQueryExecuteQueryOperator(
	task_id='territory2type',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.territory2type` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.territory2type` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

contract= BigQueryExecuteQueryOperator(
	task_id='contract',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.contract` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.contract` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ml_article_recommendation__c= BigQueryExecuteQueryOperator(
	task_id='ml_article_recommendation__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ml_article_recommendation__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ml_article_recommendation__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__cta__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__cta__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__cta__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__cta__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__ctatypes__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__ctatypes__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__ctatypes__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__ctatypes__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__ctagroup__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__ctagroup__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__ctagroup__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__ctagroup__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__gsrelationshiptype__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__gsrelationshiptype__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__gsrelationshiptype__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__gsrelationshiptype__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__gsrelationship__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__gsrelationship__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__gsrelationship__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__gsrelationship__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__customerinfo__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__customerinfo__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__customerinfo__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__customerinfo__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__picklist__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__picklist__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__picklist__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__picklist__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

territory2model= BigQueryExecuteQueryOperator(
	task_id='territory2model',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.territory2model` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.territory2model` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sbqq__quote__c= BigQueryExecuteQueryOperator(
	task_id='sbqq__quote__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sbqq__quote__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sbqq__quote__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sbqq__quoteline__c= BigQueryExecuteQueryOperator(
	task_id='sbqq__quoteline__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sbqq__quoteline__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sbqq__quoteline__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

blng__invoice__c= BigQueryExecuteQueryOperator(
	task_id='blng__invoice__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.blng__invoice__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.blng__invoice__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sbqq__subscription__c= BigQueryExecuteQueryOperator(
	task_id='sbqq__subscription__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sbqq__subscription__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sbqq__subscription__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

blng__invoiceline__c= BigQueryExecuteQueryOperator(
	task_id='blng__invoiceline__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.blng__invoiceline__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.blng__invoiceline__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

blng__paymentallocationinvoiceline__c= BigQueryExecuteQueryOperator(
	task_id='blng__paymentallocationinvoiceline__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.blng__paymentallocationinvoiceline__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.blng__paymentallocationinvoiceline__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

blng__paymenttransaction__c= BigQueryExecuteQueryOperator(
	task_id='blng__paymenttransaction__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.blng__paymenttransaction__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.blng__paymenttransaction__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

csat_gs_response__c= BigQueryExecuteQueryOperator(
	task_id='csat_gs_response__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.csat_gs_response__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.csat_gs_response__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__gsmetainfo__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__gsmetainfo__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__gsmetainfo__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__gsmetainfo__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__playbook__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__playbook__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__playbook__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__playbook__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__playbookinfo__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__playbookinfo__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__playbookinfo__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__playbookinfo__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__playbooktasks__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__playbooktasks__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__playbooktasks__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__playbooktasks__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

migration_data__c= BigQueryExecuteQueryOperator(
	task_id='migration_data__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.migration_data__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.migration_data__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

prisma_saas_data__c= BigQueryExecuteQueryOperator(
	task_id='prisma_saas_data__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.prisma_saas_data__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.prisma_saas_data__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__gsrelationship__history= BigQueryExecuteQueryOperator(
	task_id='jbcxm__gsrelationship__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__gsrelationship__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__gsrelationship__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

jbcxm__cstask__c= BigQueryExecuteQueryOperator(
	task_id='jbcxm__cstask__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.jbcxm__cstask__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.jbcxm__cstask__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunity_customchangehistory__c= BigQueryExecuteQueryOperator(
	task_id='opportunity_customchangehistory__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunity_customchangehistory__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunity_customchangehistory__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

service_team__history= BigQueryExecuteQueryOperator(
	task_id='service_team__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.service_team__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.service_team__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sked__slot__c= BigQueryExecuteQueryOperator(
	task_id='sked__slot__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sked__slot__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sked__slot__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sked__job__c= BigQueryExecuteQueryOperator(
	task_id='sked__job__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sked__job__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sked__job__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sked__job__history= BigQueryExecuteQueryOperator(
	task_id='sked__job__history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sked__job__history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sked__job__history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

account_plan__c= BigQueryExecuteQueryOperator(
	task_id='account_plan__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.account_plan__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.account_plan__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

account_competitors__c= BigQueryExecuteQueryOperator(
	task_id='account_competitors__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.account_competitors__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.account_competitors__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

objectpermissions= BigQueryExecuteQueryOperator(
	task_id='objectpermissions',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.objectpermissions` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.objectpermissions` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

asset_summary__c= BigQueryExecuteQueryOperator(
	task_id='asset_summary__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.asset_summary__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.asset_summary__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

poc_engineers__c= BigQueryExecuteQueryOperator(
	task_id='poc_engineers__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.poc_engineers__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.poc_engineers__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

poc_request_opportunities__c= BigQueryExecuteQueryOperator(
	task_id='poc_request_opportunities__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.poc_request_opportunities__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.poc_request_opportunities__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

acv_error__c= BigQueryExecuteQueryOperator(
	task_id='acv_error__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.acv_error__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.acv_error__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

processdefinition= BigQueryExecuteQueryOperator(
	task_id='processdefinition',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.processdefinition` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.processdefinition` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

processinstancestep= BigQueryExecuteQueryOperator(
	task_id='processinstancestep',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.processinstancestep` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.processinstancestep` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

processinstancenode= BigQueryExecuteQueryOperator(
	task_id='processinstancenode',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.processinstancenode` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.processinstancenode` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

reimbursement_claim__c= BigQueryExecuteQueryOperator(
	task_id='reimbursement_claim__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.reimbursement_claim__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.reimbursement_claim__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ea_token__c= BigQueryExecuteQueryOperator(
	task_id='ea_token__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ea_token__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ea_token__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ea_token_consumption__c= BigQueryExecuteQueryOperator(
	task_id='ea_token_consumption__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ea_token_consumption__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ea_token_consumption__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ea_token_consumption_allocation__c= BigQueryExecuteQueryOperator(
	task_id='ea_token_consumption_allocation__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ea_token_consumption_allocation__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ea_token_consumption_allocation__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

blng__usage__c= BigQueryExecuteQueryOperator(
	task_id='blng__usage__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.blng__usage__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.blng__usage__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

blng__usagesummary__c= BigQueryExecuteQueryOperator(
	task_id='blng__usagesummary__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.blng__usagesummary__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.blng__usagesummary__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

use_case__c= BigQueryExecuteQueryOperator(
	task_id='use_case__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.use_case__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.use_case__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

userlicense= BigQueryExecuteQueryOperator(
	task_id='userlicense',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.userlicense` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.userlicense` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

milestonetype= BigQueryExecuteQueryOperator(
	task_id='milestonetype',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.milestonetype` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.milestonetype` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

insightsexternaldata= BigQueryExecuteQueryOperator(
	task_id='insightsexternaldata',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.insightsexternaldata` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.insightsexternaldata` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

insightsexternaldatapart= BigQueryExecuteQueryOperator(
	task_id='insightsexternaldatapart',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.insightsexternaldatapart` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.insightsexternaldatapart` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

eval_extn_request__c= BigQueryExecuteQueryOperator(
	task_id='eval_extn_request__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.eval_extn_request__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.eval_extn_request__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

custom_contract__c= BigQueryExecuteQueryOperator(
	task_id='custom_contract__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.custom_contract__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.custom_contract__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

saas_deal_referral__c= BigQueryExecuteQueryOperator(
	task_id='saas_deal_referral__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.saas_deal_referral__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.saas_deal_referral__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

service_engagement_questionnaire__c= BigQueryExecuteQueryOperator(
	task_id='service_engagement_questionnaire__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.service_engagement_questionnaire__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.service_engagement_questionnaire__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

opportunity_extension__c= BigQueryExecuteQueryOperator(
	task_id='opportunity_extension__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.opportunity_extension__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.opportunity_extension__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

dashboard= BigQueryExecuteQueryOperator(
	task_id='dashboard',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.dashboard` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.dashboard` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sbqq__discounttier__c= BigQueryExecuteQueryOperator(
	task_id='sbqq__discounttier__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sbqq__discounttier__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sbqq__discounttier__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sbaa__approver__c= BigQueryExecuteQueryOperator(
	task_id='sbaa__approver__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sbaa__approver__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sbaa__approver__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

sbaa__approval__c= BigQueryExecuteQueryOperator(
	task_id='sbaa__approval__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.sbaa__approval__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.sbaa__approval__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

processnode= BigQueryExecuteQueryOperator(
	task_id='processnode',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.processnode` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.processnode` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

processinstanceworkitem= BigQueryExecuteQueryOperator(
	task_id='processinstanceworkitem',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.processinstanceworkitem` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.processinstanceworkitem` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)


specialist_forecast__c= BigQueryExecuteQueryOperator(
	task_id='specialist_forecast__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.specialist_forecast__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.specialist_forecast__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

industry__c= BigQueryExecuteQueryOperator(
	task_id='industry__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.industry__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.industry__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

product_relation__c= BigQueryExecuteQueryOperator(
	task_id='product_relation__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.product_relation__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.product_relation__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

resource_request__c= BigQueryExecuteQueryOperator(
	task_id='resource_request__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.resource_request__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.resource_request__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

loginhistory= BigQueryExecuteQueryOperator(
	task_id='loginhistory',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.loginhistory` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.loginhistory` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

asset= BigQueryExecuteQueryOperator(
	task_id='asset',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.asset` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.asset` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ioinsight__c= BigQueryExecuteQueryOperator(
	task_id='ioinsight__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ioinsight__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ioinsight__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

objectterritory2assignmentrule= BigQueryExecuteQueryOperator(
	task_id='objectterritory2assignmentrule',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.objectterritory2assignmentrule` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.objectterritory2assignmentrule` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

objectterritory2assignmentruleitem= BigQueryExecuteQueryOperator(
	task_id='objectterritory2assignmentruleitem',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.objectterritory2assignmentruleitem` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.objectterritory2assignmentruleitem` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ruleterritory2association= BigQueryExecuteQueryOperator(
	task_id='ruleterritory2association',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ruleterritory2association` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ruleterritory2association` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

linked_opportunity__c= BigQueryExecuteQueryOperator(
	task_id='linked_opportunity__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.linked_opportunity__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.linked_opportunity__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

contract_relation__c= BigQueryExecuteQueryOperator(
	task_id='contract_relation__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.contract_relation__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.contract_relation__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

medalliainvitationdata__c= BigQueryExecuteQueryOperator(
	task_id='medalliainvitationdata__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.medalliainvitationdata__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.medalliainvitationdata__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ltv_account__c= BigQueryExecuteQueryOperator(
	task_id='ltv_account__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ltv_account__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ltv_account__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

ltv_opportunity__c= BigQueryExecuteQueryOperator(
	task_id='ltv_opportunity__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.ltv_opportunity__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.ltv_opportunity__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

incident_management__c= BigQueryExecuteQueryOperator(
	task_id='incident_management__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.incident_management__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.incident_management__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

incident_account__c= BigQueryExecuteQueryOperator(
	task_id='incident_account__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.incident_account__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.incident_account__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

incident_contact__c= BigQueryExecuteQueryOperator(
	task_id='incident_contact__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.incident_contact__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.incident_contact__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

license_association__c= BigQueryExecuteQueryOperator(
	task_id='license_association__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.license_association__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.license_association__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

region__c= BigQueryExecuteQueryOperator(
	task_id='region__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.region__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.region__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

event_slot__c= BigQueryExecuteQueryOperator(
	task_id='event_slot__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.event_slot__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.event_slot__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

event_slot_job__c= BigQueryExecuteQueryOperator(
	task_id='event_slot_job__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.event_slot_job__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.event_slot_job__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

event_job__c= BigQueryExecuteQueryOperator(
	task_id='event_job__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.event_job__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.event_job__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

blng__billingtransaction__c= BigQueryExecuteQueryOperator(
	task_id='blng__billingtransaction__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.blng__billingtransaction__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.blng__billingtransaction__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

blng__billingschedule__c= BigQueryExecuteQueryOperator(
	task_id='blng__billingschedule__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.blng__billingschedule__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.blng__billingschedule__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

genesys_cloud_routing__c= BigQueryExecuteQueryOperator(
	task_id='genesys_cloud_routing__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.genesys_cloud_routing__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.genesys_cloud_routing__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

case_priority_routing__c= BigQueryExecuteQueryOperator(
	task_id='case_priority_routing__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.case_priority_routing__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.case_priority_routing__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

case_skills_routing__c= BigQueryExecuteQueryOperator(
	task_id='case_skills_routing__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.case_skills_routing__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.case_skills_routing__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

interaction_profile_log__c= BigQueryExecuteQueryOperator(
	task_id='interaction_profile_log__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.interaction_profile_log__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.interaction_profile_log__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

engineer_profile_mapping__c= BigQueryExecuteQueryOperator(
	task_id='engineer_profile_mapping__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.engineer_profile_mapping__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.engineer_profile_mapping__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

poc_product__c= BigQueryExecuteQueryOperator(
	task_id='poc_product__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.poc_product__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.poc_product__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

case_questionnaire__c= BigQueryExecuteQueryOperator(
	task_id='case_questionnaire__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.case_questionnaire__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.case_questionnaire__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

marketplace_account_mapping__c= BigQueryExecuteQueryOperator(
	task_id='marketplace_account_mapping__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.marketplace_account_mapping__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.marketplace_account_mapping__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

resource_request_attendees__c= BigQueryExecuteQueryOperator(
	task_id='resource_request_attendees__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.resource_request_attendees__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.resource_request_attendees__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)

case_dimension_mapping__c= BigQueryExecuteQueryOperator(
	task_id='case_dimension_mapping__c',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.case_dimension_mapping__c` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.case_dimension_mapping__c` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)


pricebook2history= BigQueryExecuteQueryOperator(
	task_id='pricebook2history',
	use_legacy_sql=False,
	allow_large_results=True,
	gcp_conn_id='bq-itq-aia-dp',
	labels={"dag_id": "{{ dag.dag_id | replace('.', '_') | lower }}","dag_run_id": "{{dag_run.id}}", "task_id": "{{ task.task_id | replace('.', '_') | lower }}", "run_id": "{{ run_id | replace(':', '__') | replace('+', '--') | replace('.', '_') | lower }}", },
	sql='''delete `itq-aia-datalake.sfdc_landing.pricebook2history` where concat(id, cast(record_ingestion_time as string)) in  (select distinct concat(id, cast(record_ingestion_time as string)) FROM (SELECT  *, row_number() over (partition by id order by record_ingestion_time desc) rno FROM `itq-aia-datalake.sfdc_landing.pricebook2history` ) as latest_rec where   (latest_rec.rno != 1 and timestamp_diff(current_timestamp(), latest_rec.record_ingestion_time, hour) > 1));''',
	dag=dag4)
