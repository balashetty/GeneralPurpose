package com.paloaltonetworks.itbi;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class DateTimeTest {
	private static final Logger log = LogManager.getLogger(DateTimeTest.class);

	public static void main(String[] args) {
		
		LocalDateTime localDateTime = LocalDateTime.of(2024, 3, 6, 15, 51, 01);
		LocalDateTime localDateTimeNow = LocalDateTime.now(ZoneId.of("America/Los_Angeles"));
		LocalDateTime localDateTimeNowUtc = LocalDateTime.now(ZoneId.of("UTC"));

		if (localDateTimeNowUtc.isAfter(localDateTime.now())) {
			log.info ("after");
		} else {
			log.info ("before");
		}
		
	}
}
