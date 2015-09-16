//  Using java, have the function LongestWord(sen) take the sen parameter
//  being passed and return the largest word in the string. If there are two or more 
//  words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 


import java.util.*; 
import java.io.*;

class Function {  
  String LongestWord(String sen) { 
  
       String [] arr = sen.split(" ");
   
       Arrays.sort(arr);
    
       String longest = "";
    
       for(int i = 0; i < arr.length; i++){
  
	      longest = arr[0];
    
	}
    
	sen = longest;
	return sen;  
       
    return sen;
    
  } 
  
  public static void main (String[] args) {  
    // the function call should go here   
	System.out.println(LongestWord("Hey there Hellooooooooooo from Kenya")); 
  }   
  
}








  
