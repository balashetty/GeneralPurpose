package com.paloaltonetworks.itbi;


import java.io.File;
import java.net.URI;

import org.springframework.web.util.UriComponentsBuilder;

public class Test1 {

	public static void main(String[] args) {
		String gcsFilePath = "rawdata/AgreementFeed/year=2023/month=05/data.csv";
		int yi = gcsFilePath.indexOf("year");
		int mi = gcsFilePath.indexOf("month");
		String year = gcsFilePath.substring(yi + 5, yi + 5 + 4);
		String month = gcsFilePath.substring(mi + 6, mi + 6 + 2);
		System.out.println(year + ":" + month);
//		String dataFolder = System.getProperty("java.io.tmpdir");
//		System.out.println(dataFolder);
//		File file = new File(dataFolder + "/processed");
//	//	FileUtils.deleteQuietly(new File(dataFolder + "/processed"));
//
//		deleteDirectory(file);
//		   
//		String fileName = FilenameUtils.getBaseName("000000000000.part.6.csv");
//		String partNumber = fileName.substring(fileName.indexOf(".part.") + 6);
//		System.out.println(fileName + ":" + partNumber);
//		System.out.println("Double:" + Double.parseDouble(null));
		
		UriComponentsBuilder uriBuilder = UriComponentsBuilder
                .fromHttpUrl("https://paloaltonetworks--uat.sandbox.my.salesforce.com");
		
        
            uriBuilder = uriBuilder.queryParam("grant_type","password");
            uriBuilder = uriBuilder.queryParam("client_id","client");
            uriBuilder = uriBuilder.queryParam("client_secret", "client_secret");
            uriBuilder = uriBuilder.queryParam("username", "sfdcTokenUsername");
            uriBuilder = uriBuilder.queryParam("password", "sfdcToken#Password");
        
        URI url = uriBuilder.build().encode().toUri();
    	System.out.println("Printing URL:-"+url+"-");	
		
//		log.info("Printing qString:-"+qString+"-");
	}
	
	public static void  deleteDirectory(File file) {
	if (file == null || file.listFiles() == null)
		return;
	   for (File subfile : file.listFiles()) {  
           // if the subfile is a folder, recursively call the deleteDirectory()method  
           if (subfile.isDirectory()) {    // isDirectory() method is used to check whether subfile is a folder or not  
               deleteDirectory(subfile);  
           }  
           // use delete() method for deleting file and empty folder  
           subfile.delete();  
       }  

	}
}
