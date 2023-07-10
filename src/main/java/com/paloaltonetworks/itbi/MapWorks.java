package com.paloaltonetworks.itbi;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import com.google.gson.Gson;

public class MapWorks {

	public static void main(String[] args) {
		String data = "{contentDetails={caption=false, definition=hd, dimension=2d, duration=PT12M47S, hasCustomThumbnail=true, licensedContent=false, projection=rectangular}, etag=u10iTZ9BMpyVDPORcZfvtmU8sCU, fileDetails={fileName=Tutorial Understanding the NAT-Security Policy Configuration.mp4}, id=Ahrao6kBg8w, kind=youtube#video, player={embedHtml=<iframe width=\"480\" height=\"270\" src=\"//www.youtube.com/embed/Ahrao6kBg8w\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>}, processingDetails={editorSuggestionsAvailability=inProgress, fileDetailsAvailability=inProgress, processingIssuesAvailability=inProgress, processingStatus=succeeded, tagSuggestionsAvailability=inProgress, thumbnailsAvailability=inProgress}, recordingDetails={}, snippet={categoryId=22, channelId=UCPRouchFt58TZnjoI65aelA, channelTitle=Palo Alto Networks LIVEcommunity, defaultAudioLanguage=en, description=This tutorial will clarify the configuration relationship between NAT policy rules and Security Policy rules and which values to configure for each. This tutorial provides a structured/consistently repeatable method for creating NAT (especially destination NAT) rules and corresponding Security Policy rules. If you have ever heard the term “pre-nat IP, post-nat zone” and been confused, this video will clarify that saying. This tutorial will also explain the behavior of Bi-directional NAT rules and when it is appropriate to use them., liveBroadcastContent=none, localized={description=This tutorial will clarify the configuration relationship between NAT policy rules and Security Policy rules and which values to configure for each. This tutorial provides a structured/consistently repeatable method for creating NAT (especially destination NAT) rules and corresponding Security Policy rules. If you have ever heard the term “pre-nat IP, post-nat zone” and been confused, this video will clarify that saying. This tutorial will also explain the behavior of Bi-directional NAT rules and when it is appropriate to use them., title=Tutorial: Understanding the NAT/Security Policy Configuration}, publishedAt=2017-11-08T21:11:34.000Z, tags=[NAT, Destination NAT, Security Policies, post-nat zone, bidirectional, bi-directional], thumbnails={default={height=90.0, url=https://i.ytimg.com/vi/Ahrao6kBg8w/default.jpg, width=120.0}, high={height=360.0, url=https://i.ytimg.com/vi/Ahrao6kBg8w/hqdefault.jpg, width=480.0}, medium={height=180.0, url=https://i.ytimg.com/vi/Ahrao6kBg8w/mqdefault.jpg, width=320.0}, standard={height=480.0, url=https://i.ytimg.com/vi/Ahrao6kBg8w/sddefault.jpg, width=640.0}}, title=Tutorial: Understanding the NAT/Security Policy Configuration}, statistics={commentCount=61, dislikeCount=14, favoriteCount=0, likeCount=1154, viewCount=95283}, status={embeddable=true, license=youtube, madeForKids=false, privacyStatus=public, publicStatsViewable=true, uploadStatus=processed}, topicDetails={topicCategories=[https://en.wikipedia.org/wiki/Business, https://en.wikipedia.org/wiki/Knowledge, https://en.wikipedia.org/wiki/Technology]}, localizations=[], record_ingestion_time=2023-06-25T11:06:09.516619Z}";
		System.out.println(new  Gson().toJson(convertWithStream(data)));
			
	}
	
	public static Map<String, String> convertWithStream(String mapAsString) {
	    Map<String, String> map = Arrays.stream(mapAsString.split(","))
	      .map(entry -> entry.split("="))
	      .collect(Collectors.toMap(entry -> entry[0], entry -> entry[1]));
	    return map;
	}
}
