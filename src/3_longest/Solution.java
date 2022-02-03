import java.util.*;


// pwwkew
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 1) return 1;
        if (s.isEmpty()) return 0;
        
        int maxL = 0;
        String resp = "";
        
        for(char c : s.toCharArray()){
            if(resp.indexOf(c) != -1){
                if(resp.length() > maxL) maxL = resp.length();
                resp = resp.substring(resp.indexOf(c) + 1);
            }

            resp += c;          
        }
        
        if(resp.length() > maxL) return resp.length();
        
        return maxL;
    }
}