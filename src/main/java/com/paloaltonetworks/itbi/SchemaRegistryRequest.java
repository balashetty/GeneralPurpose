package com.paloaltonetworks.itbi;

public class SchemaRegistryRequest {
	boolean hard_delete = true;
	boolean deleted = true;
	boolean create_new_subject = false;
	boolean copy_to_new_subject = false;
	boolean new_object = false;
	boolean new_object_fields= false;
	boolean delete_subject = false;
	boolean delete_object = false;
	boolean delete_objects = false;
	boolean delete_object_fields = false;
	boolean delete_subject_latest_version = false;
	boolean delete_subject_all_versions = false;
	boolean get_config = false;
	boolean get_all_subjects = false;
	boolean get_all_subjects_id_versions = false;
	boolean get_subject_latest_version = false;
	boolean update_compatibility = false;
	boolean checkup_active_schedule_and_cleanup_subject = false;
	boolean validate_json_subject_object_latest_schema = false;
	boolean validate_json_subject_object_backward_schema = false;
	boolean test_subject_objects_exists = false;
	boolean test_compatibility = false;
	boolean test_validity = false;
	boolean verbose = true;
	Integer id;
	Integer version;
	Integer backward_version = 1;
	String latestVersion = "latest";
	String jsonSchema;
	String subject_name;
	String copy_to_subject_name;
	String object_name;
	String[] object_fields;
	String[] objects;
	String compatibility;
	String event_name = "sfdc_event";
	String namespace = "com.paloaltonetworks.sfdc";
	String namespace_calulated = "com.paloaltonetworks.sfdc.calculated";
	public boolean isHard_delete() {
		return hard_delete;
	}
	public void setHard_delete(boolean hard_delete) {
		this.hard_delete = hard_delete;
	}
	public boolean isDeleted() {
		return deleted;
	}
	public void setDeleted(boolean deleted) {
		this.deleted = deleted;
	}
	public boolean isCreate_new_subject() {
		return create_new_subject;
	}
	public void setCreate_new_subject(boolean create_new_subject) {
		this.create_new_subject = create_new_subject;
	}
	public boolean isCopy_to_new_subject() {
		return copy_to_new_subject;
	}
	public void setCopy_to_new_subject(boolean copy_to_new_subject) {
		this.copy_to_new_subject = copy_to_new_subject;
	}
	public boolean isNew_object() {
		return new_object;
	}
	public void setNew_object(boolean new_object) {
		this.new_object = new_object;
	}
	public boolean isNew_object_fields() {
		return new_object_fields;
	}
	public void setNew_object_fields(boolean new_object_fields) {
		this.new_object_fields = new_object_fields;
	}
	public boolean isDelete_subject() {
		return delete_subject;
	}
	public void setDelete_subject(boolean delete_subject) {
		this.delete_subject = delete_subject;
	}
	public boolean isDelete_object() {
		return delete_object;
	}
	public void setDelete_object(boolean delete_object) {
		this.delete_object = delete_object;
	}
	public boolean isDelete_objects() {
		return delete_objects;
	}
	public void setDelete_objects(boolean delete_objects) {
		this.delete_objects = delete_objects;
	}
	public boolean isDelete_object_fields() {
		return delete_object_fields;
	}
	public void setDelete_object_fields(boolean delete_object_fields) {
		this.delete_object_fields = delete_object_fields;
	}
	public boolean isDelete_subject_latest_version() {
		return delete_subject_latest_version;
	}
	public void setDelete_subject_latest_version(boolean delete_subject_latest_version) {
		this.delete_subject_latest_version = delete_subject_latest_version;
	}
	public boolean isDelete_subject_all_versions() {
		return delete_subject_all_versions;
	}
	public void setDelete_subject_all_versions(boolean delete_subject_all_versions) {
		this.delete_subject_all_versions = delete_subject_all_versions;
	}
	public boolean isGet_config() {
		return get_config;
	}
	public void setGet_config(boolean get_config) {
		this.get_config = get_config;
	}
	public boolean isGet_all_subjects() {
		return get_all_subjects;
	}
	public void setGet_all_subjects(boolean get_all_subjects) {
		this.get_all_subjects = get_all_subjects;
	}
	public boolean isGet_all_subjects_id_versions() {
		return get_all_subjects_id_versions;
	}
	public void setGet_all_subjects_id_versions(boolean get_all_subjects_id_versions) {
		this.get_all_subjects_id_versions = get_all_subjects_id_versions;
	}
	public boolean isGet_subject_latest_version() {
		return get_subject_latest_version;
	}
	public void setGet_subject_latest_version(boolean get_subject_latest_version) {
		this.get_subject_latest_version = get_subject_latest_version;
	}
	public boolean isUpdate_compatibility() {
		return update_compatibility;
	}
	public void setUpdate_compatibility(boolean update_compatibility) {
		this.update_compatibility = update_compatibility;
	}
	public boolean isCheckup_active_schedule_and_cleanup_subject() {
		return checkup_active_schedule_and_cleanup_subject;
	}
	public void setCheckup_active_schedule_and_cleanup_subject(boolean checkup_active_schedule_and_cleanup_subject) {
		this.checkup_active_schedule_and_cleanup_subject = checkup_active_schedule_and_cleanup_subject;
	}
	public boolean isValidate_json_subject_object_latest_schema() {
		return validate_json_subject_object_latest_schema;
	}
	public void setValidate_json_subject_object_latest_schema(boolean validate_json_subject_object_latest_schema) {
		this.validate_json_subject_object_latest_schema = validate_json_subject_object_latest_schema;
	}
	public boolean isValidate_json_subject_object_backward_schema() {
		return validate_json_subject_object_backward_schema;
	}
	public void setValidate_json_subject_object_backward_schema(boolean validate_json_subject_object_backward_schema) {
		this.validate_json_subject_object_backward_schema = validate_json_subject_object_backward_schema;
	}
	public boolean isTest_subject_objects_exists() {
		return test_subject_objects_exists;
	}
	public void setTest_subject_objects_exists(boolean test_subject_objects_exists) {
		this.test_subject_objects_exists = test_subject_objects_exists;
	}
	public boolean isTest_compatibility() {
		return test_compatibility;
	}
	public void setTest_compatibility(boolean test_compatibility) {
		this.test_compatibility = test_compatibility;
	}
	public boolean isTest_validity() {
		return test_validity;
	}
	public void setTest_validity(boolean test_validity) {
		this.test_validity = test_validity;
	}
	public boolean isVerbose() {
		return verbose;
	}
	public void setVerbose(boolean verbose) {
		this.verbose = verbose;
	}
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public Integer getVersion() {
		return version;
	}
	public void setVersion(Integer version) {
		this.version = version;
	}
	public Integer getBackward_version() {
		return backward_version;
	}
	public void setBackward_version(Integer backward_version) {
		this.backward_version = backward_version;
	}
	public String getLatestVersion() {
		return latestVersion;
	}
	public void setLatestVersion(String latestVersion) {
		this.latestVersion = latestVersion;
	}
	public String getJsonSchema() {
		return jsonSchema;
	}
	public void setJsonSchema(String jsonSchema) {
		this.jsonSchema = jsonSchema;
	}
	public String getSubject_name() {
		return subject_name;
	}
	public void setSubject_name(String subject_name) {
		this.subject_name = subject_name;
	}
	public String getCopy_to_subject_name() {
		return copy_to_subject_name;
	}
	public void setCopy_to_subject_name(String copy_to_subject_name) {
		this.copy_to_subject_name = copy_to_subject_name;
	}
	public String getObject_name() {
		return object_name;
	}
	public void setObject_name(String object_name) {
		this.object_name = object_name;
	}
	public String[] getObject_fields() {
		return object_fields;
	}
	public void setObject_fields(String[] object_fields) {
		this.object_fields = object_fields;
	}
	public String[] getObjects() {
		return objects;
	}
	public void setObjects(String[] objects) {
		this.objects = objects;
	}
	public String getCompatibility() {
		return compatibility;
	}
	public void setCompatibility(String compatibility) {
		this.compatibility = compatibility;
	}
	public String getEvent_name() {
		return event_name;
	}
	public void setEvent_name(String event_name) {
		this.event_name = event_name;
	}
	public String getNamespace() {
		return namespace;
	}
	public void setNamespace(String namespace) {
		this.namespace = namespace;
	}
	public String getNamespace_calulated() {
		return namespace_calulated;
	}
	public void setNamespace_calulated(String namespace_calulated) {
		this.namespace_calulated = namespace_calulated;
	}
	
	
}