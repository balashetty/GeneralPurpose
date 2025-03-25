package com.paloaltonetworks.itbi;

public class AvroSchema {
	private String schema;
	private Integer version;
	private Integer id;
	private String subject;
	public String getSchema() {
		return schema;
	}
	public void setSchema(String schema) {
		this.schema = schema;
	}
	public Integer getVersion() {
		return version;
	}
	public void setVersion(Integer version) {
		this.version = version;
	}
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getSubject() {
		return subject;
	}
	public void setSubject(String subject) {
		this.subject = subject;
	}
	@Override
	public String toString() {
		return "AvroSchema [schema=" + schema + ", version=" + version + ", id=" + id + ", subject=" + subject + "]";
	}
}
