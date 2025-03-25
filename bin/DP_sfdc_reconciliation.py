# file location gs://itd-aia-airflow-dags/DP_sfdc_reconciliation.py
#gsutil cp gs://itd-aia-airflow-dags/DP_sfdc_reconciliation.py DP_sfdc_reconciliation.py



from datetime import timedelta, datetime
import json
from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator

default_args = {'owner': 'Data pipeline',
		'depends_on_past': False,
		'start_date': datetime(2019, 10, 8),
		'email': ['Data-Pipeline-Team@paloaltonetworks.com'],
		'email_on_failure': True,
		'email_on_retry': False, 'retries': 3,
		'retry_delay': timedelta(minutes=30)
			   }
# dag1 :truncate reload objects: recordtype, user, userrole, assignmentrule, group, groupmember, leadstatus, partnerrole, profile, territory2, userterritory2association, knowledgeableuser
#permissionset, permissionsetassignment, user_daily_once

dag1 = DAG(dag_id='DP_sfdc_Reconciliation1', default_args=default_args, schedule_interval='0 9 * * *')

# dag2 :critical objects: opportunity, account, opportunitylineitem, opportunitysplit, case etc...

dag2 = DAG(dag_id='DP_sfdc_Reconciliation2', default_args=default_args, schedule_interval='0 11 * * *')

# dag3 :GCP objects: opportunity, account, opportunitylineitem, opportunitysplit, case etc...
#cap_nominationreasons__c, cap_nominationreasons__history, cap_note__c, case_escalation__c, case_escalation__history, casecomment, casehistory, engagement__c, engagement__history, event,
# rma__c, support_case_audit__c,    product2, pricebook, account_customchangehistory__c, accounthistory, accreditations__c

dag3 = DAG(dag_id='DP_sfdc_Reconciliation3', default_args=default_args, schedule_interval='0 13 * * *')

t1 = SimpleHttpOperator( task_id='reconcile_userterritory2association', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=userterritory2association&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t2 = SimpleHttpOperator( task_id='reconcile_objectterritory2association', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=objectterritory2association&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t3 = SimpleHttpOperator( task_id='reconcile_opportunitycontactrole', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=opportunitycontactrole&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t4 = SimpleHttpOperator( task_id='reconcile_knowledgeableuser', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledgeableuser&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t5 = SimpleHttpOperator( task_id='reconcile_knowledgearticle', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledgearticle&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t6 = SimpleHttpOperator( task_id='reconcile_accountteammember', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=accountteammember&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t7 = SimpleHttpOperator( task_id='reconcile_knowledgearticleversion', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledgearticleversion&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t8 = SimpleHttpOperator( task_id='reconcile_knowledgearticleversionhistory', method='GET', http_conn_id='aia-dp-igw',
endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledgearticleversionhistory&days=90', headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t9 = SimpleHttpOperator( task_id='reconcile_knowledge__ka', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledge__ka&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t10 = SimpleHttpOperator( task_id='reconcile_knowledge__kav', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledge__kav&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t11 = SimpleHttpOperator( task_id='reconcile_groupmember', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=groupmember&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t12 = SimpleHttpOperator( task_id='reconcile_recordtype', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=recordtype&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t13 = SimpleHttpOperator( task_id='reconcile_user', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=user&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t13 = SimpleHttpOperator( task_id='reconcile_userrole', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=userrole&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t14 = SimpleHttpOperator( task_id='reconcile_assignmentrule', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=assignmentrule&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t15 = SimpleHttpOperator( task_id='reconcile_group', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=group&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t16 = SimpleHttpOperator( task_id='reconcile_leadstatus', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=leadstatus&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t17 = SimpleHttpOperator( task_id='reconcile_partnerrole', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=partnerrole&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t18 = SimpleHttpOperator( task_id='reconcile_profile', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=profile&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t19 = SimpleHttpOperator( task_id='reconcile_territory2', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=territory2&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t20 = SimpleHttpOperator( task_id='reconcile_permissionset', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=permissionset&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

t21 = SimpleHttpOperator( task_id='reconcile_permissionsetassignment', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=permissionsetassignment&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag1 )

### end of dag1 of trncate relaod objects

t22 = SimpleHttpOperator( task_id='reconcile_opportunity', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=opportunity&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag2 )

t23 = SimpleHttpOperator( task_id='reconcile_account', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=account&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag2 )

t24 = SimpleHttpOperator( task_id='reconcile_opportunitylineitem', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=opportunitylineitem&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag2 )

t25 = SimpleHttpOperator( task_id='reconcile_opportunitysplit', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=opportunitysplit&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag2 )

t26 = SimpleHttpOperator( task_id='reconcile_case', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=case&truncate=true&days=90',
 		headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag2 )

t27 = SimpleHttpOperator( task_id='reconcile_opportunitycontactrole', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=opportunitycontactrole&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t28 = SimpleHttpOperator( task_id='reconcile_cap_nominationreasons__c', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=cap_nominationreasons__c&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t29 = SimpleHttpOperator( task_id='reconcile_cap_nominationreasons__history', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=cap_nominationreasons__history&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t30 = SimpleHttpOperator( task_id='reconcile_cap_note__c', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=cap_note__c&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t31 = SimpleHttpOperator( task_id='reconcile_case_escalation__c', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=case_escalation__c&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t32 = SimpleHttpOperator( task_id='reconcile_case_escalation__history', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=case_escalation__history&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t33 = SimpleHttpOperator( task_id='reconcile_casecomment', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=casecomment&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t34 = SimpleHttpOperator( task_id='reconcile_casehistory', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=casehistory&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t35 = SimpleHttpOperator( task_id='reconcile_engagement__c', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=engagement__c&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t36 = SimpleHttpOperator( task_id='reconcile_engagement__history', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=engagement__history&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t37 = SimpleHttpOperator( task_id='reconcile_event', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=event&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t38 = SimpleHttpOperator( task_id='reconcile_rma__c', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=rma__c&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t39 = SimpleHttpOperator( task_id='reconcile_support_case_audit__c', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=support_case_audit__c&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t40 = SimpleHttpOperator( task_id='reconcile_product2', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=product2&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t41 = SimpleHttpOperator( task_id='reconcile_pricebook', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=pricebook&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t42 = SimpleHttpOperator( task_id='reconcile_account_customchangehistory__c', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=account_customchangehistory__c&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t43 = SimpleHttpOperator( task_id='reconcile_accounthistory', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=accounthistory&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t44 = SimpleHttpOperator( task_id='reconcile_accreditations__c', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=accreditations__c&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t45 = SimpleHttpOperator( task_id='reconcile_knowledge__datacategoryselection', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledge__datacategoryselection&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t48 = SimpleHttpOperator( task_id='reconcile_knowledgearticle', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledgearticle&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t49 = SimpleHttpOperator( task_id='reconcile_knowledgearticleviewstat', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledgearticleviewstat&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )

t50 = SimpleHttpOperator( task_id='reconcile_knowledgearticlevotestat', method='GET', http_conn_id='aia-dp-igw', endpoint='sfdc-reconcile-service/sfdc/reconcile?object=knowledgearticlevotestat&truncate=true&days=90',
headers={"Content-Type": "application/json","Accept": "application/json"}, dag=dag3 )
