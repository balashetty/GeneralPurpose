package com.paloaltonetworks.itbi;

public class SchemaRegistryResponse<T extends Object> {
	private Boolean success;
	private Boolean validationSuccess;
	private String error_code;
	private String error_message;
	private String validation_error_message;
	private String message;
	private String validationMessage;
	private T result;
	public boolean isSuccess() {
		return success;
	}
	public void setSuccess(boolean success) {
		this.success = success;
	}
	public String getError_code() {
		return error_code;
	}
	public void setError_code(String error_code) {
		this.error_code = error_code;
	}
	public String getError_message() {
		return error_message;
	}
	public void setError_message(String error_message) {
		this.error_message = error_message;
	}
	public String getMessage() {
		return message;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	public T getResult() {
		return result;
	}
	public void setResult(T result) {
		this.result = result;
	}
	public Boolean getSuccess() {
		return success;
	}
	public void setSuccess(Boolean success) {
		this.success = success;
	}
	public Boolean getValidationSuccess() {
		return validationSuccess;
	}
	public void setValidationSuccess(Boolean validationSuccess) {
		this.validationSuccess = validationSuccess;
	}
	public String getValidation_error_message() {
		return validation_error_message;
	}
	public void setValidation_error_message(String validation_error_message) {
		this.validation_error_message = validation_error_message;
	}
	public String getValidationMessage() {
		return validationMessage;
	}
	public void setValidationMessage(String validationMessage) {
		this.validationMessage = validationMessage;
	}
	@Override
	public String toString() {
		return "SchemaRegistryResponse [success=" + success + ", validationSuccess=" + validationSuccess
				+ ", error_code=" + error_code + ", error_message=" + error_message + ", validation_error_message="
				+ validation_error_message + ", message=" + message + ", validationMessage=" + validationMessage
				+ ", result=" + result + "]";
	}
	
}
