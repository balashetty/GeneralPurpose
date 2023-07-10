package com.paloaltonetworks.itbi;

import java.io.File;

import org.apache.commons.io.FileUtils;
import org.apache.commons.io.FilenameUtils;

public class Test1 {

	public static void main(String[] args) {
		
		String dataFolder = System.getProperty("java.io.tmpdir");
		System.out.println(dataFolder);
		File file = new File(dataFolder + "/processed");
	//	FileUtils.deleteQuietly(new File(dataFolder + "/processed"));

		deleteDirectory(file);
		   
//		String fileName = FilenameUtils.getBaseName("000000000000.part.6.csv");
//		String partNumber = fileName.substring(fileName.indexOf(".part.") + 6);
//		System.out.println(fileName + ":" + partNumber);
//		System.out.println("Double:" + Double.parseDouble(null));
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
