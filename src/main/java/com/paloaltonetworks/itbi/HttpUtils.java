package com.paloaltonetworks.itbi;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.HttpClientErrorException;

public class HttpUtils {
	private final static Logger log = LoggerFactory.getLogger(HttpUtils.class);

	public static boolean isOk(ResponseEntity<String> restResponse) {
		if (restResponse != null && restResponse.getStatusCode().is2xxSuccessful()) {
			return true;
		}
		return false;
	}

	public static boolean isOkResource(ResponseEntity<Resource> restResponse) {
		if (restResponse != null && restResponse.getStatusCode().is2xxSuccessful()) {
			return true;
		}
		return false;
	}

	public static boolean isTooManyRequests(ResponseEntity<String> restResponse) {
		if (restResponse.getStatusCode() == HttpStatus.TOO_MANY_REQUESTS) {
			return true;
		}
		return false;
	}

//	public static void wait(ResponseEntity<String> restResponse) {
//		Long timePeriod = 10L;
//		
//		List<String> values = restResponse.getHeaders().getOrEmpty("X-RateLimit-Remaining-Minute");
//
//		if (values.size() > 0) {
//			try {
//				Long remainingPerMinute = Long.parseLong(values.get(0));
//				
//				if (remainingPerMinute == 0) {
//					timePeriod = 60L;
//				}
//				log.info("X-RateLimit-Remaining-Minute {}, Sleeping for {} seconds", remainingPerMinute, timePeriod);
//			} catch (Exception e) {
//			}
//		} else {
//			log.info("Sleeping for {} seconds", timePeriod);
//		}
//
//		try {
//			Thread.currentThread().sleep(timePeriod * 1000);
//		} catch (Exception e) {
//		}
//	}
//
//	public static void wait(HttpClientErrorException.TooManyRequests tmre) {
//		Long timePeriod = 10L;
//		
//		log.info(tmre.getResponseHeaders().toString());
//		
//		List<String> values = tmre.getResponseHeaders().getOrEmpty("Retry-After");
//
//		if (values.size() > 0) {
//			try {
//				timePeriod = Long.parseLong(values.get(0));
//				log.info("Retry-After {}, Sleeping for {} seconds", values.get(0), timePeriod);
//			} catch (Exception e) {
//			}
//		} else {
//			log.info("Sleeping for {} seconds", timePeriod);
//		}
//		
//		
//		try {
//			Thread.sleep(timePeriod * 1000);
//		} catch (Exception e) {
//		}
//	}
	
	public static void wait(int timePeriod) {
		try {
			Thread.sleep(timePeriod * 1000);
		} catch (Exception e) {
		}
	}
}