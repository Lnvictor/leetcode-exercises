import java.util.*;

class Solution {
    public String longestPalindrome(String s) {
    if (s.isEmpty()) return "";
        if (s.length() == 1) return s;
        if (s.length() > 1000) return null;
        
        String maxL = "";
        StringBuilder temp = new StringBuilder();
        
        //cbbd
        for (char c : s.toCharArray()){
            temp.append(c);
            
            String normal = temp.toString();
            String reverse =  new StringBuilder(String.valueOf(normal)).reverse().toString();
            
            if (normal.equals(reverse)){
                if (normal.length() > maxL.length()) { 
                    maxL = String.valueOf(normal);
                }
            }
            else {
	            while(normal.length() > 1) {
	            	normal = normal.substring(1);
	            	reverse = reverse.substring(0, reverse.length()-1);
	            	
	            	if (normal.length() > maxL.length() && normal.contentEquals(reverse)) 
	                    maxL = String.valueOf(normal);
	            }
            }
        }
        
        return maxL;
    }

}